import socket,sys,logging

#Creates the socket with the variable sock
sock = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)

#Define the server address and port
serverAddress = ("129.21.84.234", 10001)
#bind associates the socket with an ip and prints out a statement
print(sys.stderr, "Starting up on %s port %s" % serverAddress)
sock.bind(serverAddress)

#Listen for incoming connections & puts into server mode
sock.listen(1)

# filename = open(input("Enter a filename: "),"w")


while True:
    # Wait for a connection
    print('Waiting for a connection...')
    #accept returns the open connection along with the ip address of the client
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)
        # Receive the data in small chunks and send it back to client
        while True:
            filename = open("log.txt",'a')
            data = connection.recv(16)
            data_decode = data.decode()
            print(f'received "{data_decode}"')
            if data_decode == 'over and out':
                connection.close()
            elif data:
                print('Sending data back to the client')
                connection.sendall(data)
            else:
                print('No more data from', client_address)
                break
            print(data_decode)
            filename.write(data_decode+"\n")
            filename.close()
            
            
    finally:
        # Clean up the connection and close it
        connection.close()

