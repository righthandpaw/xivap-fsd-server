import sys
import socket
import threading

class fsdnetwork:
	def __init__(self,FSDregistry,FSDapi,FSDprotocol,bind_ip,bind_port,worker_type):


		self.bufferSize		= 1024
		self.FSDregistry	= FSDregistry
		self.FSDapi 		= FSDapi
		self.FSDprotocol	= FSDprotocol

		self.fsdserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.fsdserver.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		
		self.fsdserver.bind((bind_ip, bind_port))
		self.fsdserver.listen(20)  # max backlog of connections
		
		print("Starting {} Thread - Listening on {}:{}".format(worker_type,bind_ip, bind_port))
		
		while True:
			client_socket, client_address = self.fsdserver.accept()
			print ('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))
			
			#thread code (Recieving)
			fsd_thread = threading.Thread(target=self.worker, args=(client_socket,))
			fsd_thread.start()
		
	#Threaded handler
	def worker(self,client_socket):
		#leave this to be overridden
		return True
	
		