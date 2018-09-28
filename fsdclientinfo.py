class fsdclientinfo:
		
	def __init__(	self,
					callsign 		="",
					connection		="",
				
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
		self.__connection		=	connection
		
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
		
	def SetConnection(self,connection):
		self.__connection = connection
			
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
	
	def GetConnection(self):
		return self.__connection

	
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
	
	#def Remove(self,callsign):
	#	self.__callsign = ""
