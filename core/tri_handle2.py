#!/usr/bin/env python
# -*- coding:utf-8 -*-
import global_setting
import json,os,sys,threading
from conf import templates, hosts,conf
from get_monitor_dic import * #get_monitor_host_list,get_all_host_monitor_dic
import db_connector
from triWeb.models import Group,IP
import monitor_data_handle as alert_handle
import time,pickle,subprocess
import redis_connector
import socket
import key_gen,random_pass
import sys,trigger_formulas
from utils import pprint 
monitor_result_dic={}
server_ip = conf.server_ip
server_port = conf.server_port
#get all hosts' monitor configuration out from DB 
monitor_dic=  get_all_host_monitor_dic(server_ip)

#fetch latest status from redis
def pull_status_data():
    
    r=redis_connector.get_redis()
    monitor_status_dic = r.get('monitor_status_data')
    if monitor_status_dic is not None:
        monitor_status_dic = json.loads(monitor_status_dic)
        return monitor_status_dic
    else:
        return "No monitor data found in Redis,please check..."
    #if monitor_status_dic is none,we should return an empty dict,and write it into logs.

def push_status_data(host,port):
    try:
        #connect server let the status data into redis
        psh_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        psh_s.connect((host,port))
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        psh_s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        #print '\033[34;1m Pulling the latest monitor data from SocketServer......\033[0m'
        RSA_status=psh_s.recv(1024)
        if RSA_status == 'RSA_OK':
            psh_s.send('StatusDataIntoRedis')
            status=psh_s.recv(1024)
            print status
            if status == "StatusDataIntoRedis_OK":
                return pull_status_data()
            else:#error must happened. 
                pprint(status,'err',exit=1)
    except socket.error:
        pprint(socket.error, 'err',exit=1)
        #sys.exit("Socket connect error")
    finally:
        psh_s.close()

def trigger_condition_handle(formulas, data):
    '''formulas : trigger formula 
        data: monitor data of this service 
    '''
    #print '--->',formulas, data
    for formula in formulas:
        handle_func = getattr(trigger_formulas, formula['handler'] )
        formated_value = handle_func(formula['mintues'], data[formula['item_key']] )
        #print ':::::formated val;  key: %s   trigger_value: %s   val: %s ' %(formula['item_key'],formula['value'],formated_value )
        if formula['logic'] == 'AND':  
            if formula['operator'] == '>': 
                if float(formated_value) > float(formula['value']): 
                    #print '\033[31;1m:::Statisfied:   logic: AND , so Continue\033[0m', float(formated_value), formula['operator'], float(formula['value'] )
                    continue
                else: 
                    #print '\033[32;1m:::not Statisfied: logic: AND ,so break and got next level\033[0m' , formated_value, formula['operator'], formula['value']
                    break
                    
            elif formula['operator'] == '<': 
                if formula['operator'] == '<': 
                    if float(formated_value) < float(formula['value']): 
                        #print '\033[31;1m:::Statisfied:  logic: AND , so Continue \033[0m', float(formated_value), formula['operator'], float(formula['value'] )
                        continue
                    else: 
                        #print '\033[32;1m:::not Statisfied: logic: AND , break and got next level\033[0m' , formated_value, formula['operator'], formula['value']
                        break
                        
            elif formula['operator'] == '=' :
                pass 
                
        elif formula['logic'] == 'OR':
            print 'Pass OR right now ....' #pass
def trigger_handle(**kwargs):
    '''kwargs:  
    obj=  service configuration 
    service_data =  real monitored service data from client
    '''
    severity = ['Disaster', 'Urgent', 'Problem', 'Warning', 'Information'] 
    #print '\033[43;1m---trigger---\033[0m'  , kwargs
    if not kwargs.has_key('obj'):
        pprint('Lack of service configration data','err')
        return
    if not kwargs.has_key('service_data'):
        pprint('Lack of service data','err')
        return
    
    expression = json.loads(kwargs['obj'].trigger.expression)
    #print expression
    for s in severity:
        print '\033[35;1m%s\033[0m' %s
        print expression[s]
        #status and a level of alarm expression ------------work here
        '''
        logic_counter = 1
        for condition_item in expression[s]:
            #print '-------------------------------------Logic:',logic_counter
            print '\tMonitorValue: \033[32;1m%s\033[0m ' %kwargs['service_data'] 
            logic_counter +=1'''    
        #return a host and its service status and opt value ---------------work here
        
            
        #trigger_condition_handle(formulas=expression[s], data=kwargs['service_data'] )
 
server_ip,port  = server_ip,server_port
push_status_data(server_ip,port) 
latest_monitor_data = pull_status_data()
if isinstance(latest_monitor_data,dict):
    for h,value in monitor_dic.items():
        print '\033[42;1m %s \033[0m' %h
        #print value
        print "==============================aaaaaaa========================"
        if latest_monitor_data.has_key(h): #make sure host is in the lastest monitor data
            #loop each service in this host 
            for service_key, service_obj in value.items():
                #print "-----------------------ccccc--------------------"
                #print value
                #print '\033[41;1mservice_key:  %s  \033[0m check_interval: %s  trigger: %s '% ( service_key, service_obj.check_interval, service_obj.trigger)
                client_service_data = latest_monitor_data[h]['result_values'][service_key]
                #print '++++|||',client_service_data
                #check if this service links to any trigger
                if service_obj.trigger: 
                    #go through trigger expression first 
                    #print 'Trigger:', service_obj.trigger.expression
                    trigger_handle(obj= service_obj, service_data =client_service_data)
                    #print service_obj.trigger.name
                else: #if not trigger links , only store the data in redis
                    print 'no triiger for \033[31;1m%s\033[0m  will save this data to redis later' %service_key
                #print "-----------------------yyyyy---------------------"

        else: #no monitor data for this host , definitely something went wrong
            pprint("No monitor data for this host!" , 'err')
        print "===============================zzzzzzz========="
        break;
else:
    pprint('No ','err')
