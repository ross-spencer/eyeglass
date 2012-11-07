import eyeglass
eg = eyeglass.EyePrescription()
sample = open('sample.eygl', 'wb')
eg.__save__(sample)
sample.close()