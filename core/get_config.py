#!/usr/bin/env python
# -*- coding:utf-8 -*-
import db_connector,json,pickle
from triWeb.models import *
from django.core.exceptions import ObjectDoesNotExist

#得到一台主机所具有的的服务项。
def get_config_for_host(host=None,ip=None):
    try:
        if host is not None:
            print '---host---', host,ip
            host_obj = IP.objects.get(hostname = host)
        elif ip is not None:
            host_obj = IP.objects.get(ip = ip)
        else:
            return 'Need at least one argument to search host info'
    except ObjectDoesNotExist:
        return '[%s] object cannot be found in database.' % host
    monitor_dic={}
    monitor_list = []
    template_list = []
    #get monitor list from it's parent group
    #print "\033[31;1m-------child of groups------\033[0m" 
    
    for g in host_obj.group.select_related():
        #print g.name , g.template_list.select_related()
        for t in g.template_list.select_related():
            template_list.append(  t.name )
    #get monitor list from this host's template list
    #print '\033[31;1m--------child of templates------\033[0m'
    #print host_obj.template_list.select_related()
    for t in host_obj.template_list.select_related():
        template_list.append(  t.name )

    #get monitor list from this host's customized service list 
    #print '\033[31;1m--------customized serivices------\033[0m'
    monitor_list += host_obj.custom_services.values()

    #print "-----combined template list----"
    #print set(template_list)
    for t_name in set(template_list):
        t_obj = templates.objects.get(name=t_name)
        monitor_list += t_obj.service_list.values()
    #print monitor_list
    #for service in monitor_list:
    #   print service
    #print template_list
    monitor_dic['service']=monitor_list
    monitor_dic['hostname']=host_obj.hostname

    return monitor_dic

def get_config_for_agent(host=None,ip=None):
    try:
        if host is not None:
            print '---host---', host,ip
            agent_obj = trunk_servers.objects.get(name = host)
        elif ip is not None:
            agent_obj = trunk_servers.objects.get(ip_address = ip)
        else:
            return 'Need at least one argument to search host info'
    except ObjectDoesNotExist:
        return '[%s] object cannot be found in database.' % host
    monitor_dic={}
    host_in_agent=Ip.objects.filiter(belongs_to=agent_obj.id)
    if len(host_in_agent):
        for one_host in host_in_agent:
            monitor_dic[one_host.hostname]=get_config_for_host(host=one_host.hostname)
            #if monitor_dic[one_host.hostname] is str:say it has no monitor service
    else:
        return '%s has not monitor host in this trunk_servers' %agent_obj.host
    return monitor_dic



if __name__ == '__main__':
    host_monitor_list = get_config_for_host('server_test_18')
    print host_monitor_list
    #host_monitor_list = get_config_for_host(None,'10.168.7.101')
    if type(host_monitor_list) is not str:
        for i in  host_monitor_list:print i
    else:
        print host_monitor_list
