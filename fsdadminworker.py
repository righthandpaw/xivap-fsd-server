import re
import socket
import threading
import time
import json
import sys

from fsdclientinfo import fsdclientinfo
from fsdnetwork import fsdnetwork

class fsdadminworker(fsdnetwork):
	def __init__(self,FSDregistry,FSDapi,FSDprotocol,FSDp2ppool,bind_ip,bind_port,worker_type):
		fsdnetwork.__init__(self,FSDregistry,FSDapi,FSDprotocol,FSDp2ppool,bind_ip,bind_port,worker_type)
		
	def worker(self,admin_socket):
		
		laddr = admin_socket.getsockname()
		raddr = admin_socket.getpeername()
		print(dir(admin_socket))
		print(admin_socket)
		print('$CQMYUID:THEIRID:P2P:2:PPOS1:{}:{}:{}:{}\n\r'.format(raddr[0],raddr[1],laddr[0],laddr[1]))
		print()
		
			
		#print(admin_address)
		#do some work
		
		#close socket
		admin_socket.close()