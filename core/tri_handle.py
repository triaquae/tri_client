#!/usr/bin/env python
# -*- coding:utf-8 -*-
import global_setting
import json,os,sys,threading
from conf import templates, hosts
from get_monitor_dic import get_monitor_host_list,get_all_host_monitor_dic
import db_connector
from triWeb.models import Group,IP
import monitor_data_handle as alert_handle
import time,pickle,subprocess
import redis_connector
import socket
import key_gen,random_pass
import sys

monitor_result_dic={}

def pull_status_data():
    #pull out status data from Redis
    monitor_status_dic = redis_connector.r.get('monitor_status_data')
    #取到到清除该数据
    #redis_connector.r.delete('monitor_status_data')
    if monitor_status_dic is not None:
        monitor_status_dic = json.loads(monitor_status_dic)
        return monitor_status_dic
    else:
        return "No monitor data found in Redis,please check..."
        #sys.exit("No monitor data found in Redis,please check")

def push_status_data(host,port):
    try:
        #connect server let the status data into redis
        psh_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        psh_s.connect((host,port))
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        psh_s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print '\033[34;1m sending status to Monitor server .... \033[0m' 
        #判断RSA认证结果
        RSA_status=psh_s.recv(1024)
        if RSA_status == 'RSA_OK':
            psh_s.send('StatusDataIntoRedis')
            status=psh_s.recv(1024)
            if status == "StatusDataIntoRedis_OK":
                return pull_status_data()
            else:
                pass
    except socket.error:
        print socket.error
        sys.exit("socket connect error")
    finally:
        psh_s.close()

#通过templat模板来处理，每个模板具有的服务和主机与监控状态进行比较。如果存在主机单独与服务的关系，另作比较        
template_dic,custom_monitor_list=get_all_template_dic() 
def service_handle(status_dic,template_dic,custom_monitor_list=None):
    alert_dic={}
    #1处理模板中的主机服务项
    for k,v in template_dic.items():
        monitor_host_list = set(v['host_list'])
        for monitor_host in set(v['host_list']):
            if status_dic.has_key(monitor_host):
                for service in v['template'].service_list.values():
                    if status_dic[monitor_host]['result_values'].has_key(service['name']):
                        try:
                            s = alert_handle.service_handle(service,  status_dic[monitor_host]['result_values'][service['name']] )
                            if len(s) !=0:
                                alert_list.append(s)
                        except KeyError:
                            alert_list.append({"NoValidServiceData":(service,"service not exist in client data")} )
                    else:
                        pass
                '''
                if len(monitor_host.custom_services.values()):
                    for custom_service in monitor_host.custom_services.values():
                        if status_dic[monitor_host]['result_values'].has_key(custom_service['name']):
                            try:
                                s = alert_handle.service_handle(custom_service,  status_dic[monitor_host]['result_values'][custom_service['name']] )
                                if len(s) !=0:
                                    alert_list.append(s)
                            except KeyError:
                                alert_list.append({"NoValidServiceData":(custom_service,"service not exist in client data")} )
                        else:
                            pass
                '''
            else:
                print 'host not in this template'
    
    #2处理一般服务项
    if custom_monitor_list is not None:
        for custom_host in custom_monitor_list():
            if status_dic.has_key(monitor_host):
                for service in custom_host.custom_services.values():
                    if status_dic[monitor_host]['result_values'].has_key(service['name']):
                        try:
                            s = alert_handle.service_handle(service,  status_dic[monitor_host]['result_values'][service['name']] )
                            if len(s) !=0:
                                alert_list.append(s)
                        except KeyError:
                            alert_list.append({"NoValidServiceData":(service,"service not exist in client data")} )
                    else:
                        pass
            else:
                print 'host not custom service'
    
        
#数据处理:1是否存在该主机，2该主机的服务项是否为空，3是否能得到服务项结果，4处理具体服务项
def status_handler(status_dic,host_dic):
    alert_dic={}
    #if host_dic.has_key(status_dic[])
    #解析处理主机监控字典，分析状态字典的内容
    for h_k in host_dic.keys():
        alert_list=[]
        one_host_dic=host_dic[h_k]
        #1分析某台主机的是否返回了结果数据
        if status_dic.has_key(one_host_dic['hostname']):
            if len(one_host_dic['service']):
                if len(status_dic[h_k]['result_values']):
                    #得到服务项的监控间隔
                    for k,service in enumerate(one_host_dic['service']):
                        print k,service['name'],service['check_interval']
                        if status_dic[h_k]['result_values'].has_key(service['name']):
                            #主机存在该监控服务项，用一个.py具体处理
                            try:
                                s = alert_handle.service_handle(service,  status_dic[h_k]['result_values'][service['name']] )
                                if len(s) !=0:
                                    alert_list.append(s)
                            except KeyError:
                                alert_list.append({"NoValidServiceData":(service,"service not exist in client data")} )
                        else:
                            alert_list.append({"NoValidServiceData":(service['name'],"service not exist in client data")} )
                else:
                    alert_list.append('host: %s has no get result data'%(one_host_dic['hostname']))
            else:
                print '%s host has no service....'%(h_k)
        else:
            alert_list.append('host: %s has no monitoring...'%(one_host_dic['hostname']))
            print 'host: %s has no monitoring...'%(one_host_dic['hostname'])
        
        #2分析需要得到监控状态的信息
        '''
        if len(one_host_dic['service']):
            if status_dic.has_key(one_host_dic['hostname']): 
            for k,service in enumerate(one_host_dic['service'])：
                print k,service['name'],service['check_interval']
        else:
            print '%s host has no service....'%(h_k)
        '''
        alert_dic[h_k]=alert_list
    alert_dic['TimeStamp'] = time.time()
    redis_connector.r['TempTriAquaeAlertList'] = json.dumps(alert_dic)
    #一个处理监控项中是否有该结果信息，
    #另一个是处理在规定的时间间隔中，某主机的监控信息是否返回
            
