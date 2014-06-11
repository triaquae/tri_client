#coding:utf-8
import db_connector 
from triWeb.models import *
monitor_dic = {}
customize_monitor_list = []
'''
for t in templates.objects.all():
    monitor_dic[t.name] = {
        'template' : t,
        'host_list' : []
        }

#pull templates out from groups
##{u'templates': {'host_list': [<IP: zxb_work>, <IP: vm_work>], 'template': <templates: templates>},
for g in Group.objects.all():
    hosts_in_this_group = IP.objects.filter(group__name=g.name)
    #print hosts_in_this_group 
    for t in  g.template_list.values():
        monitor_dic[  t['name']  ]['host_list'].extend(hosts_in_this_group)

# pull templates out from hosts,
#{u'templates': {'host_list': [<IP: zxb_work>, <IP: vm_work>, <IP: zxb_work>, <IP: vm_work>], 'template': <templates: templates>},
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
'''
#zxb自己设计监控字典。通过service与ip进行查询

def get_host():
    host_list=[]
    for h in IP.objects.all():
        host_list.append(h)
    return host_list
    #host_list=IP.objects.all()

#得到所有主机的监控信息字典
def get_host_monitor_dic():
    host_monitor_dic={}
    for h in get_host():
        service_list=[]
        #proxy_ip=h.belongs_to.ip_address
        for service in h.custom_services.all():
            tmp_dic={}
            tmp_dic['service']=service.name
            tmp_dic['interval']=service.check_interval
            service_list.append(tmp_dic)
        host_monitor_dic[h.ip]=service_list
    return host_monitor_dic

#处理字典,处理每个trunk_server所具有的主机监控项
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

#1得到一台服务端本地主机的监控信息，必须知道该代理位置。
def get_one_host_monitor_dir(host_ip,server_ip):
    monitor_dic={}
    service_list=[]
    #得到该主机的代理
    tc=trunk_servers.objects.filter(ip_address=server_ip)#tc[0].id
    if len(tc)!=1:
        print 'trunk_servers is not only.....'
        return 0
    else:
        host=IP.objects.filter(ip=host_ip,belongs_to=1)
        if len(host) !=1:
            print 'host clint is not only.....'
            return 0
        else:
            for service in host[0].custom_services.all():
                tmp_dic={}
                tmp_dic['service']=service.name
                tmp_dic['interval']=service.check_interval
                service_list.append(tmp_dic)
            monitor_dic[host_ip]=service_list
            monitor_dic['hostname']=host[0].hostname
            return monitor_dic

#print get_one_host_monitor_dir('10.168.7.69','10.168.7.69')
def test():
    interval_dic={}
    monitor_dic=get_one_host_monitor_dir('10.168.7.35',1)
    for ip in monitor_dic.keys():
            for service in monitor_dic[ip]:
                #monitor_dic[ip] is a service list 
                for m in service.keys():
                    #得到监控项和时间
                    if m=='interval':
                        interval=service[m]
                    else:
                        service_name=service[m]
                if interval_dic.has_key(interval):
                    interval_dic[interval]['name'][service_name] = service
                    #interval_dic[interval]['name'] = service_name
                else:
                    interval_dic[interval] = { 'name' : { service_name : service},'last_check': 0 }
                    #interval_dic[interval] = { 'name': service_name ,'last_check': 0 }
    return interval_dic

#2得到某个代理中具有的监控字典,如果不存在怎么办？？？
def get_proxy_monitor_list(proxy_ip):
    proxy_monitor_dic={}
    #monitor_list={}
    host_monitor_dic=get_host_monitor_dic()
    tc=trunk_servers.objects.filter(ip_address=proxy_ip)
    if len(tc)!=1:
        print 'trunk_server is not.....'
        return 0
    else:
        hosts_in_this_trunk_server=IP.objects.filter(belongs_to=tc[0].id)
        if len(hosts_in_this_trunk_server):
            for h in hosts_in_this_trunk_server:
                tmp_dic={}
                tmp_dic[h.ip]=host_monitor_dic[h.ip]
                tmp_dic['hostname']=h.hostname
                proxy_monitor_dic[h.ip]=tmp_dic
                #proxy_monitor_list.append(tmp_dic)        
            return proxy_monitor_dic
    return 0
#print get_proxy_monitor_list('10.168.7.69')

#得到某个主机改变的监控项信息
def get_change_monitor_dic(hostname):
    monitor_dic={}
    service_list=[]
    host=IP.objects.filter(hostname=hostname)
    if len(host)!=1:
        print 'error......'
        return 0
    else:
        for service in host[0].custom_services.all():
            tmp_dic={}
            tmp_dic['service']=service.name
            tmp_dic['interval']=service.check_interval
            service_list.append(tmp_dic)
        monitor_dic[host[0].ip]=service_list
        monitor_dic['hostname']=hostname
        return monitor_dic
#得到某个主机的ip
def get_host_ip(hostname):
    host=IP.objects.filter(hostname=hostname)
    if len(host)!=1:
        print 'error......'
        return 0
    else:
        host_ip=host[0].ip
        return host_ip
        
#得到某个主机所属的代理id
def get_host_proxy(hostname):
    #可能查不到该ip
    host=IP.objects.filter(hostname=hostname)
    if len(host)!=1:
        print 'error......'
        return 0
    else:
        belongs_to=host[0].belongs_to
        return belongs_to
#print get_host_proxy('5245')
#得到某个代理ip           
def get_proxy_ip(proxy_id):
    proxy=trunk_servers.objects.filter(id=proxy_id)
    if len(proxy)!=1:
        print 'error......'
        return 0
    else:
        ip_address=proxy[0].ip_address
        return ip_address
    
    
    