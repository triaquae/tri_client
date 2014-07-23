# Monitoring  client program
import socket,time

HOST = '127.0.0.1'    # The remote host
PORT = 9999              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
print "will connecto to server 30 secs later.."
