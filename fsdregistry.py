class fsdregistry:

	def __init__(self):
		self.__Registry = {}
		
	def UpdateRegistry(self,client):
		
		self.__myID = client.GetUserName()
		
		self.__Registry[self.__myID]={
			"connection":client.GetConnection(),	
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
			"rank":client.GetRank(),
			"fsdver":client.GetFsdVer(),
			"simver":client.GetSimVer(),
			}

	def DeleteKey(self,userID):
		print(userID)
		self.__Registry.pop(userID,None)

	def GetRegistry(self):
		return self.__Registry		
	def GetRegistryKeys(self):
		#return self.__Registry.keys()
		return self.__Registry.copy()
		

	#User/Pilot information
	def GetMyID(self):
		return self.__myID
	def GetCallSign(self,userID):
		return self.__Registry[userID]["callsign"]


	def GetRank(self,userID):
		return self.__Registry[userID]["rank"]

	def GetFsdVer(self,userID):
		return self.__Registry[userID]["fsdver"]

	def GetSimVer(self,userID):
		return self.__Registry[userID]["simver"]

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
	def GetConnection(self,userID):
		return self.__Registry[userID]["connection"]
	


			
	