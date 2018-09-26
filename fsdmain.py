import re
import socket
import threading
from threading import Lock, Thread
import time
import json
import sys
from fsdapi import fsdapi
from fsdprotocol import fsdprotocol
from fsdregistry import fsdregistry
from fsdclientinfo import fsdclientinfo
from fsdclientworker import fsdclientworker
from fsdadminworker import fsdadminworker
from fsdp2ppool import fsdp2ppool 

class fsdmain:
	
	def __init__(self):
	
		self.FSDregistry 	= fsdregistry()
		self.FSDapi 		= fsdapi()
		self.FSDprotocol 	= fsdprotocol()
		self.FSDp2ppool		= fsdp2ppool()
		print("Starting Server")
		
		#server code	

		fsd_bind_ip = '0.0.0.0'
		fsd_bind_port = 6809
		
		adm_bind_ip = '0.0.0.0'
		adm_bind_port = 6805
		
		#start FSD server
		
		server_thread = threading.Thread(target=fsdclientworker, args=(self.FSDregistry,self.FSDapi,self.FSDprotocol,self.FSDp2ppool,fsd_bind_ip,fsd_bind_port,"FSD",))
		server_thread.start()
		
		
		admin_thread = threading.Thread(target=fsdadminworker, args=(self.FSDregistry,self.FSDapi,self.FSDprotocol,self.FSDp2ppool,adm_bind_ip,adm_bind_port,"Admin",))
		admin_thread.start()

