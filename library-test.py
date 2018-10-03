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
		
	
class duallibs():
	def __init__(self):
		self.registy={}

	def main(self):
		localRegistry={}

		self.registy['X01']={
			"pilot":"aaaa"
		}

		self.registy['X02']={
			"pilot":"bbbb"
		}

		self.registy['X03']={
			"pilot":"cccc"
		}



				
		localRegistry['X01']={
			"pilot":"aaaa"
		}		
	



		print("self.registry = ", self.registy)
		print("localRegisty = ",localRegistry)






		if len(self.registy) >= len(localRegistry):
			for key in self.registy.keys():
				if key not in localRegistry:
					localRegistry[key]={
						"pilot":self.registy[key]["pilot"],
					}


		


		print("localRegisty = ",localRegistry)
		self.registy.pop('X01',None)
		print(self.registy)

		if len(self.registy) <= len(localRegistry):
			print("have to remove pilot")
			for key in localRegistry.copy():
				if key not in self.registy:
					print("this {} is nolonger in self.registry, deleting from localRegistry".format(key))
					localRegistry.pop(key,None)
		
		



		if len(self.registy) >= len(localRegistry):
			for key in self.registy.keys():
				if key not in localRegistry:
					localRegistry[key]={
						"pilot":self.registy[key]["pilot"],
					}

		if len(self.registy) <= len(localRegistry):
			for key in localRegistry.copy():
				if key not in self.registy:
					print("this {} is nolonger in self.registry, deleting from localRegistry".format(key))
					localRegistry.pop(key,None)








		
		print(localRegistry)
	

		#Thoughts, check the lengths if self.registry is longer the local reg is missing
		#if local is longer then we need to delete
		#if they are the same compare keys


#tester().main()	
duallibs().main()