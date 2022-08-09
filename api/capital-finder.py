from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_string_list)

        message = "Please enter valid country/capital name."

        if "country" in query_dict and "capital" in query_dict:
            try:
                url = "https://restcountries.com/v3.1/capital/"
                response = requests.get(url + query_dict["capital"])
                data = response.json()
                country = data[0]['name']['common']
                capital = query_dict['capital']
                if query_dict['country'] == country:
                    message = str(f"{capital} matches with {country}'s capital.")
                else:
                    message = str(f"The capital of {country} is NOT {capital}")
            except:
                message = 'Error. Pleas check your query entries.'

        elif "country" in query_dict:
            try:
                url = "https://restcountries.com/v3.1/name/"
                response = requests.get(url + query_dict["country"])
                data = response.json()
                capitals = data[0]["capital"]
                currencies = data[0]['currencies']
                get_cur = []
                for cur in currencies:
                    get_cur.append(cur)
                message = str(f"The capital of {query_dict['country']} {'are' if len(capitals) > 1 else 'is' } {', '.join(capitals)}. "
                              f"Currency is {', '.join(get_cur)}")
                currencies = data
            except:
                message = 'Country cannot be found.'

        elif "capital" in query_dict:
            try:
                url = "https://restcountries.com/v3.1/capital/"
                response = requests.get(url + query_dict["capital"])
                data = response.json()
                country = data[0]['name']['common']
                currencies = data[0]['currencies']
                get_cur = []
                for cur in currencies:
                    get_cur.append(cur)
                message = str(f"{query_dict['capital']} is the capital of {country}. Currency is {', '.join(get_cur)}")
            except:
                message = 'Capital cannot be found.'

        self.wfile.write(message.encode())
        return