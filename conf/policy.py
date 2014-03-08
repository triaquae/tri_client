#!/usr/bin/env python
import service

class Policy:
	name = None
	contact = 'it@admin.com'
	alert_policy = None
	groups = None
	hosts = None
	
	services = None
	"""
	tasks = []
	schedule = []
	
	def task(self):
		task_name = None
		
	def schedule(self):
		schedule_name = None
	"""

class defaultPolicy(Policy):
	name = 'TriaquaeDefaultPolicy'
	groups = ['BJ', 'TestGroup']
	hosts = ['localhost']
	services = {
		'cpu': service.cpu(),
		'memory':  service.memory()
	}
	#services = ['cpu','load','disk', 'memory',]


enabled_policy =( 
	defaultPolicy(),
	Policy()	
)

#print enabled_policy[0].services[0].index_dic
