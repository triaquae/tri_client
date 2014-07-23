import time,pickle,os



status_dic = {} 
status_file = 'state/monitor_status.pkl'
while True:
	os.system('python m_trigger.py')

	with open(status_file) as f:
		monitor_dic= pickle.load(f)
	current_time = time.time()
	for ip, values in monitor_dic.items():
	    time_stamp = values[0]
	    if time_stamp != 'unkown':
		time_diff = current_time - time_stamp
		if time_diff >30:
			print '\033[31;1m %s --- %s \033[0m' %(ip, time_diff)
		else: #status ok
			print '\033[32;1m %s --- %s \033[0m' %(ip, time_diff)
			print values[1]
	    else:
		if status_dic.has_key(ip):
			if status_dic[ip]['unkown_counter'] > 2:
				print '\033[31;1m %s --- Done \033[0m' %ip
			else:
				print "\033[31;1mhost %s's  status is unkown\033[0m"  % ip
				status_dic[ip]['unkown_counter'] += 1
		else:
			status_dic[ip] = {'unkown_counter': 1}
				
	time.sleep(10)	
