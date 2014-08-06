#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json


triggerexp_dic={'Information':[],
                'Warning':[{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
                'Problem':[{'item_key':'iowait','operator':'>','value':'90','logic':"||",'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'30','logic':None,'handler': 'sum', 'mintues':10}],
                'Urgent':[{'item_key':'iowait','operator':'>','value':'95','logic':"&",'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'20','logic':None,'handler': 'sum', 'mintues':10}],
                'Disaster':[{'item_key':'iowait','operator':'>','value':'99','logic':"&",'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'10','logic':None,'handler': 'sum', 'mintues':10}]
               }
               
triggerexp_dic2 = {
    'Information':[],
    'Warning': [ 
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}]
             #每一条和下面那条都是else关系        
            ], 
    'Problem': [ 
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}]      
            ],     
    'Urgent': [ 
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}],
            [{'item_key':'iowait','operator':'>','value':'80','logic':"else", 'handler': 'sum', 'mintues':10},{'item_key':'idle','operator':'<','value':'60','logic':None,'handler': 'sum', 'mintues':10}]
            ],     
    'Disaster':[],


}               
memtrigger_dic2={
    'Information':[],
    'Warning': [],
    'Problem': [
            [{'item_key':'mem_free','operator':'<','value':'30','logic':'||','handler': 'avg', 'mintues':5},{'item_key':'mem_usage','operator':'>','value':'70','logic':None,'handler': 'avg', 'mintues':5}],
            [{'item_key':'mem_free','operator':'<','value':'30','logic':'||','handler': 'avg', 'mintues':5},{'item_key':'mem_usage','operator':'>','value':'70','logic':None,'handler': 'avg', 'mintues':5}]
    
        ],
    'Urgent':[],
    'Disaster':[
            [{'item_key':'mem_free','operator':'<','value':'10','logic':'&','handler': 'avg', 'mintues':5},{'item_key':'mem_usage','operator':'<','value':'90','logic':None,'handler': 'avg', 'mintues':5}]
            ]
}
memtrigger_dic={
                'Information':[],
                'Warning':[{'item_key':'MemFree','operator':'<','value':'30','logic':'||','handler': 'avg', 'mintues':5},{'item_key':'MemUsage','operator':'>','value':'70','logic':None,'handler': 'avg', 'mintues':5}],
                'Problem':[{'item_key':'MemFree','operator':'<','value':'15','logic':'else','handler': 'avg', 'mintues':5},{'item_key':'MemUsage','operator':'>','value':'85','logic':None,'handler': 'avg', 'mintues':5}],
                'Urgent':[],
                'Disaster':[{'item_key':'MemFree','operator':'<','value':'10','logic':'&','handler': 'avg', 'mintues':5},{'item_key':'MemUsage','operator':'<','value':'90','logic':None,'handler': 'avg', 'mintues':5}]
}
     
cputrigger_dic = {
    'Information': [],
    'Warning': [],
    'Problem':  [{'item_key':'idle','operator':'<','value':'15','logic':'AND','handler': 'avg', 'mintues':5},{'item_key':'iowait','operator':'>','value':'85','logic':'OR','handler': 'avg', 'mintues':5}, {'item_key':'system','operator':'>','value':'80','logic':None,'handler': 'avg', 'mintues':5}],
    'Urgent': [],
    'Disaster':[]
}
     
#print json.dumps(triggerexp_dic2)
print json.dumps(memtrigger_dic)
print json.dumps(cputrigger_dic)

"""if eval(triggerexp_dic['Warning']['value'] + triggerexp_dic['Warning']['operator'] + '85'):
    print 1
else:
    print 2
"""                
               
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
    
def sum(itime=10)
'''    



    
    



