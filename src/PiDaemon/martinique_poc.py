import json
import time
from asb_manager import asb_manager
from mock_rgb_strip import mock_rgb_strip
from color_fade_engine import color_fade_engine
from color_fade_manager import color_fade_manager
from color_sequence_manager import color_sequence_manager
from color_sequence_request import color_sequence_request
from color_sequence import color_sequence
from rgb_light_color import rgb_light_color
from multiprocessing import Process, Queue, JoinableQueue

def get_default_sequence(settings):
    with open(settings["default-sequence-file"]) as sequence_file:
        sequence_data = json.load(sequence_file)
        
    seq = color_sequence.load_from_json(sequence_data)
    return seq
    
def get_gpio():
    with open('gpio_settings.json') as gpio_settings:
        gpio = json.load(gpio_settings)
        
    return gpio
    
def get_settings():		
    with open('local_settings.json') as local_settings_file:
        settings = json.load(local_settings_file)
    
    return settings
    
def main():
    # create the tasking queue
    sequence_queue = JoinableQueue()
    
    # get all the GPIO stuff done and create the engine
    gpio = get_gpio()
    settings = get_settings()
    sequence = get_default_sequence(settings)
    rgb_strip = mock_rgb_strip(gpio['led_pins'], gpio['led_frequency'])
    engine = color_fade_engine(rgb_strip)
    
    mgr = color_sequence_manager(sequence_queue, engine)
    
    #firstRequest = color_sequence_request("START", sequence)
    mgr.start()
    
    marti = asb_manager(sequence_queue)
    marti.start()
    
    print("[Martinique_POC]: Running...")
    
    #print(">>> sleeping 5 seconds before starting <<<")
    #time.sleep(2)
    #sequence_queue.put(firstRequest)   
    #sequence_queue.join()
    
    #time.sleep(5)
    #print(">>> Sending Poison Pill <<<")
    #poison_request = color_sequence_request(None, None)
    #sequence_queue.put(poison_request)
    #sequence_queue.join()

if (__name__ == '__main__'):
    try:
        main()
    except KeyboardInterrupt:
        print("[KEYBOARD INTERRUPT DETECTED]")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)