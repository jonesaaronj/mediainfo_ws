import http.server
import urllib.parse
import subprocess
import json

class CommandHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)

        file = query_params['file'][0]

        result = subprocess.check_output(['mediainfo', '--output=JSON', file], text=True)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))

if __name__ == '__main__':
    PORT = 8000
    with http.server.HTTPServer(("", PORT), CommandHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
