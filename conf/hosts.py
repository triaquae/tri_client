#!/usr/bin/env python 
from services import linux



class localhost:
	#hostname = 'localhost'
	services = {
		'ngnix': linux.ngnix(),
	}
	alert_policy = None





monitored_hosts = {

	'localhost': localhost(),
	

}
