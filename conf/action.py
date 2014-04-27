#!/usr/bin/env python
severity = {
	'Unimportant' : [ record,1],
	'Information': [ record, 1],
	'Warning' : [ email,1 ,5 escalate],
	'Critical':[email, sms, 2,escalate],
	'Urgent': [email,sms, 1,escalate],
	'Disaster' : []
}

action_obj {
host 
Severity_type 
group
service
template
}

notifier = {
	alex
	rachel
	BJ_IDC_monitor_group
}
opreator = [> < = contains starts in ]

if host = 'localhost' and service  = 'cpu':
	action = 'Urgent' 





