import socket, threading

PORT = 5050
SERVER = socket.gethostbyname (socket.gethostname ())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
server.bind (ADDR)

def clientHandling (connection, address):
    print (f'[NEW CONNECTION] {address} connected')
    isConnected = True
    while isConnected:
        messageLength = connection.recv (HEADER).decode (FORMAT)
        if messageLength:
            messageLength = int (messageLength)
            message = connection.recv (messageLength).decode (FORMAT)
            if message == DISCONNECT_MESSAGE:
                isConnected = False
            print (f'[{address}] {message}')
            connection.send ('Message Recieved'.encode (FORMAT))
    connection.close ()

def start ():
    server.listen ()
    print (f'[LISTENING] Server is listening on {SERVER}')
    while True:
        connection, address = server.accept ()
        thread = threading.Thread (target=clientHandling, args=(connection, address))
        thread.start ()
        print (f'[ACTIVE CONNECTION] {threading.active_count () - 1}')

print ('[SERVER STARTING] server has been started')
start ()