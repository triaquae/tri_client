
import db_connector 

from triWeb.models import *


for h in IP.objects.filter(status_monitor_on=True):
	print h.hostname
	print h.template_list.values()
	

"""
for t in templates.objects.all():
	print t.name
	for s in t.service_list.values():
		print '\033[42;1m%s\033[0m' %s
		service_obj =  services.objects.get(name=s['name'])
		for item in  service_obj.item_list.values():
			print item
"""
