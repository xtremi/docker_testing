# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
hostName = "0.0.0.0"
serverPort = 3000

class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        contentLength = int(self.headers.get('content-length'))
        print("\tContent length: ", contentLength)
        print("\tContent type: ", self.headers.get('content-type'))
        postData = self.rfile.read(contentLength)
        
        obj = json.loads(postData)

        print("\tName  = ", obj["name"])
        print("\tValue = ", obj["value"])

        

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "tcext/plain")
        self.end_headers()
        

        if self.path == "getMessage":
            self.wfile.write(bytes("myMessage", "utf-8"))
        elif self.path == "otherMessage":
            self.wfile.write(bytes("the other message", "utf-8"))
        else:
            self.wfile.write(bytes("unknown request", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    webServer.serve_forever()


    #try:
    #    webServer.serve_forever()
    #except KeyboardInterrupt:
    #    pass
#
    webServer.server_close()
    print("Server stopped.")