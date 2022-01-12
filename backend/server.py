# Python 3 server example
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

from Cart import InstaCart

hostName = "localhost"
serverPort = 8080
cart = InstaCart('naterush1997@gmail.com', '../password-instacart.txt')
cart.login()

DIRECTORY = '../ui/out'


class MyServer(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/getcurrentrecipe'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(cart.to_JSON().encode('utf8'))
            return
        else:
            # Serve the files, doh
            super().do_GET()

    def do_POST(self):

        if self.path.startswith('/setcurrentrecipe'):
            content = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode('utf8'))
            url = content['url']

            print("Adding url")
            
            # Add the recipe
            cart.add_recipe(url)

            # Send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
        if self.path.startswith('/toggle_ingredient'):
            content = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode('utf8'))
            index = content['index']
            cart.toggle_ingredient(index)

            # Send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
        if self.path.startswith('/clear'):
            cart.clear()
            # Send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

# TODO: 1. serve the folder that's at out
# TODO: 