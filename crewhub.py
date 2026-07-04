#!/usr/bin/env python3

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8090))
STATUS_MESSAGE = os.environ.get("STATUS_MESSAGE", "CrewHub is running")


class CrewHubHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>CrewHub</title>
        </head>
        <body>
            <h1>CrewHub Status Page</h1>
            <p><strong>Status:</strong> {STATUS_MESSAGE}</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        # Suppress default console logging
        return


server = HTTPServer(("0.0.0.0", PORT), CrewHubHandler)

print(f"CrewHub running on port {PORT}")
print(f"Status message: {STATUS_MESSAGE}")

server.serve_forever()
