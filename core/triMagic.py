#!/usr/bin/env python
# Monitoring  client program
import socket,time,os,getpass
from hashlib import md5
import commands,sys,pickle,json
from django.core.exceptions import ObjectDoesNotExist
import db_connector  # file_transfer
from TriAquae.hosts.models import * 
import compress,key_gen

unsupported_cmds = ['vi']

socket.setdefaulttimeout(15)

help_msg ="""Avaliable arguments:
\033[32;1m
--help          show helps
--cmd           run command
--show          show groups
                show group YourGroupName
                show detail YourHostName
--filter        filter options: os, hostname, ip
		e.g. os=linux,  hostname='web' ,  ip="192.168" 
-h host         hostname,multiple host separator is,e.g. "host1, host2, host3",'ALL' means all hosts
-g group        group name,multiple group separator is ,e.g. "group1,group2"
--send 		send file to remote 
		e.g. --send  'local_filename1,local_filename2'  '/remote_path/'
--script        run script on remote client
 \033[0m"""


def no_valid_argv(option):
	print "\033[31;1mError:no valid argument found after:\033[0m",option
	sys.exit()

def print_output(string,output_type):
	if output_type == 'success':
		print '\033[32;1m%s\033[0m' % string
	elif output_type == 'error':
                print '\033[31;1m%s\033[0m' % string
	elif output_type == 'warning':
                print '\033[33;1m%s\033[0m' % string
def virify_filesize(filename):
  if os.path.isfile(filename):
	if os.path.getsize(filename) /1024  >10000: #big than 10Mb
	  if '-y' in sys.argv:
		return True
	  else:         
		print 'File after compressing is still bigger than 10Mb,transfering big size file to multiple clients could be very slow, add -y option if you want proceed this.' 
		sys.exit()
	else:
		return True

def md5_file(filename):
	if os.path.isfile(filename):
		m = md5()
		with open(filename, 'rb') as f:
			m.update(f.read())
		return m.hexdigest()
	else:
		return None

def jobRunner(action,host,job,data=None):
        PORT = 9999
        try:
        	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	s.connect((host.ip, PORT))
        except socket.error, e:
		line_len = (25 - len(host.hostname)) * '-'
                print '\033[31;1m%s %s> %s\033[0m' %(host.hostname,line_len,e)
               	return 'socket err' 
        def receive_data(sock):
                return_data = ''
                while True:
                        data = sock.recv(4096)
                        if not data:break
                        return_data += data
                return return_data
	def RSA_verify(sock):
		sock.send('RSA_KEY_Virification')
		encrypted_data = sock.recv(1024)
		try:
			decrpted_data = key_gen.RSA_key.decrypt_RSA(key_gen.private_file,encrypted_data)
			#print '\033[32;40;1m---------\033[0m', decrpted_data
			#sock.send('s %s'% decrpted_data)
			sock.send(decrpted_data)
			RSA_final_confirmation = sock.recv(1024)
			if RSA_final_confirmation != 'CorrectRSAkey':raise ValueError
		except ValueError:
			print "\033[31;1mError: RSA verification failed! Checked your RSA KEY setting in both side!\033[0m"
			sys.exit()
	RSA_verify(s)
        if action == 'CMD_Excution':
                for cmd in unsupported_cmds:
                        if job.strip().startswith(cmd):
                                print "error: doesn't support interactive command:", job
                                return '1'
                if job.strip().startswith('top'):
                        job= 'top -bn1 |head -n 25'
                s.sendall('%s| %s' %(action, job) )
                return_data = receive_data(s)
                cmd_status,result = pickle.loads(return_data)
                if cmd_status == 0:
                        print '\033[32;1m%s\t\t  result:OK \t%s\033[0m' % (host.hostname,cmd_status)
                else:
                        print '\033[31;1m%s\t\t  result:ERROR \033[0m' % host.hostname

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
			script_name = script.split('/')[-1]
			print '++++++|sending script \033[34;1m%s\033[0m to %s:'% (script_name,host.hostname)
			s.send('%s|%s|%s' %(action, script_name,md5_key ))
			file_content = ''
			with open(script, 'rb') as f:
				file_content = f.read()
			#print '\033[36;1m%s\033[0m' % file_content
			time.sleep(0.5)
			s.sendall(file_content)
			#print '++++++|Sending complete,virifiying file completion status'
			time.sleep(1)
			s.send('EndOfDataConfirmationMark')
			fileTransferStatus = s.recv(100)
			if fileTransferStatus == 'FileTransferComplete':
				print '\033[33;1mStart running %s on %s,check the log recv/%s.log on client side.\033[0m' %(script,host.hostname,script)
			elif fileTransferStatus == 'FileTransferNotComplete' : 
				print 'FileTransfer to %s Failed!' % host.hostname
			s.close()
		else:
			print 'script file not found!'
			s.close()
	if action == 'SEND_FILE':
		md5_key = data[0]
		compress_mark = data[1]
		local_filename,remote_path = job
		s.send('SEND_FILE|%s|%s|%s|%s' % (md5_key,local_filename, remote_path, compress_mark) )
		
		with open(local_filename, 'rb') as f:
		  sendingConfirmationSignal = s.recv(100)
		  if sendingConfirmationSignal == "FileOk2Send":
			print 'sending file to %s ....' % host.hostname
		  else:
			print_output('%s on %s' % (sendingConfirmationSignal,host.hostname), 'error')
			return sendingConfirmationSignal
		  while True:
			data = f.read(4096)
			if not data:break
			s.send(data)
		time.sleep(1)
		s.send('EndOfDataConfirmationMark')
		fileTransferStatus = s.recv(100)	
                if fileTransferStatus == 'FileTransferComplete':
		   print_output('Send file to %s succeed!' % host.hostname, 'success')
		   """if compress_mark == 'tarAndCompressed':
			print 'going to remove local temp file'
			os.remove(local_filename) #remove .z file
			os.remove(local_filename[:-2]) # remove .tar file
		   elif compress_mark == 'compressed':
			os.remove(local_filename) #remove .z file
		   else:
			print "what just happend? I don't trust my self."""
                elif fileTransferStatus == 'FileTransferNotComplete' :
                   print 'FileTransfer to %s Failed!' % host.hostname

		s.close()
