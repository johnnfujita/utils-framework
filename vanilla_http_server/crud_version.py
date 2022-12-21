import cgi
import cgitb
from http.server import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                message = "Hello!"
                self.wfile.write(bytes(message, "utf8"))
                return
            if self.path.endswith("/user/new"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Create Profile</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/user/new'>"
                output += "<input name = 'new-username' type = 'text' placeholder = 'New Username' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(bytes(output, "utf-8"))
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/user/new"):
                print(self.headers._headers)
                ctype = cgi.parse_header(self.headers._headers["05"])
                if ctype == "mulitpart/form-data":
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get("new-username")

                    self.send_response(201)
                    self.send_header("Content-type", "text/html")
                    self.send_header("Location", "/hello")
                    self.end_headers()

        except:
            pass


def main():
    try:
        server = HTTPServer(("", 8080), WebServerHandler)
        print("Web Server running on port 8080")
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == "__main__":
    main()
