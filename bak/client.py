# Monitoring  client program
import socket,time,json
import commands
HOST = '192.168.2.129'    # The remote host
PORT = 9998              # The same port as used by the server
status_file = 'state/monitor_status.json'
#--------------

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('getMonitorStatusData')
#data = s.recv(1024)
s.close()

time.sleep(2)
with open(status_file) as f:

	monitor_dic = json.load(f)
	for k,v in monitor_dic.items():
		print k,v

print "will connecto to server 30 secs later.."
