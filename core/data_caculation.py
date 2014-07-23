
#a=[[1396766780.617834, "0.00", "0.67", "99.33", "0.00"], [1396766838.235313, "0.00", "0.84", "96.79", "2.36"], [1396766943.867216, "0.00", "0.67", "96.96", "2.36"], [1396868395.640945, "0.00", "0.51", "97.31", "2.19"]]


def convert_to_float(status):
        status_list = [float(x ) for x in status[1:]]
	return status_list

def get_average(source_data):
	data_list=map(convert_to_float, source_data)
	total_value = [0 for i in range(len(data_list[0])) ] #initialize total value list
	for i in data_list:
	  for index,n in enumerate(i):
		total_value[index] += n


	avg = [round(x/len(data_list),2)  for x in  total_value ] 
	return avg


#print get_average(a)
