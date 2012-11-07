#useful reference: http://www.dwp.gov.uk/publications/specialist-guides/medical-conditions/a-z-of-medical-conditions/vision/visual-acuity-vision.shtml
#wikipedia-acuity: http://en.wikipedia.org/wiki/Visual_acuity
#wikipedia-eyeglass: http://en.wikipedia.org/wiki/Eyeglass_prescription
#recommended extension: eygl

import datetime
import struct
class EyePrescription:

	ISODATETIMELEN = 19  #LENGTH OF DATETIME STRING

	def __init__(self):
	
		self.__eofbof__()
		self.__date__()
		
		#right: oculus dexter {OD)
		#left:  oculus sinister (OS)
		#both:  oculus uterque (OU)
		
		self.sphere = {'right': 0, 'left': 0}		# amount or short/long sightedness plus/minus: float
		self.cylinder = {'right': 0, 'left': 0} 	# Amount of astigmatism #float
		self.axis = {'right': 0, 'left': 0}			# Orientation of cylinder #integer
		self.prism = {'right': 0, 'left': 0}		# Correction required to help muscles of eyes coordinate (usually blank: float?)
		self.base = {'right': 0, 'left': 0}			# Direction in which prism is placed (usually blank: float?)
		
		self.distance_acuity = {'right': 0, 'left': 0}	#6 divided by ...60 36 24 18 12 9 6 5
		self.near_acuity = {'right': 0, 'left': 0}		#N...24 18 14 12 10 8 6 5
		
		self.purpose = ''									#purpose of glasses #140 characters
		self.observations = ''							#optician's observations #255 characters
		self.next = 0										#next recommended checkup	#float
		
	def __eofbof__(self):
		self.magic = '\xBB\x0D\x0A\x65\x79\x65\x67\x6C\x61\x73\x73\x1A\x0A\xAB'			#00 01 0D 0A eyeglass 1A 0A
		self.padding = ''  
		self.eof = '\x00\x65\x6f\x66'	#EOF
		self.version = 1
		
	def __date__(self):
		datetime.time(microsecond = 0)
		d = datetime.datetime.now()
		self.datetime = d.isoformat('T')[:self.ISODATETIMELEN]		#2012-11-07T00:44:41(minus ms - .000000)
		
	def __save__(self, file):
		file.write(struct.pack('14s', self.magic))
		file.write(struct.pack('>H', self.version))	#unsigned short
		file.write(self.datetime)
		
		#padding
		file.write(struct.pack('>88s', self.padding))
		
		#right
		file.write(struct.pack('>f', self.sphere['right'])) 					#float
		file.write(struct.pack('>f', self.cylinder['right'])) 				#float
		file.write(struct.pack('>i', self.axis['right'])) 						#int
		file.write(struct.pack('>f', self.prism['right'])) 					#float
		file.write(struct.pack('>f', self.base['right'])) 						#float
		
		file.write(struct.pack('>f', self.distance_acuity['right'])) 		#float
		file.write(struct.pack('>f', self.near_acuity['right'])) 			#float

		#left
		file.write(struct.pack('>f', self.sphere['left'])) 					#float
		file.write(struct.pack('>f', self.cylinder['left'])) 					#float
		file.write(struct.pack('>i', self.axis['left'])) 						#int
		file.write(struct.pack('>f', self.prism['left'])) 						#float
		file.write(struct.pack('>f', self.base['left'])) 						#float
		
		file.write(struct.pack('>f', self.distance_acuity['left'])) 		#float
		file.write(struct.pack('>f', self.near_acuity['left'])) 				#float

		#addendum
		file.write(struct.pack('140s', self.purpose)) 				#140characters
		file.write(struct.pack('255s', self.observations))			#255characters
		file.write(struct.pack('>f', self.next))

		#eof
		file.write(struct.pack('4s', self.eof))
