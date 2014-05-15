#!/usr/bin/env python
import global_setting
import json,os,sys,threading
from conf import templates, hosts
from get_monitor_dic import get_monitor_host_list
import db_connector
from triWeb.models import Group,IP
import monitor_data_handle as alert_handle
import time,pickle,subprocess
import redis_connector 

def pull_status_data():
	#pull out status data from Redis
	monitor_dic = redis_connector.r.get('TriAquae_monitor_status')
	if monitor_dic is not None:
		monitor_dic = json.loads(monitor_dic)
		return monitor_dic
	else:
		sys.exit("No monitor data found in Redis,please check")


#host_list =   set(host_list)
def data_handler(host_dic):
	graph_dic = {}
	alert_dic = {}
	for h,p_index_list in  host_dic.items():  #p_index stands for templates.index in enabled_templates.list 
	  alert_list = []
	  graph_dic[h.hostname] = [] #initialize the list
	  for p_index in set(p_index_list):
		p = templates.enabled_templates[p_index] #find this host belongs to which template
		if monitor_dic.has_key(h.hostname): #host needs to be monitored
			if len(monitor_dic[h.hostname]) == 0: 
				alert_list.append({"ServerDown":"No data received from client,is the agent or the host down"} )
				#print "\033[31;1mno data from client, is it done?\033[0m",h.hostname
				break
			else: 
				print "\033[46;1m%s\033[0m" % h.hostname
				for service,alert_index in p.services.items():
				  try:
					s = alert_handle.handle(service,alert_index,  monitor_dic[h.hostname][service])	
					if len(s) !=0:alert_list.append(s)
				  except KeyError:
					alert_list.append({"NoValidServiceData":(service,"service not exist in client datat")} )
					
		else: #host not in database or not enalbed for monitoring
			print "\033[34;1mnot going to monitor server:\033[0m", h.hostname
	  if hosts.monitored_hosts.has_key(h.hostname):
		customized_templates= hosts.monitored_hosts[h.hostname]
		#print "*"*50,'Customized'#,customized_templates.services
		for service,alert_index in customized_templates.services.items():
		  try:	
			s = alert_handle.handle(service,alert_index,  monitor_dic[h.hostname][service])
			if len(s) !=0:alert_list.append(s)
		  except KeyError:
			alert_list.append({"NoValidServiceData":(service,"service not exist in client datat")} )
			
	  #else:
	  #	print 'no customized templates.,h
	  alert_dic[h.hostname] = alert_list
	#print '\033[41;1m*\033[0m'*50,'ALert LIST\n'
	#for host,alerts in  alert_dic.items():
	#	print '\033[31;1m%s\033[0m' %host
	#	for msg in  alerts:print msg #for i in alerts:print i
	alert_dic['TimeStamp'] = time.time()
	redis_connector.r['TempTriAquaeAlertList'] = json.dumps(alert_dic)

	#print '\033[42;1m graph list ----------\033[0m\n'
	#for h,g in graph_dic.items():
	#	print h
	#	if len(g) >0:
	#	 for s in  g:
	#		print s

def multi_job(m_dic):
	def run(name):
		print 'going to run job......',name
	threading.Thread(target=run, args=(m_dic,)).start()


time_counter = time.time()
monitor_list = get_monitor_host_list()


counter = 0
while True:
	#if time.time() - time_counter > 60: #refresh monitor list every 60 sec
		#print '------------------------------------------------------------------->'	
		#del sys.modules['conf.templates.]
		#reload(templates.service) 
		#monitor_list = get_monitor_host_list()
		#time_counter = time.time()
	monitor_dic = pull_status_data()
	data_handler( monitor_list )
	print '\033[42;1m-----Alert Checking Executed...>>>>\033[0m' ,counter
	counter += 1
	#p = subprocess.Popen('python /home/alex/tri_client/status_data_optimzation.py', stdout=subprocess.PIPE, shell=True)
	#print monitor_list
	time.sleep(10)
