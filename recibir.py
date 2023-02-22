import socket

server_address = ('192.168.1.6', 5555)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print("Conexión establecida")

while True:
    message = input("Mensaje: ")
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Recibido: {response}")
    
client_socket.close()
