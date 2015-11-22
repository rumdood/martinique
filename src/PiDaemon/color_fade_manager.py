import time

class color_fade_manager(object):
	
	def __init__(self, fade_engine):
		self.__engine = fade_engine
		
	def run_sequence(self, 
		sequence, 
		max_loops=0, 
		fade_delay=0.1, 
		color_pause=0,
		state_dict=None):
		
		if (state_dict == None):
			state_dict = dict()
			state_dict["READY"] = True
			state_dict["RUNNING"] = False
			
		while (not state_dict["READY"]):
			print("-> Waiting for system to be ready for sequence")
			time.sleep(1)
		
		loop_count = 0
		
		while(state_dict["READY"] and
			(max_loops == 0 or loop_count < max_loops)):
			
			state_dict["RUNNING"] = True
			
			target_color = sequence.get_next_color()
			self.__engine.fade_to_color(target_color, fade_delay)
			time.sleep(color_pause)
			
			if (max_loops > 0):
				loop_count = loop_count + 1
				
		state_dict["RUNNING"] = False
		state_dict["READY"] = True		