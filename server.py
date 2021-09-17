import socket
import sys

#Creates the socket with the variable sock
sock = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)

#Define the server address and port
serverAddress = ("129.21.87.219", 10001)
#bind associates the socket with an ip and prints out a statement
print(sys.stderr, "starting up on %s port %s" % serverAddress)
sock.bind(serverAddress)

#Listen for incoming connections & puts into server mode
sock.listen(1)




while True:
    # Wait for a connection
    print('waiting for a connection')
    #accept returns the open connection along with the ip address of the client
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and send it back to client
        while True:
            data = connection.recv(16)
            data_decode = data.decode()
            print(f'received "{data_decode}"')
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection and close it
        connection.close()

