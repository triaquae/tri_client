#/usr/bin/python
# -*- coding:utf-8 -*-
import time
import json
from get_monitor_dic import *
from triWeb.models import *

#service为监控服务项对象，status_data为每个服务项结果状态字典
def service_handle(service, status_data ):
    host_alert_dic ={}
    time_diff = time.time()-status_data['last_check']
    if time_diff <=service['check_interval']:
        #print status_data
        #这里处理服务具有的监控项信息，和报警信息。
        #item_list=service.item_list.objects.filter(enabled=True)
        #trigger_list=service.trigger_list.objects.all()
        serv_dic=get_service_dic(service)
        '''
        #这里应该是一个item对应0/1个trigger，不应该是service对应trigger_list
        for k,item in item_list:
            trigger =item.objects.get('trigger')
            if trigger:
                #得到监控项的状态信息；进行比较
                pass
        '''
        #如果一个trrigger对应需要多个items怎么办？
        ####通过trrigger表达式来分析需要什么监控项状态信息
        #一个trigger有多个items
        for k,trigger in enumerate(serv_dic['trigger_list']):
            #分析expression的格式
            trigger['expression'].find("()")
            item_key=trigger['expression'].strip().split(".")[:-1]
            fun_attr=trigger['expression'].strip().split(".")[-1]
            fun=getattr('filename',fun_attr)
            for k,v in status_data.items():
                if item_key == k:
                    #通过函数计算，得到的结果状态
                    status=fun(v)
                    if status:pass
                    else:
                        host_alert_dic[service['name']]='%s problem is %s'%(service['name'],trigger['Description'])
                        
    else:
        host_alert_dic[service['name']]='LostConnectionWarining',service['name'],service['check_interval'],time_diff 
    
def handle(name, alert_index, status_data ):
    host_status_dic = {}
    #print '---------------->monitor name',name,alert_index.interval, time.time() - status_data['last_check']
    time_diff = time.time() - status_data['last_check'] 
    if time_diff < alert_index.interval:  # service works fine
        #print status_data
        for n,index  in alert_index.triggers.items(): #n stands for indicator name
            if index[0] is not None:
                if index[0] != 'string':  
                    if n not in alert_index.lt_operator : #use > gt mode  
                        if float(status_data[n]) > index[2]: #cross critical limit
                            msg= 'CriticalLimit',n, status_data[n],index[2]
                            host_status_dic[n] = msg
                        elif float(status_data[n]) > index[1]: # cross warning limit
                            msg= 'WarningLimit',n, status_data[n],index[1]
                            host_status_dic[n] = msg
                        else:
                            pass
                    #print '\033[42;1mFine....\033[0m', n, status_data[n], 'warining limit:' ,index[1]
                    else: #lt_operator use < lt mode
                        if float(status_data[n]) < index[2]: #cross critical limit
                            #print '\033[41;1mCritical....\033[0m', n, status_data[n],'critical limit:',index[2]
                            msg= "CriticalLimit", n, status_data[n],index[2]
                            host_status_dic[n] = msg
                        elif float(status_data[n]) < index[1]: # cross warning limit
                            msg="WariningLimit", n, status_data[n],index[1]
                            host_status_dic[n] = msg
                        else:
                            pass
                        #print '\033[42;1mFine....\033[0m', n, status_data[n], 'warining limit:' ,index[1]
                else: #string
                    if status_data[n] == index[2]:
                        print "\033[42;1mString equal...\033[0m", status_data[n], index[1]
                    else:
                        msg = "ValueDifferenceAlert", status_data[n], index[1]
                        host_status_dic[n] = msg
                    #print '\033[43;1mWarining String unequal....\033[0m',status_data[n], index[1]
            else: #None ,will not alert
                pass
                #print '\033[47;1mWill not Alert...\033[0m', n, status_data[n] 
            #print n, index,'----------->',status_data[n]
    else: #service down
        #msg="\033[31;1mClient back to normal,lost connection for  Sec\033[0m" ,name,  time_diff 
        msg=name, time_diff 
        host_status_dic[name] = 'LostConnectionWarining',name,time_diff,alert_index.interval
    return host_status_dic
