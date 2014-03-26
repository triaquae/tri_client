#!/usr/bin/env python 
import service



class localhost:
	#hostname = 'localhost'
	services = {
		'cpu': service.cpu(),
		'memory':  service.memory(),
		'load':  service.load(),
		'upCheck': service.upCheck(),
	}
	alert_policy = None





monitored_hosts = {

	'localhost': localhost(),
	

}
