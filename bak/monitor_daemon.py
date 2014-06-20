import SocketServer,time
import pickle,json
import os 
import db_connector
"""
status_file = 'state/monitor_status.pkl'
if os.path.exists(status_file):
	with open(status_file) as f:
		monitor_dic = pickle.load(f)
else:
	monitor_dic = {}
	for ip in monitor_list.m_list:
		monitor_dic[ip] = 'unkown','unkown'
"""

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
	#if self.client_address[0] not in monitor_list.m_list:
	#	err_msg= "\033[31;1mIP %s not allowed to connect this server!\033[0m" % self.client_address[0]
	#	self.request.sendall(err_msg)
	#	print err_msg 
	if True:
		self.data = self.request.recv(1024).strip()
		print "{} wrote:",self.client_address[0]
		if self.client_address[0] == "127.0.0.1":
			print "going to serialize Monitor_dic"
			#with open(status_file,'wb') as f:
			#	pickle.dump(monitor_dic, f)
		print json.loads(self.data),'|||'
		host_obj = db_connector.IP.objects.get(hostname = 'localhost')
		obj = db_connector.ServiceStatus.objects.get(host= host_obj)
		obj.status = json.loads(self.data)
		obj.save()
		#monitor_dic[self.client_address[0]] = time.time(),self.data 
		#print monitor_dic[self.client_address[0]]
		# just send back the same data, but upper-cased
		self.request.sendall(self.data.upper())
	
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()

