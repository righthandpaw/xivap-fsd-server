import re
import threading
from threading import Lock
import copy
from fsdprotocol import fsdprotocol
from pprint import pprint  

class fsdp2ppool():
	
	def __init__(self):
		self.FSD			= fsdprotocol()
		self.__counter		= 0
		self.__clientPool 	= {}
		self.td 			= threading.Condition()
		
	def AddRequests(self,words):
		#$CQAAAA:BBBB:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
		#$CRBBBB:AAAA:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
		
		
		#self.lock.acquire(True)
		
		
		status=self.td.acquire()
		
		
		matches = re.match('(\\'+self.FSD.FSDInfoRequest()+'|\\'+self.FSD.FSDInfoReply()+')([A-Za-z0-9]+)',words[0])
		requesttype		= matches.group(1)
		fromCallsign 	= matches.group(2)
		toCallsign 		= words[1]
		mode 			= words[3]
		publicip 		= words[5]
		publicport 		= words[6]
		privateip 		= words[7]
		privateport 	= words[8]
		key = ("{}{}").format(fromCallsign,toCallsign)
		
		self.__clientPool[key]={
			'requesttype':requesttype,
			'fromCallsign':fromCallsign,
			'mode':mode,
			'publicip':publicip,
			'publicport':publicport,
			'privateip':privateip,
			'privateport':privateport,
			'toCallsign':toCallsign,
			'status':'pending'
		}
		
		status = self.td.release()
		
		
		
		
		
	def GetRequests(self,toCallsign):

		clientPool = self.__clientPool.copy()
		local = {}
		for key in clientPool.keys():
			if toCallsign in clientPool[key]['toCallsign']:
				local[key]= clientPool[key]

		return local	
	
	def UpdateRequests(self,key):
		self.__clientPool[key]['status']='sent'
		