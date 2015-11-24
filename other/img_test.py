import logging
logging.basicConfig(level=logging.WARNING)
class Student(object):
	def __init__(self, name):
		self.__name = name
		
	def print_name(self):
		print self.__name
	
bart = Student('bart')

print bart._Student__name

s = '0'
n = int(s)
logging.info('n=%d' % n )
print 10/n

