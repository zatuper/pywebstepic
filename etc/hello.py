#!/usr/bin/python3

def handler_app(environ, start_response):
    resp = []
    status = '200 OK'
    resp = environ['QUERY_STRING'].split("&")
    for arg in resp:
        response_body  = [arg+"\r\n"]

    response_headers = [
        ('Content-Type', 'text/plain'),
    ]

    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':
    handler_app.run()
