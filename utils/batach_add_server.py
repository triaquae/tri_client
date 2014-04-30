#!/usr/bin/env python
import db_connector
from TriAquae.hosts.models import Group,IP
g_name = Group.objects.get(name ='BJ')
n = 760 
for i in range(1,254):
	addr = '192.168.97.%s' % i
	add_server = IP.objects.create(

	ip = addr, 
	hostname = "server_test_%s" %n,
	port = 22,
	os =  'Linux test',
	#group = g_name,

	)	
	n +=1
	add_server.group.add(g_name)


