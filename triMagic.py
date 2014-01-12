# Monitoring  client program
import socket,time,os
from hashlib import md5
import commands,sys,pickle,json
from django.core.exceptions import ObjectDoesNotExist
import db_connector


unsupported_cmds = ['vi']

socket.setdefaulttimeout(15)

HOST = '192.168.2.246'    # The remote host
def jobRunner(action,host,job):
        PORT = 9999
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host.ip, PORT))
        except socket.error, e:
                print '\033[31;1mError:%s -------> %s\033[0m' %(host.hostname,e)
                sys.exit()
        def receive_data(sock):
                return_data = ''
                while True:
                        data = sock.recv(4096)
                        if not data:break
                        return_data += data
                return return_data
	def md5_file(filename):
		if os.path.isfile(filename):
			m = md5()
			with open(filename, 'rb') as f:
				m.update(f.read())	
			return m.hexdigest()
		else:
			return None	
        if action == 'CMD_Excution':
                for cmd in unsupported_cmds:
                        if job.strip().startswith(cmd):
                                print "error: doesn't support interactive command:", job
                                return '1'
                if job.strip().startswith('top'):
                        job= 'top -bn1 |head -n 25'
                s.sendall('%s| %s ' %(action, job) )
                return_data = receive_data(s)
                cmd_status,result = pickle.loads(return_data)
                if cmd_status == 0:
                        print '\033[32;1m%s\t\t  result:OK \t%s\033[0m' % (host,cmd_status)
                else:
                        print '\033[31;1m%s\t\t  result:ERROR \t%s\033[0m' % (host,cmd_status)

                print result
                s.close()

        if action == 'getHardwareInfo':
                s.send(action)
                return_data = receive_data(s)
                result = json.loads(return_data)
                for hardInfoName,value in result.items():
			if hardInfoName =='Memory_Slots_All':pass
			elif hardInfoName in ('Hard_Disk','System_Ip','System_Mac','Ethernet_Interface','Physical_Cpu_MHz'):
				print "\033[34;1m%s:\033[0m" %hardInfoName
				for i in value:print '\t',i
			else:
				print "\033[34;1m%s:\033[0m %s" %(hardInfoName,value)
		s.close()
	if action == 'RUN_Script':
		script = job
		md5_key =  md5_file(script)
		if md5_key is not None:
			print md5_key
			script_name = script.split('/')[-1]
			print script_name,'===='
			s.send('%s|%s|%s' %(action, script_name,md5_key ))
			with open(script, 'rb') as f:
				s.sendall(f.read())
			s.close()
		else:
			print 'script file not found!'
			s.close()

def multi_job():
	import multiprocessing
	# batch run process

	result = []
	def run(host):
		task = '''%s %s '%s' %s %s''' % (script,host,cmd,run_user,track_num)
		os.system(task)

	if len(ip_list) < 50:
		thread_num = len(ip_list)
	else:
		thread_num = 30
	pool = multiprocessing.Pool(processes=thread_num)

	for ip in ip_list:
		result.append(pool.apply_async(run,(ip,)) )
	#time.sleep(5)
	#pool.terminate()

	pool.close()
	pool.join()


	for res in result:
		res.get(timeout=5)


if len(sys.argv) <2:
	print 'Argument needed, run -h for help.'	
	help_msg ="""Avaliable arguments:
-cmd		run command
-show   	show groups
		show group YourGroupName
		show detail YourHostName
-filter 	os='linux'

-script 	run script on remote client
 """
	print help_msg
	sys.exit()

def virify_argument():
    try:
	
	host_list = []
	if '-h' in sys.argv:
		argv = '-h'
		argument  = sys.argv[ sys.argv.index( argv) +1 ].split()
		for host in argument:
			try:
				host_list.append( db_connector.IP.objects.get(hostname = host) )
			except ObjectDoesNotExist:
				print "Error: host %s is not exist in the database" % host
				sys.exit()		
	elif '-g' in sys.argv:
		argv = '-g'
		argument  = sys.argv[ sys.argv.index( argv) +1 ].split()
		for g in argument:
			try:
				host_list.extend( db_connector.IP.objects.filter(group__name= g) )
			except ObjectDoesNotExist:
				print "Error: group %s is not exist in the database" % g
                                sys.exit()
	else:
		print 'Error: must take at least 1 host or group to proceed this, 0 given.'
		sys.exit()
				
	return host_list
    except IndexError:
	print 'Error: take exactly 1 argument after %s, but 0 given!' % argv
		
