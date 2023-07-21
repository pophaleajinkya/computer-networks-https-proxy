import socket
import sys
import requests

# Set up a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port number for the server to connect to
server_address = ('localhost', 8080)
print('Connecting to %s port %s' % server_address)
http = str(sys.argv[1])
# http="http://engineering.case.edu/eecs/about"
# Connect the socket to the server address and port number
client_socket.connect(server_address)


try:
    # Send data to the server
    message = http.encode()
    print('Sending "%s"' % message)
    client_socket.sendall(message)

    # Receive data from the server
    msg = client_socket.recv(204800).decode()
    res = eval(msg)
    print(res.keys())
    print('Response Status Code:', res['status_code'])
    print('Response Headers:', res['response_headers'])
    with open('proxy_content.txt', 'w') as file:
        file.writelines(str(res['response_content']))
        file.close()
finally:
    # Clean up the connection
    client_socket.close()
