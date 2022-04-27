from http import client
from logging.config import listen
import socket

from requests import request

ip = ''
porta = 8000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((ip, porta))
listen_socket.listen(1)

print('servidor http esta rodando em %s' % porta)

while True:
    client_connection, client_adress - listen_socket.accept()
    request - client_connection.recv(1024)
    print (request.decode('utf-8'))
    http_response = """"
HTTP/1.1 200 OK

Hello, World!
"""

    client_connection.send(http_response.encode('utf-8'))
    client_connection.close()

listen_socket.close()    