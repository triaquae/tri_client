#!/usr/bin/env python
import json,os,sys
from conf import policy
import db_connector
from TriAquae.hosts.models import Group,IP
import monitor_data_handle as alert_handle
import time
import redis_connector 
status_file = 'state/monitor_status.json'

with open(status_file) as f:
	monitor_dic = json.load(f)
	

#for host, status in monitor_dic.items():
#	print host,status


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



#host_list =   set(host_list)
for h,p_index_list in  host_dic.items():  #p_index stands for policy_index in enabled_policy list 
  for p_index in p_index_list:
    	p = policy.enabled_policy[p_index] #find this host belongs to which policy
	if monitor_dic.has_key(h.hostname): #host needs to be monitored
		if len(monitor_dic[h.hostname]) == 0: 
			print "\033[31;1mno data from client, is it done?\033[0m",h.hostname
		else: 
			print "\033[46;1m%s\033[0m" % h.hostname
			#for k,v in  monitor_dic[h.hostname].items(): #k stands for the monitor indicator name
			for service,alert_index in p.services.items():
				alert_handle.handle(service,alert_index,  monitor_dic[h.hostname][service],  redis_connector.r)	
				#print  service,  monitor_dic[h.hostname][service]
				"""if p.services.has_key(k):  #services will be monitored 
					print '------------------------------------------>\033[46;1mwill only monitor \033[0m', k
					#print p.services[k]
					alert_handle.handle(k, p.services[k], v)	
				"""
	else: #host not in database or not enalbed for monitoring
		print "\033[34;1mnot going to monitor server:\033[0m", h.hostname
