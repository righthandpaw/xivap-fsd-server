import re
import threading
from threading import Lock
from fsdp2ppool import fsdp2ppool
from pprint import pprint
import time


class tester():

	def __init__(self):
		self.fsdinforequest	=	"$CQ"
		self.FSDp2ppool = fsdp2ppool()

	
	def main(self):	

		
		
		a_thread = threading.Thread(target=self.workerA,)
		

		b_thread = threading.Thread(target=self.workerB,)
		b_thread.start()
		a_thread.start()
		
	def workerA(self):	

		
	
	
		sentences = [
					'$CQNR1918:NR1919:P2P:2:PPOS1:114.158.182.21:24062:127.0.0.1:29587',
					]
		
		for sentence in sentences:
			self.FSDp2ppool.AddRequests(sentence.split(':'))
		
		w_thread = threading.Thread(target=self.watcher,args=('NR1918',))
		w_thread.start()		


	def workerB(self):
		

		sentences = [
					'$CQNR1919:NR1918:P2P:2:PPOS1:114.158.182.21:21870:127.0.0.1:29512',

					]
		
		for sentence in sentences:
			self.FSDp2ppool.AddRequests(sentence.split(':'))
	
		watcher = threading.Thread(target=self.watcher,args=('NR1919',))
		watcher.start()

		
	def watcher(self,callsign):
	
		print("Give me all messages for Callsign - {}".format(callsign))
		#run this in a loop 
		
		while True:
			waiting = True
			while waiting is True:
				if self.FSDp2ppool.GetRequests(callsign) != {}:
					waiting = False
			
			p2pclient = self.FSDp2ppool.GetRequests(callsign)
			for key in p2pclient:
				if p2pclient[key]['status'] == 'pending':
					#print("sending")
					#print(p2pclient[key])
					self.FSDp2ppool.UpdateRequests(key)
					print(p2pclient[key])
		
		
		
	
		

		
	
tester().main()	
#MyServer = tester()