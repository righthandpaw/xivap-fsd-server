class fsdclientinfo:
		
	def __init__(	self,
					callsign 		= "",
					localaddress	="",
					localport		="",
					remoteaddress 	="",
					remoteport		="",
				
					p2pmethod		="",
					p2ppublicip		="",
					p2ppublicport	="",
					p2pprivateip	="",
					p2pprivateport	="",
					
					fullname		="",
					username		="",
					password		="",
					airplane		="A320",
					
					ident				="",
					transponder			="",
					rating				="",
					latitude 			="",
					longitude			="",
					truealt				="",
					speed				="",
					pitchbankheading	="",
					ground				="",
					
					verified=False):
		
		self.__callsign			=	callsign
		self.__localaddress		=	localaddress
		self.__localport		=	localport
		self.__remoteaddress	=	remoteaddress
		self.__remoteport		=	remoteport
		
		self.__p2pmethod		=	p2pmethod
		self.__p2ppublicip		=	p2ppublicip
		self.__p2ppublicport	=	p2ppublicport
		self.__p2pprivateip		=	p2pprivateip
		self.__p2pprivateport	=	p2pprivateport
		
		self.__fullname			=	fullname
		self.__username			=	username
		self.__password			=	password
		self.__airplane			=	airplane
		self.__ident			=	ident
		self.__transponder		=	transponder
		self.__rating			=	rating
		self.__latitude			=	latitude
		self.__longitude		=	longitude
		self.__truealt			=	truealt
		self.__speed			=	speed
		self.__pitchbankheading	=	pitchbankheading
		self.__ground			=	ground
		
		
		self.__verified		=	verified
		self.__error		=	{}

		
	#Sets	
	def SetCallSign(self,callsign):
		self.__callsign = callsign
		
	def SetLocalAddress(self,localaddress):
		self.__localaddress = localaddress
		
	def SetLocalPort(self,localport):
		self.__localport = localport
		
	def SetRemoteAddress(self,remoteaddress):
		self.__remoteaddress = remoteaddress
		
	def SetP2Pmethod(self,p2pmethod):
		self.__p2pmethod(p2pmethod)
				
	def SetP2PpublicIP(self,p2ppublicip):
		self.__p2ppublicip = p2ppublicip
	
	def SetP2PpublicPort(self,p2ppublicport):
		self.__p2ppublicport = p2ppublicport
	
	def SetP2PprivateIP(self,p2pprivateip):
		self.__p2pprivateip = p2pprivateip
		
	def SetP2PprivatePort(self,p2pprivateport):
		self.__p2pprivateport = p2pprivateport
		
	def SetRemotePort(self,remoteport):
		self.__remoteport = remoteport	
	
	def SetFullName(self,fullname):
		self.__fullname = fullname

	def SetUserName(self,username):
		self.__username = username

	def SetPassword(self,password):
		self.__password = password
			
	def SetAirPlane(self,airplane):
		self.__airplane = airplane

	def SetIdent(self,ident):
		self.__ident	= ident
		
	def SetTransponder(self,transponder):
		self.__transponder = transponder
		
	def SetRating(self,rating):
		self.__rating = rating
		
	def SetLatitude(self,latitude):
		self.__latitude = latitude
	
	def SetLongitude(self,longitude):
		self.__longitude = longitude
		
	def SetTrueAlt(self,truealt):
		self.__truealt = truealt
		
	def SetSpeed(self,speed):
		self.__speed = speed
		
	def SetPitchBankHeading(self,pitchbankheading):
		self.__pitchbankheading = pitchbankheading
		
	def SetGround(self,ground):
		self.__ground = ground
		
	def SetVerification(self,verified):
		self.__verified = verified
	
	def SetError(self,errorNumber,error):
		self.__error[errorNumber] = error
	

	#Gets
	def GetCallSign(self):
		return self.__callsign
	
	def GetLocalAddress(self):
		return self.__localaddress
		
	def GetLocalPort(self):
		return self.__localport
		
	def GetRemoteAddress(self):
		return self.__remoteaddress
		
	def GetRemotePort(self):
		return self.__remoteport
	
	def GetP2Pmethod(self)
		return self.__p2pmethod
	
	def GetP2PpublicIP(self):
		return self.__p2ppublicip
		
	def GetP2PpublicPort(self):
		return self.__p2ppublicport
		
	def GetP2PprivateIP(self):
		return self.__p2pprivateip
		
	def GetP2PprivatePort(self):
		return self.__p2pprivateport
	
	def GetFullName(self):
		return self.__fullname
	
	def GetUserName(self):
		return self.__username
		
	def GetPassword(self):
		return self.__password
	
	def GetAirPlane(self):
		return self.__airplane	
		
	def GetIdent(self):
		return self.__ident
		
	def GetTransponder(self):
		return self.__transponder
		
	def GetRating(self):
		return self.__rating
		
	def GetLatitude(self):
		return self.__latitude
	
	def GetLongitude(self):
		return self.__longitude
		
	def GetTrueAlt(self):
		return self.__truealt
		
	def GetSpeed(self):
		return self.__speed
		
	def GetPitchBankHeading(self):
		return self.__pitchbankheading
		
	def GetGround(self):
		return self.__ground	
		
	def GetVerification(self):
		return self.__verified
		
	def GetError(self):
		return self.__error
	
	