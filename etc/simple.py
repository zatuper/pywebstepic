
CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/path/to/my/app',
    'python': '/usr/bin/python',
    'args': (
        '--bind=127.0.0.1:8080',
        '--workers=16',
        '--timeout=60',
        'app.module',
    ),
}
import urlparse 
spisok=''

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    resp = environ['QUERY_STRING'].split("&")
    print resp
    for arg in resp:
        response_body  = [arg+"\r\n"]
    
return ["response_body"]
