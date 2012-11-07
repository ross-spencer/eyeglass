#script to create three samply eygl files. 
#default using basic constructor values
#big-endian file using sample prescription
#little-endian file using same prescription

import eyeglass
eg = eyeglass.Eyeglass()

eg.__save__('default-sample-be')	#default constructor output

#prescription taken from here and augmented for creative purposes
#http://en.wikipedia.org/wiki/File:Specrx-prescription2.jpg
eg.setsphere(-3.35, +0.50)
eg.setcylinder(-0.25, -1.00)
eg.setaxis(130, 80)
eg.setprism(0, 0)
eg.setbase(0, 0)
eg.setdistance_acuity(0.66, 0.5)
eg.setnear_acuity(12, 12)
eg.setpurpose("Distance and Close Work.")
eg.setobservations("Patient's eyesight needs correction. History of diabetes in family but indicators found. Standard checkup interval recommended.")
eg.setnext(1)

eg.__save__('prescription-sample-be', True)	#big-endian
eg.__save__('prescription-sample-le', False)	#little-endian