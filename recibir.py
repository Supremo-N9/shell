import socket

server_ip = '192.168.1.68'
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

print("Conexión establecida")
print(client_socket.recv(1024).decode())

client_socket.close()
