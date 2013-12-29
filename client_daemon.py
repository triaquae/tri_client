import SocketServer,time
import pickle
import monitor_list
import os,commands 
import pickle

'''
status_file = 'state/monitor_status.pkl'
if os.path.exists(status_file):
	with open(status_file) as f:
		monitor_dic = pickle.load(f)
else:
	monitor_dic = {}
	for ip in monitor_list.m_list:
		monitor_dic[ip] = 'unkown','unkown'
'''
class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
	if self.client_address[0] != '192.168.2.245':
		err_msg= "\033[31;1mIP %s not allowed to connect this server!\033[0m" % self.client_address[0]
		self.request.sendall(err_msg)
		print err_msg 
	else:
		self.data = self.request.recv(1024).strip()
		print "{} wrote:",self.client_address[0]
		if self.data.startswith('CMD_Excution|'):
			cmd = self.data.split('CMD_Excution|')[1]
			cmd_status,result = commands.getstatusoutput(cmd)	
			print 'host:%s \tcmd:%s \tresult:%s' %(self.client_address[0], cmd, cmd_status)	
		if self.client_address[0] == "127.0.0.1":
			print "going to serialize Monitor_dic"

		self.request.sendall(pickle.dumps( (cmd_status,result) ))
	
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()

