import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

print("UDP Server listening on port 12345")

while True:
    data, addr = server_socket.recvfrom(1024)
    print("Received:", data.decode(), "from", addr)
    server_socket.sendto("Message received".encode(), addr)
