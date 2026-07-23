#!/usr/bin/env python3
"""Simple HTTP server that forces no-cache headers so browsers always fetch fresh content."""
import http.server, os

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    def log_message(self, fmt, *args):
        print(fmt % args)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Jemm server running at http://localhost:8080 (no-cache mode)")
http.server.HTTPServer(('', 8080), NoCacheHandler).serve_forever()
