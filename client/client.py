# Monitoring  client program
import conf,json,threading
import socket,time,sys
import scripts,key_gen,random
import commands
#HOST = '192.168.2.143'    # The remote host
HOST = '192.168.91.209'    # The remote host
PORT = 9998              # The same port as used by the server
hostname = 'localhost'
status_dic = {'services': {}}
last_check_dic = {}
interval_dic = {}

conf.BASE_DIR

#get all the services' monitor inverval and put it into interval_dic
for k,v in conf.enabled_services.items():
	if k == 'services':
		for i in v:
			service_name,service = i[0],i[1]
			if interval_dic.has_key( service.check_interval):
				interval_dic[ service.check_interval ]['name'][service_name] = service
			else:
			
				interval_dic[ service.check_interval ] = { 'name' :  { service_name : service },
									   'last_check': 0 }
			


def multi_job(m_list, m_interval):
	status_dic = {}
	#run single thread...
	def run(name,m_api):
		print 'going to run ...',name
		status_dic[name] = m_api.script.monitor()
		interval_dic[m_interval]['last_check'] = time.time()
		return interval_dic[m_interval]
	result = [] 
	for name, t in m_list.items():
		result.append(threading.Thread(target=run, args=(name,t)).start())
	
	# get result
	while True:
		if len(status_dic) == len(m_list): #all threads are finished.
			return status_dic
			break
		else: 
			time.sleep(1)


def monitor_api(m_dic, m_interval):
	status_dic = multi_job(m_dic['name'], m_interval)
	status_dic['hostname'] = hostname
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	RSA_signal,random_num = 'RSA_KEY_Virification', str(random.random())
	encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
	s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
	print '\033[34;1m sending status to Monitor server .... \033[0m' 
	s.send('ReportMonitorStatus')
	transferSignal = s.recv(1024)
	if transferSignal == 'ReadyToReceiveStatusData':
		s.sendall(json.dumps(status_dic))
	s.close()
	print "wait for the next round..."
	

# Trigger the monitor api
while True:
	for interval,monitor_dic in interval_dic.items():
		time_diff = time.time() - monitor_dic['last_check']  
		if time_diff >= interval:
			#print time_diff,'going to monitor %s ' % monitor_dic['name']
			monitor_api(monitor_dic, interval)
			#monitor_dic['last_check'] = time.time()
		else:
			print '%s hit the next inteval in %s seconds.' % (monitor_dic['name'].keys(), interval - time_diff )
	#monitor_api()
	time.sleep(5)
