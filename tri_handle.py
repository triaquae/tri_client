#!/usr/bin/env python
import json,os,sys
from conf import policy
import db_connector
from TriAquae.hosts.models import Group,IP
import time
status_file = 'state/monitor_status.json'

with open(status_file) as f:
	monitor_dic = json.load(f)


#for host, status in monitor_dic.items():
#	print host,status



for p in  policy.enabled_policy:
	host_list = []
	if p.groups is not None:
		for g in p.groups:
			host_list.extend( IP.objects.filter(group__name = g) )
			
		for h in p.hosts:
			host_list.extend(IP.objects.filter(hostname = h) )

	host_list =   set(host_list)
	for h in  host_list:
		if monitor_dic.has_key(h.hostname):
			if len(monitor_dic[h.hostname]) == 0: 
				print "\033[31;1mno data from client, is it done?\033[0m",h.hostname
			else:
				print "\033[32;1m%s\033[0m" % h.hostname
				for k,v in  monitor_dic[h.hostname].items():
					if p.services.has_key(k): 
						print '----->will monitor ', k
						print p.services[k].index_dic
					if type(v) is dict:
						print '\033[33;1m %s \033[0m' % k
						for name,status in v.items():
						  if name == 'last_check':
						    status = time.time() - status
						    print '\t\033[33;1m%s  %s sec ago\033[0m' %(name,status)
						  else:
						    print '\t',name,status	
					else:print k,v
		else:
			print "\033[34;1mnot going to monitor server:\033[0m", h.hostname
