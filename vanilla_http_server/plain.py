import http.server
import socketserver
import cgi
import cgitb

cgitb.enable(display=0, logdir="./tmp/logs")

PORT = 8000

# looks for the index.html file in the current directory
handler = http.server.SimpleHTTPRequestHandler

## http is a application layer protocol over TCP/IP, empty means listening on all interfaces
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# all of this can be acomplished with just python -m http.server 8080 --bind 127.0.0.1 --directory .
