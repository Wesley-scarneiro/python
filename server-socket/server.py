'''
    Servidor de socket simples que utiliza TCP.
    Recebe um texto e o converte todo para maiúsculo para o cliente.
    saída do servidor:
        Server is on, waiting for connections...
        Client '127.0.0.1' connected
        Server is off.
    saída do client:
        Connected to the server {127.0.0.1}
        Enter text: wesley silva carneiro
        Response servidor: WESLEY SILVA CARNEIRO
'''

import socket

# HOST e porta do servidor
HOST = '127.0.0.1'
PORT = 10000

# Cria um socket utilizando IpV4 (cama de rede) e TCP (camada de transporte)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server is on, waiting for connections...")
    client = server.accept()
    print(f"Client '{client[1][0]}' connected")
    while True:
        text = client[0].recv(1024)
        if not text:
            break
        text = text.upper()
        client[0].sendall(text)
print("Server is off.")