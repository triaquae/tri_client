from get_monitor_dic import get_monitor_host_list
import json,time
from conf import templates, hosts
import redis_connector as redis
from graph import data_storage_interval
import data_caculation

def status_data_collection():
	latest_status= json.loads(redis.r.get('TriAquae_monitor_status'))
	for h,p_index_list in  get_monitor_host_list().items():
		if redis.r.get('STATUS_DATA::%s' % h.hostname) is None:
			print "no data in redis", h.hostname
			redis.r['STATUS_DATA::%s' % h.hostname] = json.dumps({})
		else:
			pass #print redis.r.get('STATUS_DATA::%s' % h.hostname)
		STATUS_DATA = json.loads(redis.r.get('STATUS_DATA::%s' % h.hostname))
		print '\033[45;1m %s \033[0m ' % h.hostname	 
		for p_index in p_index_list:   #template index list for each host 
		  p = templates.enabled_templates[p_index]
		  for service,obj in  p.services.items(): 
			  if latest_status[h.hostname].has_key(service): # data available from client 
				last_check_stamp = latest_status[h.hostname][service]['last_check']
			  else:
				last_check_stamp = None
			  if STATUS_DATA.has_key(service): #check whether this monitor index has historical data
				#get the last check status data
				last_time_in_db =  STATUS_DATA[service]['Actual'][-1][0] 
				if last_check_stamp is not None:
					if last_check_stamp == last_time_in_db : #minimum 10 s interval
						print '\033[32;1mduplicate point......\033[0m', service, h.hostname
						continue
					else:
						STATUS_DATA[service]['Actual'].append( [last_check_stamp] )
				else:continue #skip below part	
			  else: # add serivce name into dic if it's not in there
				STATUS_DATA[service] = {}
				STATUS_DATA[service]['Actual'] = [[last_check_stamp ] ]
				STATUS_DATA[service]['last_check_index_dic'] = {} # save the end data point of each data set 
				for dataset_name,interval in data_storage_interval.items(): 
					STATUS_DATA[service][dataset_name] = [[last_check_stamp] ]
					STATUS_DATA[service]['last_check_index_dic'][dataset_name] = 0
			  for index_name in  obj.graph_index['index']: #graph list 
			    try:
			      print index_name,'line will be draw...........'
			      index_value = latest_status[h.hostname][service][index_name] 
			      STATUS_DATA[service]['Actual'][-1].append(index_value)
			      current_time_stamp = time.time()
			      for dataset_name,interval in data_storage_interval.items():
				last_point_time = STATUS_DATA[service][dataset_name][-1][0]
				if current_time_stamp - last_point_time < interval[0]:  #interval[0] is the step,interval[1] is max point limit
					pass #print "\033[43;1m not hitting the interval yet\033[0m", dataset_name
				else: #hitting the periodic inverval 
					period_start_index = STATUS_DATA[service]['last_check_index_dic'][dataset_name]  
					if len( STATUS_DATA[service]['Actual'][period_start_index:] ) > 0: #has new data since last data collection	
						#print '-------->>>',STATUS_DATA[service]['Actual'][period_start_index:] #get index list starts from last slice end point
						average_data = data_caculation.get_average(STATUS_DATA[service]['Actual'][period_start_index:])
						print "\033[41;1mAverage:\033[0m", average_data
						average_list = [time.time()]
						average_list.extend(average_data)
						STATUS_DATA[service][dataset_name ].append(  average_list  )
						print STATUS_DATA[service][dataset_name ]
						#set new period start index
						new_period_start_index = len(STATUS_DATA[service]['Actual']) 
						STATUS_DATA[service]['last_check_index_dic'][dataset_name] = new_period_start_index 
						
					else:
						print "hit the interval but not new data since last point, what's wrong?"
					print '\033[42;1m ---->hitting hte interval ...\033[0m', dataset_name
			    except KeyError:pass
		redis.r['STATUS_DATA::%s' % h.hostname] = json.dumps(STATUS_DATA)
		for n,v in STATUS_DATA.items():
			print "\033[42;1m %s \033[0m" %n, STATUS_DATA[n]["last_check_index_dic"]
			#for i in v['Actual']:
			for i,data in v.items():
				if len(data) > 1 and  i != "last_check_index_dic":
				  print i,"---------->start date------>", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data[0][0] )) 
				  for d in data[-10:]:
					print '\t',d, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(d[0] ))
				else:
					pass #print i,data
			      

while True:	
	status_data_collection()
	time.sleep(10)
