CONFIG = {
    # 'mode': 'wsgi',
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
    url = url.split('&')
    resp=''
    print 'app: url', url
    for e in url:
        if (e):
           print 'app: element', e
           resp+='\n'+(str([e])).replace("'", '').replace("[",'').replace("]",'')
           #datastr='\n'.join(map(str, e)).replace("'", '').replace("[",'').replace("]",'')
    print 'app - resp', resp 
    return resp
    
