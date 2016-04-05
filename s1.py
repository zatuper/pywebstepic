import socket
import select
import sys

clients = []

server = socket.socket()
server.bind(('0.0.0.0', 2222))
server.listen(1)

while True:
    rs, ws, es = select.selct([server] + clients + [sys.stdin], [], [], 10)
    for reader in rs:
        if reader is server:
            client, (ip, port) = server.accept()
            clients.append(client)
        else:
            data = client.recv(1000)
            for recipient in clients:
                recipient.send(data)
    if not rs:
        print 'no activity for 10 seconds'
