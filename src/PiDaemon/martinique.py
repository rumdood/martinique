from flask import Flask
from multiprocessing import Process, Manager
import json
from rgb_strip import rgb_strip
from color_fade_engine import color_fade_engine
from color_fade_manager import color_fade_manager
from color_sequence import color_sequence
from rgb_light_color import rgb_light_color

app = Flask(__name__)
_process = None
_processManager = None
_stateDict = []

def run_loop(mDict):
	with open('gpio_settings.json') as gpio_settings:
		gpio = json.load(gpio_settings)
		
	with open('local_settings.json') as local_settings_file:
		settings = json.load(local_settings_file)
			
	with open(settings["default-sequence-file"]) as sequence_file:
		sequence_data = json.load(sequence_file)
			
	seq = color_sequence.load_from_json(sequence_data)
		
	with rgb_strip(gpio['led_pins'], gpio['led_frequency']) as strip:
		
		engine = color_fade_engine(strip)
		mgr = color_fade_manager(engine)
		mgr.run_sequence(sequence=seq, 
			max_loops=0, 
			fade_delay=seq.color_fade_delay, 
			color_pause=seq.color_cycle_delay,
			state_dict=mDict)
		
def spawn_process_loop():
	if (__name__ == '__main__'):
		
		if (len(_stateDict) == 0):
			_stateDict["READY"] = True
			_stateDict["RUNNING"] = False
		else:
			stop_process_loop()
		
		while (_stateDict["RUNNING"]):
			print("-> Waiting for previous sequence to end")
			time.sleep(1)
		
		_stateDict["READY"] = True
		_process = Process(target=run_loop, args=(_stateDict,))
		_process.start()
		
	return 'Sequence Started'
	
def stop_process_loop():
	if (__name__ == '__main__'):
		_stateDict["READY"] = False
	
	return 'Sequence Stopped'
	
@app.route("/run")
def do_run():
	return spawn_process_loop()
	
@app.route("/stop")
def do_stop():
	return stop_process_loop()
	
if (__name__ == '__main__'):
	
	with open('local_settings.json') as local_file:
		settings = json.load(local_file)
		
	_processManager = Manager()
	_stateDict = _processManager.dict()
	app.run(host="0.0.0.0",port=settings['http-port'])