def multi_job(hosts,task,argument,file_data = None):
	import multiprocessing
	# batch run process
	result = []
	
	if len(hosts) < 50:
		thread_num = len(hosts)
	else:
		thread_num = 50
	pool = multiprocessing.Pool(processes=thread_num)

	for h in hosts:
		#jobRunner(job_action, hosts[0], script)
		#result.append(pool.apply_async(run,(h,)) )
		result.append(pool.apply_async(jobRunner,(task,h,argument, file_data)) )

	pool.close()
	pool.join()

	for res in result:
		res.get(timeout=5)


if len(sys.argv) <2:
	print 'Argument needed, run --help for help.'	
	print help_msg
	sys.exit()


def virify_argument():
    try:
	
	host_list = []
	if '-h' in sys.argv:
		argv = '-h'
		argument  = sys.argv[ sys.argv.index( argv) +1 ].split(',')
		if argument[0] == 'ALL':
			host_list = IP.objects.all()
		else:
		  for host in argument:
			try:
				host_list.append( IP.objects.get(hostname = host.strip()) )
			except ObjectDoesNotExist:
				print "Error: host %s is not exist in the database" % host
				sys.exit()		
	elif '-g' in sys.argv:
		argv = '-g'
		argument  = sys.argv[ sys.argv.index( argv) +1 ].split(',')
		for g in argument:
			try:
				host_list.extend( IP.objects.filter(group__name= g) )
			except ObjectDoesNotExist:
				print "Error: group %s is not exist in the database" % g
                                sys.exit()
	else:
		print 'Error: must take at least 1 host or group to proceed this, 0 given.'
		sys.exit()
				
	return host_list
    except IndexError:
	print 'Error: take exactly 1 argument after %s, but 0 given!' % argv
	sys.exit()
def virify_runUser():
  try:
	if '-u' in sys.argv:
		argv = '-u'
		run_user = sys.argv[ sys.argv.index( argv) +1 ]
		return run_user
	else:
		return None
  except IndexError:
	print "Error: no argument found after -u"
	sys.exit()
  		
if '--cmd' in sys.argv:
	hosts = virify_argument()
	cmd = sys.argv[sys.argv.index('--cmd')  + 1]
	if cmd.strip().startswith('sudo'):
		password = getpass.getpass("\033[32;1mPassword:\033[0m")
		cmd = "echo %s|sudo -S %s"% (password,cmd)
	job_action = 'CMD_Excution'
        if len(hosts) > 1: # kick off multi jobs
                multi_job(hosts, job_action,cmd)
        else:
		jobRunner(job_action,hosts[0], cmd)
