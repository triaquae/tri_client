#!/usr/bin/env python
import json,os,sys
from conf import policy, hosts
import db_connector
from TriAquae.hosts.models import Group,IP
import monitor_data_handle as alert_handle
import time
import redis_connector 

#pull out status data from Redis
monitor_dic = redis_connector.r.get('TriAquae_monitor_status')
if monitor_dic is not None:
	monitor_dic = json.loads(monitor_dic)
else:
	sys.exit("No monitor data found in Redis,please check")
	
#pull out all the hosts in enabled_policy
host_dic = {}
for n,p in  enumerate(policy.enabled_policy):
	if p.groups is not None: 
		for g in p.groups:
		  for h in IP.objects.filter(group__name = g):
			if not host_dic.has_key(h): 
				host_dic[h] = [n] #add policy order into dic 
			else:
				host_dic[h].append(n)

			#host_list.extend( IP.objects.filter(group__name = g) )
	if p.hosts is not None:	
		for h in p.hosts:
			host = IP.objects.get(hostname= h)
			if not host_dic.has_key(host):
				host_dic[host] = [n] #add policy order into dic
			else:
				if n not in host_dic[host]: #will not add the duplicate policy name
					host_dic[host].append(n)
print host_dic
print "\033[42;1m-----\033[0m"


#host_list =   set(host_list)
for h,p_index_list in  host_dic.items():  #p_index stands for policy_index in enabled_policy list 
  alert_list = []
  for p_index in p_index_list:
    	p = policy.enabled_policy[p_index] #find this host belongs to which policy
	if monitor_dic.has_key(h.hostname): #host needs to be monitored
		if len(monitor_dic[h.hostname]) == 0: 
			print "\033[31;1mno data from client, is it done?\033[0m",h.hostname
		else: 
			print "\033[46;1m%s\033[0m" % h.hostname
			for service,alert_index in p.services.items():
				#print service,alert_index , monitor_dic[h.hostname]
				# here should be add a exception , for the monitor_dic[h.hostname][service],  if no data for this service from client ,will trigger exception 
				s = alert_handle.handle(service,alert_index,  monitor_dic[h.hostname][service])	
				alert_list.append(s)
	else: #host not in database or not enalbed for monitoring
		print "\033[34;1mnot going to monitor server:\033[0m", h.hostname
  if hosts.monitored_hosts.has_key(h.hostname):
	customized_policy = hosts.monitored_hosts[h.hostname]
	print "*"*50,customized_policy.services
	for service,alert_index in customized_policy.services.items():	
		s = alert_handle.handle(service,alert_index,  monitor_dic[h.hostname][service])
		alert_list.append(s)
  else:
	print 'no customized policy',h
  print '+'*50,alert_list,'\n'
