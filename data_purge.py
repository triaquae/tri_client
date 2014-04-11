#!/usr/bin/env python 
import graph,redis_connector,db_connector
import json

interval_dic = graph.data_storage_interval
host_dic =json.loads( redis_connector.r.get("TriAquae_monitor_status") )
def purge_host_status(hostname):
	h =redis_connector.r.get("STATUS_DATA::%s" %hostname) 
	if h is not None:
		h = json.loads(h)
		for service,value_dic in h.items():
			print service,'\n'
			
			for interval_name, (interval,max_point) in interval_dic.items():
				#print interval_name,len( value_dic[interval_name] ) 
				if len( value_dic[interval_name] ) - max_point > 0:
					purge_point = len( value_dic[interval_name] ) - max_point
					del value_dic[interval_dic][:purge_point]  #purge data from 0 to purge point
			if len(h[service]['Actual']) > graph.max_point:
				purge_point = len(h[service]['Actual']) - graph.max_point
				print 'points will be purged for actual list', purge_point
				del h[service]['Actual'][:purge_point]
		redis_connector.r["STATUS_DATA::%s" % hostname]	 = json.dumps(h)			

	else:
		#print 'nothing ', hostname
		return None	

for host in host_dic.keys():
	purge_host_status(host)


