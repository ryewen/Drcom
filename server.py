#!/usr/bin/python
import socket
import commands
import os

HOST='104.225.155.60'
PORT=50007

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while 1:
       conn,addr=s.accept()
       print'Connected by',addr
       try:
         first = 1
         count = 1
         while 1:
              ifCom = 0
              #conn.send('1')
              #data = conn.recv(1024)
              f = open("/root/count.txt", "r")
              ncount = int(f.read())
              f.close()
              if ncount != count:
                  count = ncount
                  if first == 1:
                      first = 0
                  else:
                      ifCom = 1
                  first = 0
              if ifCom == 1:
                  print "Sent command"
                  conn.send('sh /tmp/drcom_shutdown.sh')
                  data = conn.recv(1024)
                  print data
              else:
                  conn.send('1')
                  data = conn.recv(1024)
       except socket.error as e:
         print 'Connect break'
       finally:
         conn.close()


