import re
import threading
import copy
from threading import Lock, Thread
from fsdprotocol import fsdprotocol 

class fsdp2ppool():
	
	def __init__(self):
		self.FSD			= fsdprotocol()
		self.__counter		= 0
		self.__lock 		= Lock()
		self.__clientPool 	= {}
		
	def AddRequests(self,words):
		#$CQAAAA:BBBB:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
		self.__lock.acquire(True,1)
		matches = re.match('\\'+self.FSD.FSDInfoRequest()+'([A-Za-z0-9]+)',words[0])
		callsign = matches.group(1)
	
		self.__clientPool[self.__counter]={
			"from":callsign,
			"to":words[1],
			"mode":words[3], 
			"publicip":words[5], 
			"publicport":words[6], 
			"privateip":words[7],
			"privateport": words[8]
		}
		self.__counter = self.__counter+1
		self.__lock.release()
		
	def GetRequests(self,callsign):
	
		self.__lock.acquire(True,1)
		#take a snapshot of the clientpool since the size could be modified
		x = 0
		localPool = self.__clientPool.copy()
		localRegistry = {}

		for i in localPool:
			if callsign in localPool[i]["to"]:
				localRegistry[x] = localPool[i]
				x=x+1

		self.__lock.release()
		return localRegistry
		
			