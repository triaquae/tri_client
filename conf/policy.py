#!/usr/bin/env python
import service

class Policy:
	name = None
	contact = 'it@admin.com'
	alert_policy = None
	groups = None
	hosts = None
	
	services = None

class defaultPolicy(Policy):
	name = 'TriaquaeDefaultPolicy'
	groups = ['TestGroup',]
	hosts = ['localhost','www.baidu.com']
	services = {
		'cpu': service.cpu(),
		'memory':  service.memory(),
		'load':  service.load(),
		'upCheck': service.upCheck(),
	}
	#services = ['cpu','load','disk', 'memory',]

class TestPolicy(Policy):
        name = 'testPl'
        #groups = ['BJ']
        hosts = ['localhost','www.baidu.com']
        services = {
                'load': service.load(),
		'memory':  service.memory(),
		'cpu': service.cpu(),
        }


enabled_policy =( 
	defaultPolicy(),
	#TestPolicy(),
)

#print enabled_policy[0].services[0].index_dic
