import re
from fsdprotocol import fsdprotocol
from threading import Lock, Thread

class fsdp2ppool:
	
	def __init__(self):
		FSD					=	fsdprotocol()
		self.__counter		= 0
		self.__lock 		= Lock()
		self.__clientPool 	= {}
		
	def AddRequests(self,message):
		#$CQAAAA:BBBB:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
		self.__lock.acquire()
		self.__clientPool[self.__counter]={
			"from":message[0],
			"to":message[1],
			"mode":message[3], 
			"publicip":message[5], 
			"publicport":message[6], 
			"privateip":message[7],
			"privateport": message[8]
		}
		self.__counter = self.__counter+1
		lock.release()
		
	def GetRequests(self,callsign):
		print(self.__clientPool)
		
		
			