import socket
import sys

#create the socket again
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create variable for server address
serverAddress = ("129.21.87.219", 10001)
#connect to server and print that you are connecting
print(sys.stderr, 'connecting to %s port %s' % serverAddress)
sock.connect(serverAddress)

#turn string into bytes by encoding or else it will pop an error saying it expected bytes
newstr = "This is the string but it will be repeated back to me"
newstr_bytes = newstr.encode("ascii")
print(newstr_bytes)


try:
    
    #Send data with (sendall)
    message = newstr_bytes
    print(sys.stderr, 'sending "%s"' % message)
    sock.sendall(message)

    #Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(sys.stderr, 'received "%s"' % data)

finally:
    print (sys.stderr, 'closing socket')
    sock.close()