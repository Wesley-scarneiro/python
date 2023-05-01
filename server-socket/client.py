'''
    Connected to the server {127.0.0.1}
    Enter text: wesley silva carneiro
    Response servidor: WESLEY SILVA CARNEIRO
'''

import socket

# HOST e porta do servidor
HOST = '127.0.0.1'
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print(f"Connected to the server {HOST}")
    while True:
        text = input("Enter text: ")
        client.sendall(text.encode('utf-8'))
        text = client.recv(1024)
        text = text.decode('utf-8')
        print(f"Response servidor: {text}")
        break