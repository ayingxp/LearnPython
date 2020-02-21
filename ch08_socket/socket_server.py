# -*- coding: utf-8 -*-

import socket

server = socket.socket()

server.bind(('localhost', 6969))

server.listen(10)

conn, addr = server.accept()


data = conn.recv(1024)

print 'recv: ', data

conn.send(data.upper())
