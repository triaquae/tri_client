import SocketServer,time
import pickle
import monitor_list
import os,commands 
from hashlib import md5
recv_dir = 'recv/'

server_address = '127.0.0.1'
block_list = []
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
        def md5_file(filename):
                if os.path.isfile(filename):
                        m = md5()
                        with open(filename, 'rb') as f:
                                m.update(f.read())
                        return m.hexdigest()
                else:
                        return None
        def receive_data(sock):
                return_data = ''
                while True:
                        data = sock.recv(4096)
                        if not data:break
                        return_data += data
                return return_data
        # self.request is the TCP socket connected to the client
	if self.client_address[0] != server_address:
		err_msg= "\033[31;1mIP %s not allowed to connect this server!\033[0m" % self.client_address[0]
		pickle_data = '', err_msg
		self.request.sendall( pickle.dumps(pickle_data)  )
		print err_msg 
		block_list.append(self.client_address[0])
		if block_list.count(self.client_address[0]) > 5:
			print "Alert::malicious attack from:" , self.client_address[0]
	else:
		self.data = self.request.recv(1024).strip()
		print "{} wrote:",self.client_address[0]
		if self.data.startswith('CMD_Excution|'):
			cmd = self.data.split('CMD_Excution|')[1]
			cmd_status,result = commands.getstatusoutput(cmd)	
			print 'host:%s \tcmd:%s \tresult:%s' %(self.client_address[0], cmd, cmd_status)	
			self.request.sendall(pickle.dumps( (cmd_status,result) ))
		if self.data.startswith('RUN_Script|'):
			filename = "%s%s " %(recv_dir,self.data.split('|')[1])
			md5_key_from_client = self.data.split('|')[2]
			file_content = receive_data(self.request)
			with open(filename, 'wb') as f:
				f.write(file_content)
			md5_key= md5_file(filename )
			if md5_key == md5_key_from_client:		
				print 'file transfer verification ok' 
			else:
				print "file not complete"
		if self.client_address[0] == "127.0.0.1":
			print "going to serialize Monitor_dic"
		if self.data == 'getHardwareInfo':
			import Hardware_Collect_Script
			hardware_data = Hardware_Collect_Script.collectAsset() 
			self.request.sendall(hardware_data )
	
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()

