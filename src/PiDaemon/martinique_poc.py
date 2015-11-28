import json
from rgb_strip import rgb_strip
from color_fade_engine import color_fade_engine
from color_fade_manager import color_fade_manager
from color_sequence import color_sequence
from rgb_light_color import rgb_light_color

class martinique_poc(object):
	
	@staticmethod
	def run():
		with open('gpio_settings.json') as gpio_settings:
			gpio = json.load(gpio_settings)
			
		with open('seafoam_sequence.json') as seafoam_file:
			seafoam = json.load(seafoam_file)
			
		seq = color_sequence.load_from_json(seafoam)
		
		with rgb_strip(gpio['led_pins'], gpio['led_frequency']) as strip:
			print("I'm going to create and run a sequence now")
			engine = color_fade_engine(strip)
			mgr = color_fade_manager(engine)
			mgr.run_sequence(sequence=seq, 
				max_loops=2, 
				fade_delay=seq.color_fade_delay, 
				color_pause=seq.color_cycle_delay,
				state_dict=mDict)
		
		
		print('FDF')