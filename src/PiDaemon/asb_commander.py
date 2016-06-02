import argparse
import json
from ComplexJSONEncoder import ComplexJSONEncoder
from azure.servicebus import ServiceBusService, Message, Queue
from color_sequence import color_sequence

def get_settings():		
    with open('local_settings.json') as local_settings_file:
        settings = json.load(local_settings_file)
    
    return settings

def get_default_sequence(settings):
    with open(settings["default-sequence-file"]) as sequence_file:
        sequence_data = json.load(sequence_file)
        
    seq = color_sequence.load_from_json(sequence_data)
    return seq
    
def get_azure_settings():
    with open('azure_settings.json') as azure_settings_file:
        azure_settings = json.load(azure_settings_file)
        
    return azure_settings['service_bus']
    
def get_sequence(sequence_file_name):   
    with open(sequence_file_name) as sequence_file:
        sequence_data = json.load(sequence_file)
        
    seq = color_sequence.load_from_json(sequence_data)
    return seq
    
parser = argparse.ArgumentParser(description="Start/Stop/Shutdown Martinique via ASB")
parser.add_argument("-stop", action="store_true", help="Stops the current sequence")
parser.add_argument("-start", action="store_true", help="Starts the specified sequence")
parser.add_argument("-shutdown", action="store_true", help="Shuts down running Martinique process")
parser.add_argument("sequence", nargs="?", default=None, help="The sequence json file you want to run")

args = parser.parse_args()

azure_settings = get_azure_settings()
bus_service = ServiceBusService(
    service_namespace= azure_settings['name_space'],
    shared_access_key_name = azure_settings['key_name'],
    shared_access_key_value = azure_settings['key_value'])

queue_name = azure_settings['queue_name']

#seq = get_default_sequence(get_settings())

if (args.start):
    if (args.sequence != None):
        sequence_data = get_sequence(args.sequence)
        print("Requesting Sequence: %s" % sequence_data.name)
        msgData = json.dumps(sequence_data, cls=ComplexJSONEncoder)
    else:
        print("No sequence specified. Please specify a sequence to start.")
        return
elif (args.stop):
    print("Requesting sequence stop")
    msgData = "STOP"
elif (args.shutdown):
    print("Requesting shutdown")
    msgData = "SHUTDOWN"
    
qMessage = Message(str.encode(msgData))
bus_service.send_queue_message(queue_name, qMessage)