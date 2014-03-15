

def handle(name, alert_index, status_data):
	print '---------------->monitor name',name
	#print '\033[31;1m %s \033[0m' %  alert_index.index_dic
	#print '\033[32;1m %s \033[0m' %  status_data
	if name == 'memory':
		print status_data
		for n,index  in alert_index.index_dic.items():
			print n
			if index[0] is not None:
			  if index[0] != 'string':
				if int(status_data[n]) > index[2]: #cross critical limit
				
					print '\033[41;1mCritical....\033[0m', n, status_data[n],index[1]
				elif int(status_data[n]) > index[1]: # cross warning limit
					
					print '\033[43;1mWarining....\033[0m', n, status_data[n],index[1]
				else:
					
					print '\033[42;1mFine....\033[0m', n, status_data[n],index[1]
