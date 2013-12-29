# Monitoring  client program
import socket,time
import commands
HOST = '192.168.2.240'    # The remote host
PORT = 9999              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd_status, cmd_result = commands.getstatusoutput('grep -E "MemTotal|MemFree|Cached|SwapTotal|SwapFree"  /proc/meminfo')
print cmd_result
s.sendall(cmd_result)
data = s.recv(1024)
s.close()
print 'Received', repr(data)
print "will connecto to server 30 secs later.."
