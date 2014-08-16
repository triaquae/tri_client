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
#get all hosts' monitor configuration out from DB 
monitor_dic=  get_all_host_monitor_dic('192.168.1.130')

print '----------->', monitor_dic
#获取redis中的数据
def pull_status_data():
    #pull out status data from Redis
    #monitor_status_dic = redis_connector.r.get('monitor_status_data')
    r=redis_connector.get_redis()
    monitor_status_dic = r.get('monitor_status_data')
    #取到到清除该数据
    #redis_connector.r.delete('monitor_status_data')
    if monitor_status_dic is not None:
        monitor_status_dic = json.loads(monitor_status_dic)
        return monitor_status_dic
    else:
        return "No monitor data found in Redis,please check..."
        #sys.exit("No monitor data found in Redis,please check")

#通知server/proxy_server端将状态数据存入到本地redis中，并获取redis中的状态数据
def push_status_data(host,port):
    try:
        #connect server let the status data into redis
        psh_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        psh_s.connect((host,port))
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        psh_s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print '\033[34;1m Pulling the latest monitor data from SocketServer......\033[0m'
        #判断RSA认证结果
        RSA_status=psh_s.recv(1024)
        if RSA_status == 'RSA_OK':
            psh_s.send('StatusDataIntoRedis')
            status=psh_s.recv(1024)
            if status == "StatusDataIntoRedis_OK":
                return pull_status_data()
            else:#error must happened. 
                pprint(status,'err',exit=1)
    except socket.error:
        
        pprint(socket.error, 'err',exit=1)
        
        #sys.exit("Socket connect error")
    finally:
        psh_s.close()

#处理具体的每一个服务，最终返回一个Severity状态
def trigger_condition_handle(formulas, data):
    '''formulas : trigger formula 
        data: monitor data of this service 
    '''
    #print '--->',formulas, data
    for formula in formulas:
        #先判断handler方法，然后判断operator 
        handle_func = getattr(trigger_formulas, formula['handler'] )
        formated_value = handle_func(formula['mintues'], data[formula['item_key']] )
        print ':::::formated val;  key: %s   trigger_value: %s   val: %s ' %(formula['item_key'],formula['value'],formated_value )
        if formula['logic'] == 'AND':  #跟下一条的关系
            #确定operator 
            if formula['operator'] == '>': #按大于处理
                if float(formated_value) > float(formula['value']): #满足条件, 因为是AND，这条满足了，跳到下一条  #代表超过阀值
                    print '\033[31;1m:::Statisfied:   logic: AND , so Continue\033[0m', float(formated_value), formula['operator'], float(formula['value'] )
                    continue
                else: #不满足，直接跳出并设定 问题为这个级别就好了
                    print '\033[32;1m:::not Statisfied: logic: AND ,so break and got next level\033[0m' , formated_value, formula['operator'], formula['value']
                    break
                    
            elif formula['operator'] == '<': #按小于处理
                if formula['operator'] == '<': #按大于处理
                    if float(formated_value) < float(formula['value']): #满足条件, 因为是AND，这条满足了，跳到下一条
                        print '\033[31;1m:::Statisfied:  logic: AND , so Continue \033[0m', float(formated_value), formula['operator'], float(formula['value'] )
                        continue
                    else: #不满足，直接跳出并设定 问题为这个级别就好了
                        print '\033[32;1m:::not Statisfied: logic: AND , break and got next level\033[0m' , formated_value, formula['operator'], formula['value']
                        break
                        
            elif formula['operator'] == '=' :
                pass 
                
        elif formula['logic'] == 'OR':
            print 'Pass OR right now ....' #pass
