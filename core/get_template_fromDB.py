
import db_connector 

from triWeb.models import *

monitor_dic = {}
customize_list = []

for t in templates.objects.all():
	monitor_dic[t.name] = {
		'template' : t,
		'host_list' : []
	 	}

#pull templates out from groups
for g in Group.objects.all():
	hosts_in_this_group = IP.objects.filter(group__name=g.name)
	#print hosts_in_this_group 
	for t in  g.template_list.values():
		monitor_dic[  t['name']  ]['host_list'].extend(hosts_in_this_group)


# pull templates out from hosts
for h in IP.objects.filter(status_monitor_on=True):
	for t in h.template_list.values(): 
		#print h,t
		monitor_dic[ t['name']]['host_list'].append(h)  


for k,v in monitor_dic.items():
	print '\033[42;1m%s \033[0m' %k, v['template'].service_list.values()
	services_obj = []
	for service in v['template'].service_list.values():
		print services.objects.get(name = service['name'])
		for host in  set(v['host_list']):
		  if len(host.custom_services.values()) >0 and host.hostname not in customize_list:
			customize_list.append( host.hostname )
		  print host.hostname  #,host.custom_services.values()

print customize_list	
