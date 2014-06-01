
#coding:utf-8
import db_connector 

from triWeb.models import *

monitor_dic = {}
customize_monitor_list = []

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
	if  len(h.custom_services.values()) >0:
		customize_monitor_list.append(h)




for k,v in monitor_dic.items():
	print '\nTemplate:   \033[42;1m%s \033[0m' %k  #, v['template'].service_list.values()
	#services_obj = []
	monitor_host_list = set(v['host_list'])
	for service in v['template'].service_list.values(): #get will be monitored service list from this template
		s_obj = services.objects.get(name = service['name'])
		print '\033[35;1m%s \033[0m' %s_obj.name,s_obj.check_interval 
		for item_obj in s_obj.item_list.values():
			print item_obj
		print 'host list:  ',monitor_host_list


#for customized list 
print '\n-----------customize_monitor_list-------------'
for host in  customize_monitor_list: #check if each host has customized monitor list
  
  print host.hostname,'\tcustomized service:', host.custom_services.values()

  