def trigger_handle(**kargs):
    '''kargs:  
    obj=  service configuration 
    service_data =  real monitored service data from client
    '''
    severity = ['Disaster', 'Urgent', 'Problem', 'Warning', 'Information'] 
    #print '\033[43;1m---trigger---\033[0m'  , kargs
    if not kargs.has_key('obj'):pprint('Lack of service configration data','err')
    if not kargs.has_key('service_data'):pprint('Lack of service data','err')
    
    expression = json.loads(kargs['obj'].trigger.expression)
    
    print kargs['service_data']
    
    #按severity顺序循环trigger字典，
    for s in severity:
        print '\033[35;1m%s\033[0m' %s , expression[s]
        #循环每个 级别 的 condition列表
        
        logic_counter = 1
        for condition_item in expression[s]:
            #循环每个condition_item
            
            print '-------------------------------------Logic:',logic_counter
            
            for k,v in condition_item.items():
                print '\t', k, ':', v
                #先获取监控数据值，然后按照handler 和operator 方式处理
                if k == 'item_key':
                    print '\tMonitorValue: \033[32;1m%s\033[0m ' %kargs['service_data'].get(v)
                
            logic_counter +=1
        #直接把一个级别的公式传给trigger_condition_handle 处理
        trigger_condition_handle(formulas=expression[s], data=kargs['service_data'] )
    #for k,v in expression.items():
    #    print k,v
    #
    #print '--------------------------in looop --------------'
    """for s in severity:
        #print '\033[41;1m ---%s ----\033[0m'%s 

        #'Warning':[{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
        for key,conditions in expression.items():#loop each trigger list 
            print '--$-->',key ,conditions
            
            
            #print '--------------------------in looop --------------2'
            for exp_line in conditions: #loop condition list in each severity
                #get item value handler first
                this_loop_satisfied  = True 
                last_loop_satisfied = True 
                relation_with_last = 'OR'
                #print '--------------------------in looop --------------4'
                for exp in exp_line:
                    #print '----->',exp 
                    value_handler = exp['handler']
                    
                    operator = exp['operator']
                    relation_with_next_one = exp['logic']
                    
                    mintues = exp.get('mintues')
                    value = exp.get('value')
                    
                    print '\033[34;1m EXP: \033[0m', value_handler,mintues,  operator,  value, relation_with_next_one
                    
                    if relation_with_last is not None:
                        
                        if relation_with_last == 'OR': # so last_loop_satisfied won't necessarily to be True
                            if last_loop_satisfied: #no need to carry on 
                                print 'Last loop has satisfied already ,will not go on ,continue'
                                
                                continue
                            else:
                                print 'OR: Last one did not work ,will test this loop again'
                            
                        elif relation_with_last == 'AND':
                            
                            if last_loop_satisfied: # last_loop_satisfied must be True
                                print 'AND: last one worked , will test this one '
                            else:
                                print 'AND: last one did not satisfied, break'
                                break
                        else:
                            print 'no match'
    """                

server_ip,port  = '192.168.1.130',9998
latest_monitor_data = push_status_data(server_ip, port)  #从redis中取出最新的监控数据

#print latest_monitor_data



if isinstance(latest_monitor_data,dict):
    #loop each host from DB 
    for h,value in monitor_dic.items():
        print '\033[42;1m %s \033[0m' %h
        #print value
        if latest_monitor_data.has_key(h): #make sure host is in the lastest monitor data
            #loop each service in this host 
            for service_key, service_obj in value['service'].items():
                print '\033[41;1mservice_key:  %s  \033[0m check_interval: %s  trigger: %s '%( service_key, service_obj.check_interval, service_obj.trigger)
                client_service_data = latest_monitor_data[h]['result_values'][service_key] #取出具体服务的最新监控数据
                #print '++++|||',client_service_data
                #check if this service links to any trigger
                if service_obj.trigger: 
                    #go through trigger expression first 
                    #print 'Trigger:', service_obj.trigger.expression 
                    # 交给trigger_handle 按trigger expression中的规则处理此服务的监控数据
                    trigger_handle(obj= service_obj, service_data =client_service_data )
                    #print service_obj.trigger.name
                else: #if not trigger links , only store the data in redis
                    print 'no triiger for \033[31;1m%s\033[0m  will save this data to redis later' %service_key

        else: #no monitor data for this host , definitely something went wrong
            pprint("No monitor data for this host!" , 'err')
else:
    pprint('No ')
