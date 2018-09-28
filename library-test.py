import re
import threading
from threading import Lock
#from fsdp2ppool import fsdp2ppool
from fsdregistry import fsdregistry
from pprint import pprint
import time


class tester():

	def __init__(self):
		self.fsdinforequest	=	"$CQ"
		self.FSDregistry = fsdregistry()

	
	def main(self):	

		
		
		a_thread = threading.Thread(target=self.workerA,)
		b_thread = threading.Thread(target=self.workerB,)
		c_thread = threading.Thread(target=self.workerC,)
		a_thread.start()
		b_thread.start()
		c_thread.start()
		
		
	def workerA(self):	



		sentences = [
					'#DLAAAAA',
					]
		
		for sentence in sentences:
			self.FSDregistry.AddMessage(sentence)
		
		time.sleep(2)
		print(self.FSDregistry.GetMessage())


	def workerB(self):
		

		
		sentences = [
					'#MDBBBB:B722',
					]
		
		for sentence in sentences:
			self.FSDregistry.AddMessage(sentence)

		time.sleep(2)
		print(self.FSDregistry.GetMessage())


	def workerC(self):
		
		sentences = [
					'#MDCCCC:C172',
					]
		
		for sentence in sentences:
			self.FSDregistry.AddMessage(sentence)
		time.sleep(2)	
		print(self.FSDregistry.GetMessage())
		
	def watcher(self,callsign):
	
		
		t = threading.currentThread()
		
	
		
				
	
tester().main()	
#MyServer = tester()