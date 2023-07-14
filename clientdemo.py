import socket

HEADER = 64
PORT = 5050
FORMATE = 'utf-8'
DISCONNECT_MESSAGE = "Disconnected"
SERVER = "192.168.62.140"
ADDR = (SERVER, PORT)

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect()
