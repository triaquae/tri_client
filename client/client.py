# Monitoring  client program
import conf,json
import socket,time
import scripts
import commands
HOST = '192.168.2.252'    # The remote host
PORT = 9999              # The same port as used by the server

status_dic = {'services': {}}
last_check_dic = {}
interval_dic = {}

conf.BASE_DIR
for k,v in conf.enabled_services.items():
	if k == 'services':
		for i in v:
			service_name,service = i[0],i[1]
			if interval_dic.has_key( service.check_interval):
				interval_dic[ service.check_interval ]['name'][service_name] = service
			else:
			
				interval_dic[ service.check_interval ] = { 'name' :  { service_name : service },
									   'last_check': 0 }
			

print interval_dic


def monitor_api(m_dic):
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#s.connect((HOST, PORT))
	status_dic = {}
	for name, service in m_dic.items():
		value_dic = service.script.monitor() 
		print name, value_dic,'|||'
			


	#s.sendall(json.dumps(status_dic))
	#data = s.recv(1024)
	#s.close()
	#print 'Received', repr(data)
	print "will connecto to server 30 secs later.."

while True:
	for interval,monitor_dic in interval_dic.items():
		time_diff = time.time() - monitor_dic['last_check']  
		if time_diff >= interval:
			print time_diff,'going to monitor %s ' % monitor_dic['name']
			monitor_api(monitor_dic['name'])
			monitor_dic['last_check'] = time.time()
		else:
			print 'not hit the inteval time yet.'
	#monitor_api()
	time.sleep(5)