#host_list = set(host_list)
def data_handler(host_dic):
    graph_dic = {}
    alert_dic = {}
    for h,p_index_list in  host_dic.items():  #p_index stands for templates.index in enabled_templates.list 
        alert_list = []
        graph_dic[h.hostname] = [] #initialize the list
        for p_index in set(p_index_list):
            p = templates.enabled_templates[p_index] #find this host belongs to which template
            if monitor_dic.has_key(h.hostname): #host needs to be monitored
                if len(monitor_dic[h.hostname]) == 0: 
                    alert_list.append({"ServerDown":"No data received from client,is the agent or the host down"} )
                    #print "\033[31;1mno data from client, is it done?\033[0m",h.hostname
                    break
                else: 
                    print "\033[46;1m%s\033[0m" % h.hostname
                    for service,alert_index in p.services.items():
                        try:
                            s = alert_handle.handle(service,alert_index,  monitor_dic[h.hostname][service])
                            if len(s) !=0:
                                alert_list.append(s)
                        except KeyError:
                            alert_list.append({"NoValidServiceData":(service,"service not exist in client data")} )
                    
            else: #host not in database or not enalbed for monitoring
                print "\033[34;1mnot going to monitor server:\033[0m", h.hostname
        if hosts.monitored_hosts.has_key(h.hostname):
            customized_templates= hosts.monitored_hosts[h.hostname]
            #print "*"*50,'Customized'#,customized_templates.services
            for service,alert_index in customized_templates.services.items():
                try:
                    s = alert_handle.handle(service,alert_index,  monitor_dic[h.hostname][service])
                    if len(s) !=0:alert_list.append(s)
                except KeyError:
                    alert_list.append({"NoValidServiceData":(service,"service not exist in client data")} )
        #else:
        #print 'no customized templates.,h
    alert_dic[h.hostname] = alert_list
    #print '\033[41;1m*\033[0m'*50,'ALert LIST\n'
    #for host,alerts in  alert_dic.items():
    #   print '\033[31;1m%s\033[0m' %host
    #   for msg in  alerts:print msg #for i in alerts:print i
    alert_dic['TimeStamp'] = time.time()
    redis_connector.r['TempTriAquaeAlertList'] = json.dumps(alert_dic)
    #print '\033[42;1m graph list ----------\033[0m\n'
    #for h,g in graph_dic.items():
    #   print h
    #   if len(g) >0:
    #   for s in  g:
    #       print s

def multi_job(m_dic):
    def run(name):
        print 'going to run job......',name
    threading.Thread(target=run, args=(m_dic,)).start()

'''
def test():
    a=10
    if not a:
        return a
    else:
        print a
aa=test()
    if aa is None:
        print "not return values"
    else:print aa
'''
time_counter = time.time()
#从数据库得到监控的字典信息，用来检测返回结果信息的正确性
host_monitor_dic = get_all_host_monitor_dic()
#将结果数据字典改为全局的，这样可以方便比较超时没有接受数据
monitor_status_dic={}
counter = 0
host='10.168.0.218'
post=9998
while True:
    #if time.time() - time_counter > 60: #refresh monitor list every 60 sec
        #print '------------------------------------------------------------------->'
        #del sys.modules['conf.templates.]
        #reload(templates.service) 
        #monitor_list = get_monitor_host_list()
        #time_counter = time.time()
    monitor_status_dic=push_status_data(host,post)
    if monitor_status_dic is not None:
        if len(monitor_status_dic) and type(monitor_status_dic) is dict:
            for k in monitor_status_dic.keys():
                print '\033[34;1mone_result:\033[0m',monitor_status_dic[k]
            #status_handler(monitor_status_dic,host_monitor_dic)
        else:
            print 'result status data is null...'
    else:
        print 'no get back result status data...'
    #monitor_status_dic = pull_status_data()
    #print monitor_status_dic
    #data_handler( monitor_list )
    print '\033[42;1m-----Alert Checking Executed...>>>>\033[0m' ,counter
    counter += 1
    #p = subprocess.Popen('python /home/alex/tri_client/status_data_optimzation.py', stdout=subprocess.PIPE, shell=True)
    #print monitor_list
    time.sleep(10)
