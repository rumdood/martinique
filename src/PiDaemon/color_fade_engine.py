import time
import json
from color_sequence import color_sequence
from rgb_light_color import rgb_light_color

class color_fade_engine(object):
	
	def __init__(self, strip):
		self.__rgb_strip = strip
		self.__current_color = rgb_light_color(0, 0, 0)
		
	def __enter__(self):
		return self
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.__rgb_strip.cleanup()
		self.__current_color = None
		return True
		
	def fade_to_color(self, target_color, step_delay):
		# don't let anyone set an out of bounds value
		if (target_color.red > 100):
			target_color.red = 100
		elif (target_color.red < 0):
			target_color.red = 0
			
		if (target_color.green > 100):
			target_color.green = 100
		elif (target_color.green < 0):
			target_color.green = 0;
		
		if (target_color.blue > 100):
			target_color.blue = 100
		elif (target_color.blue < 0):
			target_color.blue = 0
		
		if (self.__current_color == target_color):
			print('Target Color Reached')
			return;
		
		# I'm sure there's a better way to do this next bit...
		if (self.__current_color.red < target_color.red):
			self.__current_color.red = self.__current_color.red + 1
		elif (self.__current_color.red > target_color.red):
			self.__current_color.red = self.__current_color.red - 1
		if (self.__current_color.green < target_color.green):
			self.__current_color.green = self.__current_color.green + 1
		elif (self.__current_color.green > target_color.green):
			self.__current_color.green = self.__current_color.green - 1
		if (self.__current_color.blue < target_color.blue):
			self.__current_color.blue = self.__current_color.blue + 1
		elif (self.__current_color.blue > target_color.blue):
			self.__current_color.blue = self.__current_color.blue - 1
	
		self.__rgb_strip.set_color(self.__current_color.red, 
			self.__current_color.green, 
			self.__current_color.blue, step_delay)
			
		return self.fade_to_color(target_color,	step_delay)