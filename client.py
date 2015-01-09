#!/usr/bin/python
# client.py
# Copyright (C) 2011 Ershad K <ershad92@gmail.com>
# Copyright (C) 2014 Estu Fardani <estu@di.blankon.in>
# Usage - python client.py <message>

import socket
import sys

#sys.argv.remove(sys.argv[0])

f = open("userinfo.txt")
username = f.readline();
f.close();

chat = raw_input(username.strip()+": ")
data = chat

# how stream for server

# for item in sys.argv:
#     data += item
#     data += ' '
# print data

HOST = 'localhost' # hostname / IP of server
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(username[:-1] + ": " + data)
data = s.recv(1024)
s.close()

## gimana biar ndak close