#!/usr/bin/env python
import db_connector
from triWeb.models import Group,IP
g_name = Group.objects.get(name ='BJ')
n = 2 
for i in range(2,25):
	addr = '10.168.0.%s' % i
	add_server = IP.objects.create(

	ip = addr, 
	hostname = "server_test_%s" %n,
	display_name = "server_test_%s" %n,
	port = 22,
	os =  'Linux test',
	#group = g_name,

	)	
	n +=1
	add_server.group.add(g_name)


