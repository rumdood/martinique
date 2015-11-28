class rgb_light_color(object):
	
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue
	
	def __eq__(self, other): 
        	return (self.red == other.red
				and self.green == other.green
				and self.blue == other.blue)
