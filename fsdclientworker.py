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
		
	def worker(self,client_socket):

		regex = re
		client=fsdclientinfo()
		raddress = client_socket.getpeername()
		
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
					client = self.FSDapi.AddPilot(words,raddress,client,self.FSDregistry)
					if client.GetVerification() == True:
						self.FSDregistry.UpdateRegistry(client)
					else:
						for error in client.GetError():
							print(client.GetError()[error])
							forever = False

				#Delete pilot
				if regex.match(self.FSDprotocol.FSDDeletePilot(),command):
					#place message on announcement que
					#self.FSDregistry.AddMessage()					
					#remove the pilot from the pool
					self.FSDregistry.UpdateRegistry(client,'deletePilot')
					forever = False

				#Plane Info				
				if regex.match(self.FSDprotocol.FSDPlaneInfo(),command):
					client = self.FSDapi.PlaneInfo(words,client)
					if client.GetVerification() == True:
						self.FSDregistry.UpdateRegistry(client)
						
						
						motds = {	"Python FSD Flight server\r\n",
									"Based on Open XIVAP Protocol\r\n",
									" \r\n",
									"Enjoy your flight!\r\n",
								}
						for motd in motds:
							string = ("#TMserver:{}:{}\r\n".format(self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()),motd)) 
							client_socket.send(string.encode())			
					else:
						#You get nothing
						print()
				

				#P2PRequest
				if regex.match('\\'+self.FSDprotocol.FSDInfoRequest(),command):
					self.FSDp2ppool.AddRequests(words)
					
				#P2PReply
				if regex.match('\\'+self.FSDprotocol.FSDInfoReply(),command):
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
	
					#Next we need to have the server query the global registry 
					#and send us everyone's position 
					for otherUserID in self.FSDregistry.GetRegistryKeys():
						#except ourselve's ofcourse
						if otherUserID is not self.FSDregistry.GetMyID():

							#format
							#@S:DIROB11:1554:11:43.76123:-99.31627:1695:0:4261416526:-84

							string = (	"@{}:{}:{}:{}:{}:{}:{}:{}:{}:{}\r\n".format(
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
							
							#as a test we are just going to send this along to the client
							sendPD = ("-PD{}:{}:{}\r\n".format(
									self.FSDregistry.GetCallSign(otherUserID),
									self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()),
									self.FSDregistry.GetAirPlane(otherUserID)
							
							))
							
							
							sendMD = ("-PM{}:{}:\r\n".format(
									self.FSDregistry.GetCallSign(otherUserID),
									self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID())
							
							))
							
							
							if i is not 1:
								client_socket.send(sendPD.encode())
								print(sendPD)
								client_socket.send(sendMD.encode())
								print(sendMD)
								i=1
							
							#but whatever's were gona send this just to see what happens
							client_socket.send(string.encode())
					
					##DO The p2p stuff here

					p2pclient = self.FSDp2ppool.GetRequests(self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()))
					for key in p2pclient:
						if p2pclient[key]['status'] == 'pending':
							#print("sending")
							#print(p2pclient[key])
							#$CQAAAA:BBBB:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
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
							
							client_socket.send(p2pstring.encode())
							self.FSDp2ppool.UpdateRequests(key)
							#print(p2pclient[key])



							
							
		#Remove pilot
		#if client.GetError()[error]


		#close connection		
		client_socket.close()
		#clean up the Registry	