if '-cmd' in sys.argv:
	hosts = virify_argument()
	print hosts
	cmd = sys.argv[sys.argv.index('-cmd')  + 1]
	job_action = 'CMD_Excution'
	jobRunner(job_action,hosts[0], cmd)
elif '-script' in sys.argv:
	hosts = virify_argument()
	print hosts
	script = sys.argv[sys.argv.index('-script')  + 1]
	job_action = 'RUN_Script'
	jobRunner(job_action, hosts[0], script)
	print script 
elif '-show' in sys.argv:
	item = sys.argv[sys.argv.index('-show')  + 1]
	def showItem(item_name):
		if item_name == 'groups':
			search_result = db_connector.Group.objects.all()
			for group in search_result:
				ip_list = db_connector.IP.objects.filter(group__name = group)
				print "\033[32;1m%s  [%s]\033[0m" %(group.name,len(ip_list))
		elif item_name == 'group':
		  try:
			group_name =sys.argv[sys.argv.index('group')  + 1]
			ip_list = db_connector.IP.objects.filter(group__name = group_name)
			print "\033[32;1m%s  [%s]\033[0m" %(group_name,len(ip_list))
			for ip in ip_list:
				print "%s\t%s" %(ip.hostname,ip.ip)
		  except IndexError:
			print '\033[31;1mGroup name required!\033[0m'
		elif item_name == 'detail': 
			search_text = sys.argv[sys.argv.index('detail')  + 1]	
			ip_list = db_connector.IP.objects.filter(hostname__contains= search_text )	
			print "General info"	
			#for i in ip_list.values('hostname','ip','os','port','idc'):
			for i in ip_list:
				inGroups = db_connector.IP.objects.get(hostname= i.hostname).group.values('name')	
				print "\033[32;1mHostname: \033[0m", i.hostname 
				print "\033[32;1mIP: \033[0m", i.ip
				print "\033[32;1mOS: \033[0m", i.os
				print "\033[32;1mSSH Port: \033[0m", i.port
				print "\033[32;1mIDC: \033[0m", i.idc
				print '\033[32;1mGroup:\033[0m',
				for g in inGroups:
					print g['name'],
				# hardware info
				print "\n\nHardWare info"
				jobRunner('getHardwareInfo',i,'' )
	showItem(item)
	sys.exit()

"""
def jobRunner(action,host,job):
	PORT = 9999  
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, PORT))
	except socket.error, e:
		print '\033[31;1mError: %s\033[0m' %e
		sys.exit()
	def receive_data(sock):
		return_data = ''
                while True:
                        data = sock.recv(4096)
                        if not data:break
                        return_data += data
		return return_data
	if action == 'CMD_Excution':
		for cmd in unsupported_cmds:
			if job.strip().startswith(cmd):
				print "error: doesn't support interactive command:", job
				return '1'
		if job.strip().startswith('top'):
			job= 'top -bn1 |head -n 25'
		s.sendall('%s| %s ' %(action, job) )
		return_data = receive_data(s)
		cmd_status,result = pickle.loads(return_data)
		if cmd_status == 0:
			print '\033[32;1m%s\t\t  result:OK \t%s\033[0m' % (host,cmd_status)
		else:
			print '\033[31;1m%s\t\t  result:ERROR \t%s\033[0m' % (host,cmd_status)
			
		print result
		s.close()

	if action == 'getHardwareInfo':
		print '=====get=info'
		s.send(action)
		return_data = receive_data(s)
                cmd_status,result = pickle.loads(return_data)
		print result
		s.close()
"""
#jobRunner(job_action,HOST, cmd)
