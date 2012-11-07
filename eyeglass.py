#useful reference: http://www.dwp.gov.uk/publications/specialist-guides/medical-conditions/a-z-of-medical-conditions/vision/visual-acuity-vision.shtml
#wikipedia-acuity: http://en.wikipedia.org/wiki/Visual_acuity
#wikipedia-eyeglass: http://en.wikipedia.org/wiki/Eyeglass_prescription
#recommended extension: eygl

import datetime
import struct
class Eyeglass:

	ISODATETIMELEN = 19  #LENGTH OF DATETIME STRING

	def __init__(self):
	
		self.__eofbof__()
		self.__date__()
		
		#right: oculus dexter (OD)
		#left:  oculus sinister (OS)
		#both:  oculus uterque (OU)
		
		self.sphere = {'right': 0, 'left': 0}		# amount or short/long sightedness plus/minus: float
		self.cylinder = {'right': 0, 'left': 0} 	# Amount of astigmatism #float
		self.axis = {'right': 0, 'left': 0}		# Orientation of cylinder #integer
		self.prism = {'right': 0, 'left': 0}		# Correction required to help muscles of eyes coordinate (usually blank: float?)
		self.base = {'right': 0, 'left': 0}		# Direction in which prism is placed (usually blank: float?)
		
		self.distance_acuity = {'right': 0, 'left': 0}	#6 divided by...60 36 24 18 12 9 6 5
		self.near_acuity = {'right': 0, 'left': 0}	#N...24 18 14 12 10 8 6 5	#integer
		
		self.purpose = ''		#purpose of glasses #140 characters
		self.observations = ''		#optician's observations #255 characters
		self.next = 0			#next recommended checkup: Unit: years #float
		
	def __eofbof__(self):
		self.magic = '\xBB\x0D\x0A\x65\x79\x65\x67\x6C\x61\x73\x73\x1A\x0A\xAB'		#00 01 0D 0A eyeglass 1A 0A
		self.expansion = ''  
		self.eof = '\xBB\x65\x6f\x66'	#EOF
		self.version = 1
		
	def __date__(self):
		datetime.time(microsecond = 0)
		d = datetime.datetime.now()
		self.datetime = d.isoformat('T')[:self.ISODATETIMELEN]		#2012-11-07T00:44:41(minus ms - .000000)
	
	def __endian__(self, bigendian):
		self.bigendian = bigendian
		if bigendian is not True:
			self.float = '<f'
			self.bool = '<?'
			self.byte = '<B'
			self.int =  '<i'
		else:
			self.float = '>f'
			self.bool = '>?'
			self.byte = '>B'
			self.int =  '>i'
	
	def __save__(self, filename, bigendian=True):
		self.__endian__(bigendian)

		file = open(filename + '.eygl', 'wb')

		file.write(struct.pack('14s', self.magic))
		file.write(struct.pack(self.byte, self.version))	#unsigned char
		file.write(struct.pack(self.bool, self.bigendian))	#bool
		file.write(self.datetime)
		
		#padding
		file.write(struct.pack('>88s', self.expansion))
		
		#sphere
		file.write(struct.pack(self.float, self.sphere['right']))
		file.write(struct.pack(self.float, self.sphere['left']))
		
		#cylinder
		file.write(struct.pack(self.float, self.cylinder['right']))
		file.write(struct.pack(self.float, self.cylinder['left']))
		
		#axis
		file.write(struct.pack(self.int, self.axis['right']))
		file.write(struct.pack(self.int, self.axis['left']))
		
		#prism
		file.write(struct.pack(self.float, self.prism['right']))
		file.write(struct.pack(self.float, self.prism['left']))
		
		#base
		file.write(struct.pack(self.float, self.base['right']))
		file.write(struct.pack(self.float, self.base['left']))

		#distance acuity
		file.write(struct.pack(self.float, self.distance_acuity['right']))
		file.write(struct.pack(self.float, self.distance_acuity['left']))
		
		#near acuity
		file.write(struct.pack(self.int, self.near_acuity['right']))
		file.write(struct.pack(self.int, self.near_acuity['left']))

		#addendum
		file.write(struct.pack('140s', self.purpose)) 				#140characters
		file.write(struct.pack('255s', self.observations))			#255characters
		file.write(struct.pack(self.float, self.next))

		#eof
		file.write(struct.pack('4s', self.eof))

		#close
		file.close()

	### Getters and setters below here ###

	#setters
	def setsphere(self, right, left):
		self.sphere['right'] = right
		self.sphere['left'] = left
	
	def setcylinder(self, right, left):
		self.cylinder['right'] = right
		self.cylinder['left'] = left 
	
	def setaxis(self, right, left):
		self.axis['right'] = right
		self.axis['left'] = left 
	
	def setprism(self, right, left): 
		self.prism['right'] = right
		self.prism['left'] = left 
	
	def setbase(self, right, left): 
		self.base['right'] = right
		self.base['left'] = left 
		
	def setdistance_acuity(self, right, left): 
		self.distance_acuity['right'] = right
		self.distance_acuity['left'] = left 
	
	def setnear_acuity(self, right, left):
		self.near_acuity['right'] = right
		self.near_acuity['left'] = left 
		
	def setpurpose(self, purpose): 
		self.purpose = purpose
	
	def setobservations(self, observations): 
		self.observations = observations
	
	def setnext(self, next):
		self.next = next
		
	#getters
	def getsphere(self):
		return self.sphere
		
	def getcylinder(self):
		return self.cylinder
		
	def getaxis(self):
		return self.axis
		
	def getprism(self):
		return self.prism
		
	def getbase(self):
		return self.base
		
	def getdistance_acuity(self):
		return self.distance_acuity
		
	def getnear_acuity(self):
		return self.near_acuity
		
	def getpurpose(self):
		return self.purpose
		
	def getobservations(self): 
		return self.observations
		
	def getnext(self):
		return self.next