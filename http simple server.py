 #importing two class of the http.server module
#the HTTPSever module will give instruction to handle the incoming request, brain of the server
#the BaseHTTPRequestHandler will respond to incoming request with the instruction received from HTTPServer
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.0.206"
PORT = 9999

#Creating class for adding additional functionality than basic functionality provided by BaseHTTPRequestHandler
class NeuralHTTP(BaseHTTPRequestHandler):

#giving specific instruction to the code what to do, handle incoming request
    def do_GET(Self):
        Self.send_reques(200, "OK Status") #
        Self.header("content-type", "text/html")
        Self.wfile.write(bytes("html><body><h1>HELLO JEEWAN></h1></body></html>", "utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running")
server.serve_forever()
server.server_close()

print('server stop')