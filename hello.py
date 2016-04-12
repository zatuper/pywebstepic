
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
    a={}
    response=[]
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain')]
    start_response(status, response_headers)
    if (url):
        for i in range(0, len(url)):
            print url[i], '\n'
            a.update({i:url[i]})
            response+= str(a[i]) + "\r\n"
    print "concatenated string for web response ", response
#    for key in response:
#        if key:
#           a=key+"="+url[key]+"\n"
#           response+=a
#    print 'carriage return newlined ' , response
        #for key in query.keys():
     #   a = key + "=" + query[key] + "\n"
     #   response+=a
    #print 'parsed url values', response  
   
    return ([response])
    
    
    
