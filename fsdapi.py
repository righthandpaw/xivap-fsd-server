import re
from fsdprotocol import fsdprotocol
from fsdclientinfo import fsdclientinfo

class fsdapi:


	def __init__(self):
		FSD					=	fsdprotocol()
		self.FSDAddPilot	=	FSD.FSDAddPilot()
		self.FSDPlaneInfo	=	FSD.FSDPlaneInfo()
		self.FSDFlightPlan	= 	FSD.FSDFlightPlan()
		self.FSDPilotPosition = FSD.FSDPilotPosition()
		self.FSDInfoRequest	=	FSD.FSDInfoRequest()	
	
	def AddPilot(self,words,laddress,raddress,client,registry):
		
		matches		= re.match(self.FSDAddPilot+'([A-Za-z0-9]+)',words[0])
		callsign 	= matches.group(1)
		username	= words[2]
		password	= words[3]
		
		local_address	= laddress[0]
		local_port		= laddress[1]
		remote_address	= raddress[0]
		remote_port		= raddress[1]

		errorCount = 0
		
		#cleck to see if registry
		existingClient = registry.GetRegistry()

		if username in existingClient.keys():
			client.SetVerification(False)
			client.SetError(errorCount,"Already Logged In")
			errorCount+=1
		else:		
			client.SetVerification(True)
			
		for val in existingClient.keys():
			if existingClient[val]["callsign"]==callsign:
				client.SetVerification(False)
				client.SetError(errorCount,"Callsign areadly in use")
				errorCount+=1
	
		client.SetUserName(username)
		client.SetPassword(password)
		client.SetLocalAddress(local_address)
		client.SetLocalPort(local_port)
		client.SetRemoteAddress(remote_address)
		client.SetRemotePort(remote_port)
		client.SetCallSign(callsign)
		client.SetFullName(words[7])

		return client
		

	def PlaneInfo(self,words,client):
	
		airplane = words[2]
		client.SetAirPlane(airplane)
		
		return client

	
	def FlightPlan(self,words):
		matches = re.match(self.FSDPlaneInfo+'([A-Za-z0-9]+)',words[0])
		return(matches)
		
	def PilotPosition(self,words,client):
		# ident callsign transponder rating latitude longitude truealt speed pitchbankheading
		#@N:N169J:1200:3:43.12345:-78.543:12000:120:3487239347:60
	
		ident = re.match(self.FSDPilotPosition+'([A-Z])',words[0]) #Get Ident
		
		client.SetIdent(ident.group(1))
		client.SetTransponder(words[2])	
		client.SetRating(words[3])
		client.SetLatitude(words[4])
		client.SetLongitude(words[5])
		client.SetTrueAlt(words[6])
		client.SetSpeed(words[7])
		client.SetPitchBankHeading(words[8])
		client.SetGround(words[9])
		
		return client
		
	def InfoRequest(self,words,client):
		#$CQAAAA:BBBB:P2P:2:PPOS1:127.113.78.203:17504:192.168.0.7:17504
		print("InforRequest ",words)
		client.SetP2PpublicIP(words[5])
		client.SetP2PpublicPort(words[6])
		client.SetP2PprivateIP(words[7])
		client.SetP2PprivatePort(words[8])
		
		return client
		
		

		
		