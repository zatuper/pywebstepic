import socket
import select
from collections import defaultdict

BUFSIZE = 1024

def echo_server(host, port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(10)

    queue = defaultdict(list)
    rlist, wlist, = set([server_sock]), set()
    while True:
        r, w, e = select.select(rlist, wlist, [])
        for sock in r:
            if sock == server_sock:
                conn, addr = server_sock.accept()
                print "accept: %s" % conn
                rlist.add(conn)
            else:
                msg = sock.recv(BUFSIZE)
                if len(msg) == 0:
                    sock.close()
                    print "lost connection: %s" % sock
                    rlist.remove(sock)
                print "received: %s" % msg
                wlist.add(sock)
                queue[sock].append(msg)
        for sock in w:
            for msg in queue[sock]:
                 print "send: %s" % msg
                 sock.send(msg)
            queue[sock] = []

    
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 2222
    echo_server(host, port)
