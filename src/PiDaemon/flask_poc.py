from flask import Flask
from multiprocessing import Process, Manager
import json
import time
from mock_rgb_strip import mock_rgb_strip
from color_fade_engine import color_fade_engine
from color_fade_manager import color_fade_manager
from color_sequence import color_sequence
from rgb_light_color import rgb_light_color

app = Flask(__name__)
_process = None
_processManager = None
_mDictionary = []

def run_loop(mDict):
	with open('gpio_settings.json') as gpio_settings:
		gpio = json.load(gpio_settings)
		
	with open('local_settings.json') as local_settings_file:
		settings = json.load(local_settings_file)
			
	with open(settings["default-sequence-file"]) as sequence_file:
		sequence_data = json.load(sequence_file)
			
	seq = color_sequence.load_from_json(sequence_data)
		
	with mock_rgb_strip(gpio['led_pins'], gpio['led_frequency']) as strip:
		
		engine = color_fade_engine(strip)
		mgr = color_fade_manager(engine)
		mgr.run_sequence(seq, 
			0, 
			seq.color_fade_delay, 
			seq.color_cycle_delay,
			mDict)
		
def spawn_process_loop():
	if (__name__ == '__main__'):
		
		if (len(_mDictionary) == 0):
			_mDictionary["READY"] = True
			_mDictionary["RUNNING"] = False
		else:
			stop_process_loop()
		
		while (_mDictionary["RUNNING"]):
			print("-> Waiting for previous sequence to end")
			time.sleep(1)
		
		_mDictionary["READY"] = True
		_process = Process(target=run_loop, args=(_mDictionary,))
		_process.start()
		
	return 'Sequence Started'
	
def stop_process_loop():
	if (__name__ == '__main__'):
		_mDictionary["READY"] = False
	
	return 'Sequence Stopped'
	
@app.route("/run")
def do_run():
	return spawn_process_loop()
	
@app.route("/stop")
def do_stop():
	return stop_process_loop()
	
if (__name__ == '__main__'):
	_processManager = Manager()
	_mDictionary = _processManager.dict()
	app.run()