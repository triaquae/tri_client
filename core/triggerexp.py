#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json


triggerexp_dic={'Information':[],
                'Warning':[{'item_key':'iowait','operator':'>','value':'80','logic':"||"},{'item_key':'idle','operator':'<','value':'60','logic':None}],
                'Critical':[{'item_key':'iowait','operator':'>','value':'90','logic':"||"},{'item_key':'idle','operator':'<','value':'30','logic':None}],
                'Urgent':[{'item_key':'iowait','operator':'>','value':'95','logic':"&"},{'item_key':'idle','operator':'<','value':'20','logic':None}],
                'Disaster':[{'item_key':'iowait','operator':'>','value':'99','logic':"&"},{'item_key':'idle','operator':'<','value':'10','logic':None}]
               }
               
memtrigger_dic={
                'Information':[],
                'Warning':[{'item_key':'mem_free','operator':'<','value':'30','logic':'||'},{'item_key':'mem_usage','operator':'>','value':'70','logic':None}],
                'Critical':[{'item_key':'mem_free','operator':'<','value':'15','logic':'||'},{'item_key':'mem_usage','operator':'>','value':'85','logic':None}],
                'Urgent':[],
                'Disaster':[{'item_key':'mem_free','operator':'<','value':'10','logic':'&'},{'item_key':'mem_usage','operator':'<','value':'90','logic':None}]
}
                
print json.dumps(triggerexp_dic)
print json.dumps(memtrigger_dic)

if eval(triggerexp_dic['Warning']['value'] + triggerexp_dic['Warning']['operator'] + '85'):
    print 1
else:
    print 2
                
               
#得到trigger表达式字典
'''
def get_trigger_exp(service='',exp_dic={}):
    exp_dic
    if service == "CPU":
        pass
    elif service =="MEM":
        pass
    elif service == "SystemInfo":
        
        triggerexp_dic={
            'Information':[],
            'Warning':[],
            'Critical':[],
            'Urgent':[],
            'Disaster':[]
        }
    else:
        pass
        
'''


'''
#得到某段时间的平均值
def avg(itime=5):
    pass
    
#某段时间内是否变化
def change(itime=0):
    pass

def diff(itime=0):
    pass

def last(itime=0)
    pass

def max(itime=#3)
    pass

def min(itime=10)
    pass

def nodata(itime=10)
    pass
'''    



    
    



