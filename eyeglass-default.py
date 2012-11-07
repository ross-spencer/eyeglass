#script to create a sample eyeglass .eygl file using eygl defaults
import eyeglass
eg = eyeglass.Eyeglass()
sample = open('sample.eygl', 'wb')
eg.__save__(sample)
sample.close()