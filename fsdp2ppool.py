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
		self.count			= 0
		
		
	def AddRequests(self,words):
		#$CQAAAA:BBBB:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
		#$CRBBBB:AAAA:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
		
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
		key 			= ("{}{}").format(fromCallsign,toCallsign)
		reversekey 		= ("{}{}").format(toCallsign,fromCallsign)
		self.count 		= self.count+1
		
		doesExist		= False
		
		#check if the reverse key exists already
		#if it does we need to check the Request
		
		print("Pass #",self.count)
		print("does this key: {} exist?".format(reversekey))
		if reversekey in self.__clientPool:
			print("yes ... gotta check something")
			if self.__clientPool[reversekey]['requesttype'] == requesttype:
				print("We already sent this so we do not have to send again.")
				doesExist = True
			else:
				print("This does not exist so we can add it to the pile")
				doesExist = False
			
		else:
			doesExist = False
			print("no ... adding! ",key)
			
		if doesExist == False:	
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
		