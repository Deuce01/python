import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto("Hello, UDP Server!".encode(), ('localhost', 12345))

data, addr = client_socket.recvfrom(1024)
print("Received from server:", data.decode())

client_socket.close()
