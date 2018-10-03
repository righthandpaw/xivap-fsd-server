import re
import socket
import threading
import time
import json
import sys

from fsdclientinfo import fsdclientinfo
from fsdnetwork import fsdnetwork

class fsdclientworker(fsdnetwork):
	def __init__(self,FSDregistry,FSDapi,FSDprotocol,FSDp2ppool,bind_ip,bind_port,worker_type):
		fsdnetwork.__init__(self,FSDregistry,FSDapi,FSDprotocol,FSDp2ppool,bind_ip,bind_port,worker_type)
	
	def sendToOne(self,myID,toCallsign,message):
		print(myID,toCallsign,message)

		for otherUserID in self.FSDregistry.GetRegistryKeys():
			print(self.FSDregistry.GetCallSign(otherUserID))

			if self.FSDregistry.GetCallSign(otherUserID) == toCallsign:
				otherConnecton = self.FSDregistry.GetConnection(otherUserID)
				print(toCallsign,message)
				otherConnecton.send(message.encode())

	def sendToAll(self,myID,message):
		print(myID,message)
		#Quick broadcast test will move this to it's on thing later
		for otherUserID in self.FSDregistry.GetRegistryKeys():
			#except ourselve's ofcourse
			if otherUserID is not myID:
				otherConnecton = self.FSDregistry.GetConnection(otherUserID)
				otherConnecton.send(message.encode())

	def worker(self,client_socket):

		regex = re
		client=fsdclientinfo()
		localRegistry = {}
		

		i = 0
		forever = True
		while forever is True:
			request = client_socket.recv(self.bufferSize)
			message = request.decode()
			
			#if the messages gets appended we need to break them apart
			sentences = message.split("\r\n")
			print(sentences)
			
			for sentence in sentences:

				words = sentence.split(":")
				command = words[0]

				if not request:
					forever = False
				
				#Add a pilot
				if regex.match(self.FSDprotocol.FSDAddPilot(),command):
					client = self.FSDapi.AddPilot(words,client_socket,client,self.FSDregistry)
					if client.GetVerification() == True:
						self.FSDregistry.UpdateRegistry(client)

						motds = {	"Python FSD Flight server\r\n",
									"Based on Open XIVAP Protocol\r\n",
									"Enjoy your flight!\r\n",
								}
						for motd in motds:
							string = ("#TMserver:{}:{}\r\n".format(self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()),motd)) 
							client_socket.send(string.encode())	

					else:
						for error in client.GetError():
							print(client.GetError()[error])
							forever = False

				#Delete pilot
				if regex.match(self.FSDprotocol.FSDDeletePilot(),command):
					self.FSDregistry.DeleteKey(self.FSDregistry.GetMyID())
					forever = False

				#Plane Info				
				if regex.match(self.FSDprotocol.FSDPlaneInfo(),command):
					client = self.FSDapi.PlaneInfo(words,client)
					self.FSDregistry.UpdateRegistry(client)	
					for otherUserID in self.FSDregistry.GetRegistryKeys():
						#except ourselve's ofcourse
						if otherUserID is not self.FSDregistry.GetMyID():
							sendPD = ("-PD{}:{}:{}\r\n".format(
									self.FSDregistry.GetCallSign(otherUserID),
									self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()),
									self.FSDregistry.GetAirPlane(otherUserID)
							
							))

							sendMD = ("-PM{}:{}:\r\n".format(
									self.FSDregistry.GetCallSign(otherUserID),
									self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID())
							
							))

							client_socket.send(sendPD.encode())
							print(sendPD)
							client_socket.send(sendMD.encode())
							print(sendMD)
				
				#P2PRequest
				#$CQDIROB11:NR1919:P2P:2:PPOS1:172.113.78.203:17504:192.168.0.7:17504 
				if regex.match('\\'+self.FSDprotocol.FSDInfoRequest(),command):
					self.FSDp2ppool.AddRequests(words)
					
					
				#P2PReply
				if regex.match('\\'+self.FSDprotocol.FSDInfoReply(),command):
					p2pstr = ("{}\r\n".format(sentence))
					self.FSDp2ppool.AddRequests(words)
					
				

				#Plane Params (Don't know what this is used for but it is called after it recieves the welcome message				
				if regex.match(self.FSDprotocol.FSDPlaneParams(),command):
					print(command);
						
				#Pilot Position
				#example we recieve the following string the our client:
				# @S:NR1919:2726:-1:43.76174:-99.31855:1684:0:4282384454:0
				
				if regex.match(self.FSDprotocol.FSDPilotPosition(),command):
					client = self.FSDapi.PilotPosition(words,client)
					#we update our client's position in the global registry
					self.FSDregistry.UpdateRegistry(client)


					#if a new pilot happens to come on board we need to add them 
					if len(self.FSDregistry.GetRegistryKeys())-1 >= len(localRegistry):
						for key in self.FSDregistry.GetRegistryKeys():
							if key is not self.FSDregistry.GetMyID():
								if key not in localRegistry:
									print("Adding pilotID = ",key)
									localRegistry[key]={
										"callsign":self.FSDregistry.GetCallSign(key)
									}
									addOtherPilotstr = (	
										"#AP{}:{}:{}::{}:{}:{}\r\n".format(
							
										self.FSDregistry.GetCallSign(key),
										self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()),
										key,
										self.FSDregistry.GetRank(key),
										self.FSDregistry.GetFsdVer(key),
										self.FSDregistry.GetSimVer(key),
									))
									client_socket.send(addOtherPilotstr.encode())
					print(len(self.FSDregistry.GetRegistryKeys())-1,len(localRegistry))

					if len(self.FSDregistry.GetRegistryKeys())-1 <= len(localRegistry):
							for key in localRegistry.copy():
								print(key)
								if key not in self.FSDregistry.GetRegistryKeys():
									print("this {} is nolonger in self.registry, deleting from localRegistry".format(key))
									delPilotStr = ("#DP{}\r\n".format(localRegistry[key]['callsign']))
									client_socket.send(delPilotStr.encode())
									localRegistry.pop(key,None)





					#Next we need to have the server query the global registry 
					#and send us everyone's position 
					for otherUserID in self.FSDregistry.GetRegistryKeys():
						#except ourselve's ofcourse
						if otherUserID is not self.FSDregistry.GetMyID():

							#format
							#@S:DIROB11:1554:11:43.76123:-99.31627:1695:0:4261416526:-84




							Posstr = (	"@{}:{}:{}:{}:{}:{}:{}:{}:{}:{}\r\n".format(
									self.FSDregistry.GetIdent(otherUserID),
									self.FSDregistry.GetCallSign(otherUserID),
									self.FSDregistry.GetTransponder(otherUserID),
									self.FSDregistry.GetRating(otherUserID),
									self.FSDregistry.GetLatitude(otherUserID),
									self.FSDregistry.GetLongitude(otherUserID),
									self.FSDregistry.GetTrueAlt(otherUserID),
									self.FSDregistry.GetSpeed(otherUserID),
									self.FSDregistry.GetPitchBankHeading(otherUserID),
									self.FSDregistry.GetGround(otherUserID)
							))
							
							#but whatever's were gona send this just to see what happens
							client_socket.send(Posstr.encode())
					
					##DO The p2p stuff here
					
					p2pclient = self.FSDp2ppool.GetRequests(self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()))
					for key in p2pclient:
						if p2pclient[key]['status'] == 'pending':
							
							p2pstring = ("{}{}:{}:P2P:{}:PPOS1:{}:{}:{}:{}\r\n".format(
								p2pclient[key]['requesttype'],
								p2pclient[key]['fromCallsign'],
								p2pclient[key]['toCallsign'],
								p2pclient[key]['mode'],
								p2pclient[key]['publicip'],
								p2pclient[key]['publicport'],
								p2pclient[key]['privateip'],
								p2pclient[key]['privateport']
							))
							print(p2pclient)
							client_socket.send(p2pstring.encode())
							self.FSDp2ppool.UpdateRequests(key)
										
		#Remove pilot
		#if client.GetError()[error]
		#if client.GetVerification() == True:
		#self.FSDp2ppool.ClearPool()
		#print(self.FSDregistry.GetMyID())
		#self.FSDregistry.DeleteKey(self.FSDregistry.GetMyID())
			

		#close connection		
		client_socket.close()
		#clean up the Registry	
