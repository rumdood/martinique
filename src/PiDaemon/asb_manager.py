import json
from multiprocessing import Process, Queue, JoinableQueue
from azure_service_bus_listener import azure_service_bus_listener
from color_sequence_request import color_sequence_request
from color_sequence import color_sequence

class asb_manager(Process):

    def __init__(self, request_queue):
        Process.__init__(self)
        self.__bus_listener = None
        self.__request_queue = request_queue
        self.__firstRun = True

    #@staticmethod
    def timeout_expired(self):
        print("[ASB_MGR]: Queue Read Timeout")
        
        self.__bus_listener.wait_for_message(
            self.on_message_receive, 
            self.timeout_expired)
    
    #@staticmethod    
    def on_message_receive(self, message):
    
        sequence_request = None
        
        if (message == 'SHUTDOWN'):
            print("[ASB_MGR]: Got Shutdown Request. Goodbye, cruel world.")
            poison_request = color_sequence_request(None, None)
            self.__request_queue.put(poison_request)
            self.__request_queue.join()
            return
            
        if (message != 'STOP'):
            sequence_json = json.loads(message)
            target_sequence = color_sequence.load_from_json(sequence_json)
            print("[ASB_MGR]: Got Request to run sequence: %s" % target_sequence.name)
            sequence_request = color_sequence_request("START", target_sequence)
        else:
            print("[ASB_MGR]: Got a stop request")
            sequence_request = color_sequence_request("STOP", None)
            
        if (sequence_request != None):
            self.__request_queue.put(sequence_request)
            self.__request_queue.join()
        
        self.__bus_listener.wait_for_message(
            self.on_message_receive, 
            self.timeout_expired)
            
    def run(self):      
        with open('azure_settings.json') as azure_settings_file:
            azure_settings = json.load(azure_settings_file)
        
        print("[ASB_MGR]: Begin Wait For Message")
        self.__bus_listener = azure_service_bus_listener(azure_settings['service_bus'])
        
        try:
            self.__bus_listener.wait_for_message(self.on_message_receive, 
                self.timeout_expired)
        except KeyboardInterrupt:
            return