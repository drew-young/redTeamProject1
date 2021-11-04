import socket

#create the socket again
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create variable for server address
serverAddress = ("129.21.84.234", 10001)
#connect to server and print that you are connecting
print('connecting to %s port %s' % serverAddress)
sock.connect(serverAddress)

#turn string into bytes by encoding or else it will pop an error saying it expected bytes
newstr = input("String to send: ")
while newstr != "":
    newstr_bytes = newstr.encode()
    print(newstr_bytes)
    try:
        
        #Send data with (sendall)
        message = newstr_bytes
        print('sending "%s"' % message)
        sock.sendall(message)

        #Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f'received {newstr_bytes.decode()}')

    finally:
        newstr = input("String to send: ")
print ('closing socket')
sock.close()