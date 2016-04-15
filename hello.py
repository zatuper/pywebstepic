def application(env, start_response):
    url = []
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url = (env['QUERY_STRING'])
    #url += "&z=0" #z=0 just for test when no url query
    url = url.split('&')
    print 'app:', url
    datastr=str(url)
    print 'app:', datastr
    datastr=' '.join(map(str, url))
    print 'app:', datastr
    datastr='\n'.join(map(str, url)).replace("'", '').replace("[",'').replace("]",'')
    #url = '\r\n'.join([url]) 
    #url = '\r\n'.join([(env['QUERY_STRING'].split("&"))])
    #print 'app: url', url
    #for e in url:
    #    if e:
    #       print 'app: element', e
    #       resp+='\n'+(str([e])).replace("'", '').replace("[",'').replace("]",'')
    #       #datastr='\n'.join(map(str, e)).replace("'", '').replace("[",'').replace("]",'')
    #print 'app - resp', resp 
    return datastr
