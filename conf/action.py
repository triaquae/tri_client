#!/usr/bin/env python
severity = {
	'Unimportant' : {
		're_try': 5,
		'alert': ['record'],
		'recover_notice': False,
		'action': None , #['scriptName'],
		'escalate': [20, 'Warning'] #retry 20 times,then escalate to Critical level
		},
	'Warning':{
		're_try': 3,
                'alert': ['email'],
                'recover_notice': False,
                'action': None , 
                'escalate': [20, 'Critical'] 
		},
	'Critical':{
                're_try': 2,
                'alert': ['email','sms'],
                'recover_notice': True,
                'action': None,
                'escalate': [15, 'Urgent']
		},
	'Urgent': {
                're_try': 1,
                'alert': ['email','sms','wei_chat'],
                'recover_notice': True,
                'action': None ,
                'escalate': [10, 'Disaster']
		},
	'Disaster' : {
		're_try': 1,
                'alert': ['email','sms','wei_chat'],
                'recover_notice': True,
                'action': None ,
                'escalate': [10, 'Disaster']
		}
}

opreator = ['>','<', '=', 'contains', 'starts_with','in','btween']
obj ={
	'host' : ['=', 'contains', 'starts_with','in'], 
	'level ' : ['='],
	'group' :['=', 'contains', 'starts_with','in'],
	'service' : ['=']
	'template' : ['='],
	}

notifier = {
	alex
	rachel
	BJ_IDC_monitor_group
}
opreator = [> < = contains starts in ]

if host = 'localhost' and service  = 'cpu':
	action = 'Urgent' 

if host 



