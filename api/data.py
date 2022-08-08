from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "Howdy"
    self.wfile.write(message.encode())

    #
    # url_components = parse.urlsplit(self.path)
    # query_string_list = parse.parse_qsl(url_components.query)
    # query_dic = dict(query_string_list)

    # url = "url"
    # response = requests.get(url)
    # data = response.json()
    # definition = []


    # friend = query_dic["friend"]

    # message=str(url_components)
    # self.wfile.write(message.encode().query)
    #self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return



