
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
    url = {}
   
   # start_response('200 OK', [('Content-Type', 'text/plain')])
    url = env['QUERY_STRING'].split("&")
    print 'url RAW  QUERY_STRING ', url
    # values, query = parse_url_string(url)
    response={}
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(url)))]
    start_response(status, response_headers)
    if (url):
        for i in range(0, len(url)):
            print url[i], '\n'
            response.update({i:url[i]})
            
    print "now splited response ", response
#    for key in response:
#        if key:
#           a=key+"="+url[key]+"\n"
#           response+=a
#    print 'carriage return newlined ' , response
        #for key in query.keys():
     #   a = key + "=" + query[key] + "\n"
     #   response+=a
    #print 'parsed url values', response  
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
    return ([response])
    
    
    
