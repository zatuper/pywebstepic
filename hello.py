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
  #  url = {}
  #  url = env['QUERY_STRING'].split("&")
  #  # print 'url RAW  QUERY_STRING ', url
  #  a={}
 #   response=[]
 #   status = '200 OK'
 #   response_headers = [
 #       ('Content-type','text/plain')]
#    start_response(status, response_headers)
   # if (url):
   #     for i in range(0, len(url)):
   #         print (url[i], '\r', '\n')
  #          a.update({i:url[i]})
 #           response+= str(a[i]) + "\r\n"
    # print "concatenated string for web response ", response
#    return [response.encode("utf-8")]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url = (env['QUERY_STRING'])
    url = env['QUERY_STRING']
    url = url.split('&')
    print 'app: url', url
    for e in url:
        if (e):
           print 'app:', e
           datastr=str(e)
           print 'app:', datastr
           datastr=' '.join(map(str, e))
           print 'app:', datastr
           datastr='\n'.join(map(str, e)).replace("'", '').replace("[",'').replace("]",'')
           #url = '\r\n'.join([url]) 
           #url = '\r\n'.join([(env['QUERY_STRING'].split("&"))])
        resp='\r\n'.join(datastr)
        print 'app - resp', resp 
    return resp    
