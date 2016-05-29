import time
from multiprocessing import Process, Queue, JoinableQueue
from queue import Empty
from rgb_light_color import rgb_light_color
from color_sequence_request import color_sequence_request

class color_sequence_manager(Process):
    
    def __init__(self, sequence_queue, fade_engine):
        Process.__init__(self)
        self.__sequence_queue = sequence_queue
        self.__engine = fade_engine
        self.__current_sequence = None
        self.__black = rgb_light_color(0,0,0)
        
    def check_queue(self):
        if (not self.__sequence_queue.empty()):
            try:
                request = self.__sequence_queue.get_nowait()
                return request
            except Empty:
                return None
        
        return None
        
    def run(self):
        proc_name = self.name
        while (True):
            request = self.check_queue()   
            if (request is None):
                if (self.__current_sequence is None):
                    # there is nothing to do but sit and wait
                    continue
                else:
                    # no new requests, but we have work to do on the current sequence
                    time.sleep(self.__current_sequence.color_cycle_delay)
                    nextColor = self.__current_sequence.get_next_color()
                    self.__engine.fade_to_color(nextColor, self.__current_sequence.color_fade_delay)
            else: # there is a new request!
                if (request.sequence is None):
                    # poison pill to end current sequence without starting a new one
                    self.__engine.fade_to_color(self.__black, 0.1)
                    self.__current_sequence = None
                    self.__sequence_queue.task_done()
                    
                    if (request.message is None):
                        return
                else:
                    # A new sequence has been requested, start it up
                    self.__current_sequence = request.sequence
                    nextColor = self.__current_sequence.get_next_color()
                    self.__engine.fade_to_color(nextColor, self.__current_sequence.color_fade_delay)
                    
                    if (len(self.__current_sequence.colors) == 1):
                        self.__current_sequence = None # there's only one color - nothing to process after this
                        
                    self.__sequence_queue.task_done()
        return