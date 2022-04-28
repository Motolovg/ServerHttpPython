import socket


ip = '127.0.0.1'
porta = 8000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((ip, porta))
server_socket.listen(1)

print('Servidor aberto na porta %s ...' % porta)

while True:    
    
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    print(request.split())
    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n <h1> Me arruma um trampo ai professor de verdade mesmo </h1>'
    client_connection.sendall(response.encode())
    client_connection.close()

server_socket.close()