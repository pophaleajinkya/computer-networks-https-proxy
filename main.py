import socket
import requests
# Set up a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Prevent "Address already in use" errors after a previous run of the server
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set the IP address and port number for the server to listen on
server_address = ('localhost', 8080)
print('Starting up server on %s port %s' % server_address)

# Bind the socket to the server address and port number
server_socket.bind(server_address)

# Listen for incoming connections (1 is the maximum number of queued connections)
server_socket.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection_socket, client_address = server_socket.accept()

    try:
        print('Connection from', client_address)

        # Receive data from the client
        data = connection_socket.recv(1024).decode()
        print('Received "%s"' % data)
        url = requests.get(data)
        connection_socket.sendall(bytes(str
                                            (
                                                {'status_code': (url.status_code),
                                                 'response_headers': (url.headers),
                                                 'response_content': str(url.text)}
                                             ).encode('utf-8')
                                        )
                                  )
    finally:
        # Clean up the connection
        connection_socket.close()