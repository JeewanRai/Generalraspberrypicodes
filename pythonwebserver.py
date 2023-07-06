#importing http webserver library
#BaseHTTPRequestHandler is like brain that understands request sent and respond to the request
#HTTPServer is similar to body that receives request and send it to brain or receive respond from brain and sent out
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/led/on':
            print("Requiest Received")
            #led code

        self.send_response(200)
        self.emd_headers()
httpd = HTTPServer(("", 8080, MyHandler))
http.server_forever()