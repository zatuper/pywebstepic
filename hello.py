
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
    url = env['QUERY_STRING'].split("&")
    print 'will send ', url
    values, query = parse_url_string(url)
    response=[]
    response+=query_vars[0].split("=")[1]
    response+=query_vars[1].split("=")[1]
    response+=query_vars[2].split("=")[1]
    
    #for key in query.keys():
     #   a = key + "=" + query[key] + "\n"
     #   response+=a
    #print 'parsed url values', response         
    return [response]
    
