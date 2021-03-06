import time

class mock_rgb_strip(object):
	
	def __init__(self, pins, frequency):
		self.__pins = dict()
		
		self.__pins['RED'] = -1
		self.__pins['GREEN'] = -1
		self.__pins['BLUE'] = -1
		
	def __enter__(self):
		return self
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.cleanup()
		return True
	
	def set_color(self, red, green, blue):
		self.__pins['RED'] = red
		self.__pins['GREEN'] = green
		self.__pins['BLUE'] = blue
		print('[MOCK_RGB]: R: %s G: %s B: %s' % (red, green, blue))
		
	def cleanup(self):
		self.__pins['RED'] = -1
		self.__pins['GREEN'] = -1
		self.__pins['BLUE'] = -1
		print('[MOCK_RGB]: Cleanup Called')
	
	def get_pins(self):
		return self.__pins