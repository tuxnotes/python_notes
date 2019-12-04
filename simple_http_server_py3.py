# _*_ coding:utf-8 _*_
#!/usr/bin/python3

import http.server


class RequestHandler(http.server.BaseHTTPRequestHandler):

    page = """
        <html>
        <body>
        <p> Hello, Web! </p>
        </body>
        </html>
    """

    # handle request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.page)))
        self.end_headers()
        self.wfile.write(self.page)


if __name__ == "__main__":
    serverAddress = ("", 8080)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()