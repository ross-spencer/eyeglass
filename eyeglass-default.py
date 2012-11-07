#script to create a sample eyeglass .eygl file using eygl defaults
import eyeglass
eg = eyeglass.EyePrescription()
sample = open('sample.eygl', 'wb')
eg.__save__(sample)
sample.close()