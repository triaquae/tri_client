#!/usr/bin/env python 
import service



class localhost:
	#hostname = 'localhost'
	services = {
		'ngnix': service.ngnix(),
	}
	alert_policy = None





monitored_hosts = {

	'localhost': localhost(),
	

}
