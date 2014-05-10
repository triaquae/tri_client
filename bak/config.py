from tasks import *
import sys
import db_connector

# assign  tasks to policy
policy = {
	'p1':[task1,task2],
	'p2':[task2, task3],
	}


# assign policy to specfic groups and hosts
enabled_policy = {
	'p1'     :{ 'group':['BJ','SHANG hai'],
		  'host' :['localhost'],
		  'exclude': [],
		},
	
	'p2'     :{'group':['HK IDC','BJ'],
		 'host': [],
		 'exclude': ['localhost'] , 
		}
}


h=db_connector.IP.objects.get(hostname=sys.argv[1])
group_list = [g['name'] for g in  h.group.values('name') ]
print 'host in group:',group_list
h_policy = []

for p_name,servers in enabled_policy.items():
	if servers.has_key('group'):
		for g in group_list:
			if g in servers['group']:h_policy.append(p_name)	

print 'host applies to policy:', set(h_policy)
'''
	if policy.has_key(p_name):
		print 'tasks',p_name
		for task in policy[p_name]:
			for k,v in task.items():
			   if k == job:
				for run_order, job  in task[job].items():
					print 'job order', run_order
					if job.has_key('script'):
						print 'script:', job['script']	
					if job.has_key('command'):	
						print 'command:',job['command'] 
					if job.has_key('run_user'):
						print 'run_user',job['run_user']	
			   if k ==  schedule:
				if schedule_list.has_key(v):
					print 'run job at',schedule_list[v]
				else:
					print 'invalid schedule name'
	else:
		print 'no this policy:',p_name	
	'''
