def app(environ, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    #print(environ['QUERY_STRING'].replace('&','<br>').replace('\r\n',''))
    return [bytes(environ['QUERY_STRING'].replace('&',"\n"), 'utf-8')]
