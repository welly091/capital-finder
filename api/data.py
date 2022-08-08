from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    url_components = parse.urlsplit(self.path)

    message=str(url_components)
    self.wfile.write(message.encode())
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return