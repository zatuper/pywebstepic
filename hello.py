
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

  

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url = env['QUERY_STRING']
    print 'will send ', url
    values, query = parse_url_string(url)
    response=[]
    for key in query.keys():
        a = key + "=" + query[key] + "\n"
        response+=a
    print 'parsed url values', response         
    return [response]
    
def parse_url_string(url):
    print  'received', url,
    # params = url.split('?')[1].split('&')
    params = url.split('&')
    car = {}
    for param in params:
        car[param.split('=')[0]] = param.split('=')[1]
    return (values,  query)   
