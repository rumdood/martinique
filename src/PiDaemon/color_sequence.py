from rgb_light_color import rgb_light_color

class color_sequence:
	
	__current_color_index = -1
	
	def __init__(self, name=None, color_fade_delay=0, color_cycle_delay=0):
		
		if name is None:
			self.name = '_internal_'
		else:
			self.name = name
			
		self.color_fade_delay = color_fade_delay
		self.color_cycle_delay = color_cycle_delay
			
		self.colors = []
		
	def add_color(self, color):
		self.colors.append(color)
	
	@staticmethod	
	def load_from_json(json_object):
		if 'name' not in json_object:
			return None
			
		seq = color_sequence(json_object['name'],
			json_object['color_fade_delay'],
			json_object['color_cycle_delay'])
	
		jColors = json_object['colors']
		for color in jColors:
			seq.add_color(
				rgb_light_color(
					color['red'], 
					color['green'], 
					color['blue']))
		
		return seq
		
	def get_next_color(self):
		if (self.__current_color_index == len(self.colors) -1):
			self.__current_color_index = 0
		else:
			self.__current_color_index = self.__current_color_index + 1
			
		return self.colors[self.__current_color_index]