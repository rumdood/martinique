import json
from asb_manager import asb_manager
from rgb_strip import rgb_strip
from color_fade_engine import color_fade_engine
from color_sequence_manager import color_sequence_manager
from color_sequence import color_sequence
from rgb_light_color import rgb_light_color
from multiprocessing import Process, Queue, JoinableQueue

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
    rgb_strip = rgb_strip(gpio['led_pins'], gpio['led_frequency'])
    engine = color_fade_engine(rgb_strip)
    
    color_mgr = color_sequence_manager(sequence_queue, engine)
    
    #firstRequest = color_sequence_request("START", sequence)
    color_mgr.start()
    
    asbmgr = asb_manager(sequence_queue)
    asbmgr.start()
    
    print("[Martinique]: Running...")