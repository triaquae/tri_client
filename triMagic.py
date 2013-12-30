# Monitoring  client program
import socket,time
import commands,sys,pickle

unsupported_cmds = ['vi']


if len(sys.argv) <2:
	print 'Argument needed, run -h for help.'	
	sys.exit()
if '-cmd' in sys.argv:
	cmd = sys.argv[sys.argv.index('-cmd')  + 1]
	job_action = 'CMD_Excution'


#HOST = '192.168.2.24'    # The remote host
HOST = '192.168.91.190'    # The remote host
def jobRunner(action,host,job):
	PORT = 9999  
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, PORT))
	except socket.error, e:
		print '\033[31;1mError: %s\033[0m' %e
		sys.exit()
	if action == 'CMD_Excution':
		for cmd in unsupported_cmds:
			if job.strip().startswith(cmd):
				print "error: doesn't support interactive command:", job
				return '1'
		if job.strip().startswith('top'):
			job= 'top -bn1 |head -n 25'
		s.sendall('%s| %s ' %(action, job) )
		return_data = ''
		while True:
			data = s.recv(4096)
			if not data:break
			return_data += data
		cmd_status,result = pickle.loads(return_data)
		if cmd_status == 0:
			print '\033[32;1m%s\t\t  result:OK \t%s\033[0m' % (host,cmd_status)
		else:
			print '\033[31;1m%s\t\t  result:ERROR \t%s\033[0m' % (host,cmd_status)
			
		print result
		s.close()



jobRunner(job_action,HOST, cmd)
