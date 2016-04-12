

from __future__ import unicode_literals

def u(data):
    return data.encode("utf-8")

def common_response():
    for x in range(100):
        yield u("text:item:{0}".format(x*2))

    data = []
    for item in range(100):
        if item % 2 == 0:
            data.append("other:item.{0}".format(item))
        else:
            for subitem in range(item):
                data.append("other:subitem.{0}".format(subitem))

    yield u("\n".join(data))

def application_py2(environ, start_response):
    start_response(b'200 OK', [(b'Content-Type', b'text/plain')])
    return common_response()
