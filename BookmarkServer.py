#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response. status code
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write("Hello, HTTP Hassan!\n".encode())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))   # Use PORT if it's there.
    server_address = ('', port)
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
