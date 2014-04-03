from get_monitor_dic import get_monitor_host_list
import json,time
from conf import policy, hosts
import redis_connector as redis

latest_status= json.loads(redis.r.get('TriAquae_monitor_status'))
for h,p_index_list in  get_monitor_host_list().items():
	if redis.r.get('STATUS_DATA::%s' % h.hostname) is None:
		print "no data in redis", h.hostname
		redis.r['STATUS_DATA::%s' % h.hostname] = json.dumps({})
	else:
		print redis.r.get('STATUS_DATA::%s' % h.hostname)
	STATUS_DATA = json.loads(redis.r.get('STATUS_DATA::%s' % h.hostname))
	print '\033[45;1m %s \033[0m ' % h.hostname	 
	for p_index in p_index_list:
		p = policy.enabled_policy[p_index]
		for service,obj in  p.services.items(): 
		  if STATUS_DATA.has_key(service):
			pass
		  else: # add serivce name into dic if it's not in there
			STATUS_DATA[service] = {}
			STATUS_DATA[service]['Actual'] = []
		  print service, obj.graph_index
		  for index_name in  obj.graph_index['index']: #graph list 
		    try:
		      #print index_name
		      index_value = latest_status[h.hostname][service][index_name] 
		      STATUS_DATA[service]['Actual'].append(index_value)
		    except KeyError:pass
	print STATUS_DATA
		    #except ValueError:pass
#print latest_status
		      
			
			

