import time
import json


def handle(name, alert_index, status_data, redis_obj):
	host_status_dic = {}
	print redis_obj
	#print '---------------->monitor name',name,alert_index.interval, status_data['last_check']
	time_diff = time.time() - status_data['last_check'] 
	if time_diff < alert_index.interval:  # service works fine
		#print status_data
		for n,index  in alert_index.index_dic.items(): #n stands for indicator name
		  if index[0] is not None:
			if n not in alert_index.lt_operator : #use > gt mode  
			  print status_data[n]
			  if index[0] != 'string':
				if float(status_data[n]) > index[2]: #cross critical limit
				
					print '\033[41;1mCritical....\033[0m', n, status_data[n],'critical limit:',index[2]
				elif float(status_data[n]) > index[1]: # cross warning limit
					
					print '\033[43;1mWarining....\033[0m', n, status_data[n],'warning limit:',index[1]
				else:
					
					print '\033[42;1mFine....\033[0m', n, status_data[n], 'warining limit:' ,index[1]
			  else: #string
				if status_data[n] == index[2]:
					print "\033[42;1mString equal...\033[0m", status_data[n], index[1]
				else:
					print '\033[43;1mWarining String unequal....\033[0m',status_data[n], index[1]
			else: #lt_operator use < lt mode
                          if index[0] != 'string':
                                if float(status_data[n]) < index[2]: #cross critical limit

                                        print '\033[41;1mCritical....\033[0m', n, status_data[n],'critical limit:',index[2]
                                elif float(status_data[n]) < index[1]: # cross warning limit

                                        print '\033[43;1mWarining....\033[0m', n, status_data[n],'warning limit:',index[1]
                                else:

                                        print '\033[42;1mFine....\033[0m', n, status_data[n], 'warining limit:' ,index[1]
                          else: #string
                                if status_data[n] == index[2]:
                                        print "\033[42;1mString equal...\033[0m", status_data[n], index[1]
                                else:
                                        print '\033[43;1mWarining String unequal....\033[0m',status_data[n], index[1]
		  else: #None ,will not alert
			print '\033[47;1mWill not Alert...\033[0m', n, status_data[n] 
		  print n, index,'----------->',status_data[n]
	else: #service down
		print "\033[31;1mToo long since last time receive the message from client by Sec\033[0m" ,name,  time_diff 
