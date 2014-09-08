#!/usr/bin/env python
# -*- coding:utf-8 -*-
import global_setting
import json,os,sys,threading
from conf import templates, hosts
import db_connector
from triWeb.models import *
from django.core.exceptions import ObjectDoesNotExist
import get_config
        
#得到一个server/proxy_server的空监控字典
def get_monitor_empty_dic(server_ip):
    monitor_dic={}
    try:
        ts=trunk_servers.objects.get(ip_address=server_ip)
        print ts
        for host_obj in ts.ip_set.all():
            monitor_dic[host_obj.hostname]={"hostname":host_obj.hostname,'result_values':{}}
            service_list=[]
            template_list=[]
            for g in host_obj.group.select_related():
                for t in g.template_list.select_related():
                    template_list.append( t.name)
                    
            for t in host_obj.template_list.select_related():
                template_list.append( t.name)
            
            #通过所属组、所属模板的servers
            for t_name in set(template_list):
                t_obj = templates.objects.get( name = t_name)
                service_list +=t_obj.service_list.values()
            #主机本身具有的servers
            service_list +=host_obj.custom_services.values()
            #如果监控服务项为空
            if len(service_list):
                for service in service_list:
                    monitor_dic[host_obj.hostname]['result_values'][service['name']]={}
            else:
                pass
        return monitor_dic
    except ObjectDoesNotExist,err:
        print err

#得到一个server/proxy_server的所有主机的监控服务项信息字典
def get_all_host_monitor_dic(server_ip):
    monitor_dic={}
    try:
        ts=trunk_servers.objects.get(ip_address=server_ip)
        for host_obj in ts.ip_set.all():
            monitor_dic[host_obj.hostname]={}
            service_list=[]
            template_list=[]
            for g in host_obj.group.select_related():
                for t in g.template_list.select_related():
                    template_list.append( t.name)
                    
            for t in host_obj.template_list.select_related():
                template_list.append( t.name)
            
            #通过所属组、所属模板的servers
            for t_name in set(template_list):
                t_obj = templates.objects.get( name = t_name)
                service_list+=t_obj.service_list.all()
            #主机本身具有的servers
            service_list += host_obj.custom_services.all()
            #如果监控服务项为空
            if len(service_list):
                for service in service_list:
                    #item_list=service.item_list.values()
                    #trigger_list=service.trigger_list.values()
                    monitor_dic[host_obj.hostname][service.name]=service
            else:
                pass
        return monitor_dic
    except ObjectDoesNotExist,err:
        print 'not get monitor dic...'

def get_all_template_dic():
    monitor_dic={}
    custom_monitor_list=[]
    for t in templates.objects.all():
        service_list=[]
        services=t.service_list.all()
        for service in t.service_list.all():
            service_list.append(service.name)
        monitor_dic[t.name] ={
            'template':t,
            'host_list':[],
            'service_list':service_list
        }
    for g in Group.objects.all():
        try:
            hosts_in_this_group=IP.objects.filter(group__name=g.name)
        except ObjectDoesNotExist,err:
            print 'error'
        for t in g.template_list.values():
            monitor_dic[t['name']]['host_list'].extend(hosts_in_this_group)
            
    for h in IP.objects.filter(status_monitor_on=True):
        for t in h.template_list.values():
            monitor_dic[t['name']]['host_list'].append(h)
        if len(h.custom_services.values()) >0:
            custom_monitor_list.append(h)
        
    return monitor_dic,custom_monitor_list   
       
#得到每个服务的监控项等字典
def get_service_dic(serv=None):
    service_dic={}
    if serv is None:
        for service in services.objects.all():
            print service
            item_list=service.item_list.all()
            #trigger_list=service.trigger_list.all()
            try:
                trigger = triggers.objects.get(name=service.trigger)
                #print trigger.expression
                host_list=service.ip_set.all()
                #host_list+=get_all_template_dic()[]
                #error no template_set???
                template_list=service.templates_set.all()
                print template_list
                service_dic[service.name]={
                        'host_list':host_list,
                        'item_list':item_list,
                        #'trigger_list':trigger_list,
                        'trigger_dic':json.loads(trigger.expression),
                        'check_interval':service.check_interval
                    }
            except ObjectDoesNotExist,err:
                print 'not data %s' %(str(err))
    else:
        try:
            #service=services.objects.get(name=ser_name)
            item_list=serv.item_list.all()
            #trigger_list=serv.trigger_list.all()
            trigger = triggers.objects.get(name=serv.trigger)
            service_dic[serv.name]={
                    'item_list':item_list,
                    #'trigger_list':trigger_list,
                    'trigger_dic':json.loads(trigger.expression),
                    'check_interval':serv.check_interval
                }
        except ObjectDoesNotExist,err:
            print '%s error' %(err)
        finally:
            pass
    return service_dic

    
    
def get_monitor_host_list():
    host_dic = {}
    try: 
        for n,p in enumerate(templates.enabled_templates):
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
        return host_dic
    except  ObjectDoesNotExist,err:
        print 'get_monitor_dic.py:',err

        
if __name__=='__main__':
    '''
    host_monitor_dic=get_all_host_monitor_dic('10.168.0.218')
    print host_monitor_dic
    for h_k in host_monitor_dic.keys():
        one_host_dic=host_monitor_dic[h_k]
        
        if len(one_host_dic['service']):
            for k,service in enumerate(one_host_dic['service']):
                print k,service['name'],service['check_interval']
        else:
            print 'host has no service...'
    '''
    #a,b=get_all_template_dic()
    #serv_dic=get_service_dic()
    #print serv_dic
    #print get_monitor_empty_dic('10.168.0.218')
    print get_all_host_monitor_dic('192.168.1.115')
#print get_monitor_host_list()
