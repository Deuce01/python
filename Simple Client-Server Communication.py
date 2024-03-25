import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server listening on port 12345")

client_socket, addr = server_socket.accept()
print("Connection from:", addr)

data = client_socket.recv(1024)
print("Received:", data.decode())

client_socket.sendall("Message received".encode())

client_socket.close()
server_socket.close()
