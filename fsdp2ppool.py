from threading import Lock, Thread

class fsdp2ppool:
	
	def __init__(self):
		self.__counter	= 0
		self.__lock = Lock()
		self.__clientPool = {}
		
	def AddMyMessage(self,message):
		self.__lock.acquire()
		self.__clientPool[self.__counter]={
			"from":message[0],
			"to":message[1],
			"mode":message[2], 
			"publicip":message[3], 
			"publicport":message[4], 
			"privateip":message[5],
			"privateport": message[6]
		}
		self.__counter = self.__counter+1
		lock.release()
		
	def GetMyMessages(self,callsign):
		localRegistry = {}
		
			