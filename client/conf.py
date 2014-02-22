from services.models import *
import os,sys

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASE_DIR)
enabled_services = {
	'services' : (
		('httpd', apache()),
		('load', loadMonitor()),
		('cpu', cpuMonitor()),
		('memory', memoryMonitor()),
		),

}

#print cpuMonitor().script.monitor()