elif '--script' in sys.argv:
	hosts = virify_argument()
	script = sys.argv[sys.argv.index('--script')  + 1]
	job_action = 'RUN_Script'
	if len(hosts) > 1: # kick off multi jobs
		multi_job(hosts, job_action, script )
	else:
		jobRunner(job_action, hosts[0], script)
	#def multi_job(hosts,task,argument):
elif '--send' in sys.argv:
	hosts = virify_argument()
	try:
		localfile = sys.argv[sys.argv.index('--send')  + 1].strip().split(',')
		remote_path = sys.argv[sys.argv.index('--send')  + 2]
		if not remote_path.strip().startswith('/'):
			print 'remote path \033[31;1m%s\033[0m need to be absolute path, starts with /' % remote_path
			sys.exit()
		def decorate_file(filename_list):
			  file_list = []
			  for filename in filename_list:
				if not os.path.isfile(filename):
					print "Error:file %s not found or is a directory!" % filename
					sys.exit()
				else:
					file_list.append( filename )
			  print_output('compressing file......', 'success')
			  if len(file_list) >1: 
			  	tar_file = compress.tar(file_list,'temp/%s.tar' % file_list[0] )
			  	compressed_file = '%s.z' % tar_file
			  	compress.compress(tar_file, compressed_file)
				os.remove(tar_file)
			  	return compressed_file,os.path.getsize(compressed_file),'tarAndCompressed'
			  else:
				source_file = file_list[0].split('/')[-1]
				compressed_file = 'temp/%s.z'  % source_file
				compress.compress(file_list[0], compressed_file)
			  	return compressed_file,os.path.getsize(compressed_file),'compressed'
		filename,filesize, compress_mark = decorate_file(localfile)  
		if virify_filesize(filename):
			md5_key = md5_file(filename)
			if len(hosts) >1:
				multi_job(hosts,'SEND_FILE', (filename,remote_path),(md5_key,compress_mark))	
			else:
				jobRunner('SEND_FILE',hosts[0],(filename,remote_path),data=(md5_key,compress_mark))	  
	except IndexError:
		no_valid_argv('--send') 

elif '--filter' in sys.argv:
	try:
		filters = sys.argv[sys.argv.index('--filter')  + 1].split('=')
		filter_option,filter_argv = filters[0], filters[1]
		if filter_option in ('os','hostname','ip'):
		  if filter_option == 'os':
		      for i in  IP.objects.filter(os__contains=filter_argv):
			print "%s\t\033[32;1m%s\033[0m"	%(i.hostname,i.os)
		  elif filter_option == 'hostname':
		      for i in  IP.objects.filter(hostname__contains=filter_argv):
			print "%s\t\033[32;1m%s\033[0m" %(i.ip,i.hostname)
		  elif filter_option == 'ip':
                      for i in  IP.objects.filter(ip__contains=filter_argv):
                        print "%s\t\033[32;1m%s\033[0m" %(i.hostname,i.ip)

		else:
			print help_msg
	except IndexError:
		print 'Error: no valid argument found after --filter' 
elif '--show' in sys.argv:
	try:
		item = sys.argv[sys.argv.index('--show')  + 1]
	except IndexError:
		print '\033[31;1mNo valid argument found!\033[0m'
		sys.exit()
	def showItem(item_name):
		if item_name == 'groups':
			search_result = Group.objects.all()
			for group in search_result:
				ip_list = IP.objects.filter(group__name = group)
				print "\033[32;1m%s  [%s]\033[0m" %(group.name,len(ip_list))
		elif item_name == 'group':
		  try:
			group_name =sys.argv[sys.argv.index('group')  + 1]
			ip_list = IP.objects.filter(group__name = group_name)
			print "\033[32;1m%s  [%s]\033[0m" %(group_name,len(ip_list))
			for ip in ip_list:
				print "%s\t%s" %(ip.hostname,ip.ip)
		  except IndexError:
			print '\033[31;1mGroup name required!\033[0m'
		elif item_name == 'detail': 
			try:
				search_text = sys.argv[sys.argv.index('detail')  + 1]	
			except IndexError:
				no_valid_argv('detail')
			ip_list = IP.objects.filter(hostname__contains= search_text )	
			print "General info"	
			#for i in ip_list.values('hostname','ip','os','port','idc'):
			for i in ip_list:
				inGroups = IP.objects.get(hostname= i.hostname).group.values('name')	
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
else:
	print help_msg	
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
