from io import StringIO
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
    stdout = StringIO()
    url = {}
    url = env['QUERY_STRING'].split("&")
    # print 'url RAW  QUERY_STRING ', url
    a={}
    response=[]
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain', 'charset=utf-8')]
    start_response(status, response_headers)
    if (url):
        for i in range(0, len(url)):
            print (url[i], '\r', '\n')
            a.update({i:url[i]})
            response+= str(a[i]) + "\r\n"
    # print "concatenated string for web response ", response
    return [resonse.encode("utf-8")]
    
