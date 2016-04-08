from __future__ import unicode_literals

import multiprocessing

import gunicorn.app.base

from gunicorn.six import iteritems


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


def handler_app(environ, start_response):
    resp = []
    response_body = environ['QUERY_STRING'].split("&")
    for arg in response_body:
        resp = [arg+"\r\n"]
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
    ]

    start_response(status, response_headers)

    return [resp]

status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  resp = environ['QUERY_STRING'].split("&")
  resp = [item+"\r\n" for item in resp]
  return resp




class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '8080'),
        'workers': number_of_workers(),
    }
    StandaloneApplication(handler_app, options).run()
