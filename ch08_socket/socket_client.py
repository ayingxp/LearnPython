# -*- coding: utf-8 -*-

import socket

client = socket.socket()

client.connect(('localhost', 6969))

client.send('Hello World!')

data = client.recv(1024)

print 'recv: ', data

client.close()
