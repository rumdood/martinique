import json
from azure_service_bus_listener import azure_service_bus_listener
from mock_rgb_strip import mock_rgb_strip
from color_fade_engine import color_fade_engine
from color_fade_manager import color_fade_manager
from color_sequence import color_sequence
from rgb_light_color import rgb_light_color

class martinique_poc(object):

    @staticmethod
    def timeout_expired(listener):
        print("Queue Read Timeout")
        listener.wait_for_message(
            martinique_poc.on_message_receive, 
            martinique_poc.timeout_expired)
    
    @staticmethod    
    def on_message_receive(listener, message):
        
        if (message == 'SHUTDOWN'):
            print("Got Shutdown Request. Goodbye, cruel world.")
            return
            
        if (message != 'STOP'):
            sequence_json = json.loads(message)
            target_sequence = color_sequence.load_from_json(sequence_json)
            print("Got Request to run sequence: %s" % target_sequence.name)
        
        listener.wait_for_message(
            martinique_poc.on_message_receive, 
            martinique_poc.timeout_expired)
	
    @staticmethod
    def run():
        with open('gpio_settings.json') as gpio_settings:
            gpio = json.load(gpio_settings)
			
        #with open('seafoam_sequence.json') as seafoam_file:
        #    seafoam = json.load(seafoam_file)
            
        with open('azure_settings.json') as azure_settings_file:
            azure_settings = json.load(azure_settings_file)
			
        #default_sequence = color_sequence.load_from_json(seafoam)
        
        bus_listener = azure_service_bus_listener(azure_settings['service_bus'])
        #bus_listener.create_queue()
        bus_listener.wait_for_message(martinique_poc.on_message_receive, 
            martinique_poc.timeout_expired)
        
		
		#with rgb_strip(gpio['led_pins'], gpio['led_frequency']) as strip:
		#	engine = color_fade_engine(strip)
		#	mgr = color_fade_manager(engine)
		#	mgr.run_sequence(seq, 
		#		2, 
		#		0.1, 
		#		5)
		
		
        print('FDF')