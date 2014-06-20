
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


print monitor_dic

print '*'*50

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
print '\n\033[31;1m-----------customize_monitor_list-------------\033[0m'
for host in  customize_monitor_list: #check if each host has customized monitor list
  
	print host.display_name,'\tcustomized service:', host.custom_services.values()

  
'''
#zxb自己设计监控字典。通过service与ip进行查询

def get_host():
    host_list=[]
    for h in IP.objects.all():
	host_list.append(h)
    return host_list
    #host_list=IP.objects.all()

#得到主机的监控信息字典
def get_host_monitor_dic():
    host_monitor_dic={}
    for h in get_host():
	service_list=[]
	#proxy_ip=h.belongs_to.ip_address
	for service in h.custom_services.all():
	    tmp_dic={}
	    tmp_dic['services']=service.name
	    tmp_dic['interval']=service.check_interval
	    service_list.append(tmp_dic)
	host_monitor_dic[h.ip]=service_list
    return host_monitor_dic

def get_server_monitor_dic():
    server_monitor_dic={}
    host_monitor_dic=get_host_monitor_dic()
    for tc in trunk_servers.objects.all():
        host_list=[]
        hosts_in_this_trunk_server=IP.objects.filter(belongs_to=tc.id)
        for h in hosts_in_this_trunk_server:
            tmp_dic={}
            tmp_dic[h.ip]=host_monitor_dic[h.ip]
            host_list.append(tmp_dic)
        server_monitor_dic[tc.ip_address]=host_list
    return server_monitor_dic

#得到某个代理中具有的监控字典
def get_proxy_monitor_list(proxy_ip):
    proxy_monitor_list=[]
    server_monitor_dic=get_server_monitor_dic()
    proxy_monitor_list=server_monitor_dic[proxy_ip]
    return proxy_monitor_list

print get_host_monitor_dic()
print get_server_monitor_dic()

print get_proxy_monitor_list('10.168.0.218')
'''
