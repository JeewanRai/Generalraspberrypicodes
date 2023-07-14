# importing libraries
import socket
import threading #bacially means to run multiple independent programs simultaneously, not in sequence

HEADER = 64
PORT = 5050 #is like door for other computers to knock onto when required information
#SERVER = "192.168.62.140" #will host local server with ipV4 address of the local machine
SERVER = socket.gethostbyname(socket.gethostname()) #will get ipv4 address of the local machine automatically
#if we run server with ipv4 address then if we change local machine we heve to change the ip address every time when changes is done
print(SERVER) #prints out ip address of the local machine
print(socket.gethostname()) #prints out name of the computer

ADDR = (SERVER, PORT)
FORMATE = "utf-8"
DISCONNECT_MESSAGE = "Disconnected"

#creating new socket to open up the local machine to other device for connection
#will pick the ip address or server and pick up the port; bind to that address.
#AF_INET indicates types of communication protocol like ipv4 or ipv6 or bluetooth
#SOCK_STREAM is different method of sending data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected =True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMATE)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMATE)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()



def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target =handle_client, args = (conn, addr))
        thread.start()
        print("[ACTIVE CONNNECTION] {threading.activeCount() - 1}")
print("[STARTING] SERVER is starting...")
start()

