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
		
		laddress = client_socket.getsockname()
		raddress = client_socket.getpeername()

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
					client = self.FSDapi.AddPilot(words,laddress,raddress,client,self.FSDregistry)
					if client.GetVerification() == True:
						self.FSDregistry.UpdateRegistry(client)
					else:
						for error in client.GetError():
							print(client.GetError()[error])

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
				
				
				#--===The P2P handshake===--
				#The format of the P2P handshake looks something like this
				#ourselves::theOtherPerson:ourPublicIp:ourPrivateIP
				#$CQAAAA:BBBB:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
				if regex.match('\\'+self.FSDprotocol.FSDInfoRequest(),command):
				
					self.FSDp2ppool.AddRequests(words)
					self.FSDp2ppool.GetRequests(self.FSDregistry.GetCallSign(self.FSDregistry.GetMyID()))
				
					client = self.FSDapi.InfoRequest(words,client)	
					self.FSDregistry.UpdateRegistry(client)
					
					
					
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
							
							#we probably need to see if recived something like this first:
							'''
							-PRNR1919:DIROB11
							-MRNR1919:DIROB11
							$CRNR1919:DIROB11:P2P:2:PPOS1:127.36.130.77:23710:192.168.1.4:19561
							'''
							
							#then we will need to send 
							'''
							-PDDIROB11:NR1919:KODIIND
							-MDDIROB11:NR1919:
							'''
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
							
							
							
							

		#close connection
		client_socket.close()
		#clean up the Registry	
