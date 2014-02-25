import SocketServer,time
import pickle,json
import monitor_list
import os,commands,stat
from hashlib import md5
import db_connector,key_gen
from TriAquae.hosts.models import IP
recv_dir = 'recv/'

server_address = '192.168.2.248'
block_list = []
status_file = 'state/monitor_status.json'

if os.path.exists(status_file):
	with open(status_file) as f:
		monitor_dic = json.load(f)
		#make sure all the hosts are in the monitor list
		for h in IP.objects.filter(status_monitor_on=True):
			if h.hostname not in monitor_dic.keys():
				monitor_dic[h.hostname] = {}
else:
	monitor_dic = {}
	for h in IP.objects.filter(status_monitor_on=True):
		 monitor_dic[h.hostname] = {}


print monitor_dic 

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
		return_data ='' 
                while True:
                        data = sock.recv(4096)
			#print '\033[36;1m%s\033[0m' %data
			if data == 'EndOfDataConfirmationMark':
				print 'file transfer done==='
				break
                        return_data += data
		#print '\033[34;1m=====\033[0m',return_data
                return return_data
        # self.request is the TCP socket connected to the client
	def RSA_verifyication(sock):
		RSA_signal, encrypted_data,random_num_from_client = json.loads(sock.recv(1024))
		if RSA_signal == 'RSA_KEY_Virification':
			encrypted_data = "iwTgqSzMcNOHauWdXXc+rgfbWt6IUXmdIXUqNUJ2U7FZKISc2WR2yAJrq7ldR3TxQEppWgIo/Ycj\nA5gl0fGDVvAEvV02CKZ3gZEI6fWpiMoy6ucpFFDyVAWUrpiXdUOVKxOsDXGgeOObgvd1jsEQCo4i\ncLCBTWDn0HfyQic+Btm1txXc7Nw9jknUCZx6Y8I+6JaIYjNRLwJ6kSMwpTsfP37lvrQfdUkWu3bX\npV9z3hHOQ6+A8rlK7fmL1zk75TXDCmnrLY88UIv6BL4zPXtim4BCD7PlOvDG296br0VIcvF5uhqr\ntj7zOcbA81P1JBFm1nMJqLv+SB5sit923v05XA==\n"
			
			try:
				decrpted_data = key_gen.RSA_key.decrypt_RSA(key_gen.private_file,encrypted_data)
				#print decrpted_data,'+++++++', random_num_from_client
			except ValueError:
				decrpted_data = 'Incorrect decryption'
			if decrpted_data != random_num_from_client:
				return 0
		else:
			return 0
		#print RSA_singal, encrypted_data 	
	if RSA_verifyication(self.request) == 0: #didn't pass the RSA virification

		#if self.client_address[0] != server_address:
		err_msg= "\033[31;1mIP %s didn't pass the RSA virification,drop it!\033[0m" % self.client_address[0]
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
			cmd= self.data.split('CMD_Excution|')[1]
			print cmd,'=====|||||'
			cmd_status,result = commands.getstatusoutput(cmd)	
			print 'host:%s \tcmd:%s \tresult:%s' %(self.client_address[0], cmd, cmd_status)	
			self.request.sendall(pickle.dumps( (cmd_status,result) ))
		elif self.data.startswith('RUN_Script|'):
			recv_data= self.data
			filename = "%s%s" %(recv_dir,recv_data.split('|')[1].strip())
			print '+++++|receiving file from server:',filename
			md5_key_from_client = self.data.split('|')[2]
			file_content = receive_data(self.request)
			print 'write data into file....'
			with open(filename, 'wb') as f:
				f.write(file_content)
			md5_key= md5_file(filename )
			print '+++++|verfiying md5key---'
			if md5_key == md5_key_from_client:	
				print 'file transfer verification ok' 
				self.request.send('FileTransferComplete')	
				os.system('chmod +rx %s ' % filename)
				#os.chmod(filename,stat.S_IREAD+stat.S_IWOTH+stat.S_IXUSR+stat.S_IRWXO)
				cmd = "nohup  %s > %s.log &" % (filename, filename)
				print '\033[32;1mgoing to run script:\033[0m',cmd
				result = os.system(cmd )
				#print result,'||||+|||'
			else:
				print "file not complete"
				self.request.send('FileTransferNotComplete')	
		elif self.data == "getMonitorStatusData":
			print "going to serialize Monitor_dic"
			with open(status_file, 'wb') as f:
				json.dump(monitor_dic, f)
		elif self.data == 'getHardwareInfo':
			import Hardware_Collect_Script
			hardware_data = Hardware_Collect_Script.collectAsset() 
			self.request.sendall(hardware_data )
		elif self.data == 'ReportMonitorStatus':
			self.request.send('ReadyToReceiveStatusData')	
			status_data = json.loads(self.request.recv(8096) )	
			client_hostname =  status_data['hostname']
			for name,service_status in status_data.items():
				monitor_dic[ client_hostname][name] =  service_status
			print monitor_dic[client_hostname]
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9998

    # Create the server, binding to localhost on port 9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()

