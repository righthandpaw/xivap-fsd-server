class fsdregistry:

	def __init__(self):
		self.__Registry = {}
		self.__MessageQue = {}
		
	def UpdateRegistry(self,client,param='defualt'):
		
		self.__myID = client.GetUserName()
		
		if param == 'defualt':
			self.__Registry[self.__myID]={
				"remoteaddress":client.GetRemoteAddress(),
				"remoteport":client.GetRemotePort(),	
				"username":client.GetUserName(),
				"fullname":client.GetFullName(),
				"callsign":client.GetCallSign(),
				"password":client.GetPassword(),
				"airplane":client.GetAirPlane(),
				"ident":client.GetIdent(),
				"transponder":client.GetTransponder(),
				"rating":client.GetRating(),
				"latitude":client.GetLatitude(),
				"longitude":client.GetLongitude(),
				"truealt":client.GetTrueAlt(),
				"speed":client.GetSpeed(),
				"pitchbankheading":client.GetPitchBankHeading(),
				"ground":client.GetGround(),
				}

		if param == 'deletePilot':
			self.__Registry.pop(self.__myID,None)

	def AddMessage(self,callsign,message):
		return message
		
	def GetRegistry(self):
		return self.__Registry		
	def GetRegistryKeys(self):
		return self.__Registry.keys()
		
		
		
	#User/Pilot information
	def GetMyID(self):
		return self.__myID
	def GetCallSign(self,userID):
		return self.__Registry[userID]["callsign"]
	def GetRating(self,userID):
		return self.__Registry[userID]["rating"]
	
	
	#Aircraft information
	def GetAirPlane(self,userID):
		return self.__Registry[userID]["airplane"]

	
	#Aircraft Transponder information
	def GetIdent(self,userID):
		return self.__Registry[userID]["ident"]
	def GetTransponder(self,userID):
		return self.__Registry[userID]["transponder"]

	
	#Aircraft positional information
	def GetLatitude(self,userID):
		return self.__Registry[userID]["latitude"]
	def GetLongitude(self,userID):
		return self.__Registry[userID]["longitude"]
	def GetTrueAlt(self,userID):
		return self.__Registry[userID]["truealt"]
	def GetSpeed(self,userID):
		return self.__Registry[userID]["speed"]
	def GetPitchBankHeading(self,userID):
		return self.__Registry[userID]["pitchbankheading"]	
	def GetGround(self,userID):
		return self.__Registry[userID]["ground"]
		
		
		
	#Network information information	
	def GetRemoteAddress(self,userID):
		return self.__Registry[userID]["remoteaddress"]
	def GetRemotePort(self,userID):
		return self.__Registry[userID]["remoteport"]


			
	