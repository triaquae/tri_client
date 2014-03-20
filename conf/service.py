

class DefaultService:
	name = 'DefaultService'
	interval = 300
	index_dic = None
	graph_index = None
	lt_operator = [] #if this sets to empty,all the status will be caculated in > mode , gt = > 

class upCheck(DefaultService):
	name = 'host status'
	interval = 10
	index_dic = {
		'host_status' : [None],
	}
class cpu(DefaultService):
	name = 'cpu'
	interval = 30 
	index_dic = {
		'iowait': ['percentage', 5.5,90],
		'system': ['percentage', 5,90],
		'idle': ['percentage', 20,10], 
		'user': ['percentage', 80,90],
		'steal': ['percentage', 80,90],
		'nice': [None, 80,90],
	}
	graph_index ={
		'cpu usage' : {
			'iowait': ['iowait'], 
			'system': ['system'],
			'idle'  :['idle'], 
			'user' :['user'],
			},

		}
	lt_operator = ['idle']
class load(DefaultService):
        name = 'load'
        interval = 300
        index_dic = {
                'uptime': ['string', 'd',90],
                'load1': [int, 3,9],
                'load5': [int, 3,9],
                'load15': [int, 3,9],
        }
        graph_index = ['load1', 'load5', 'load15']

class memory(DefaultService):
	name = 'memory'
	index_dic = {
		'SwapUsage_p':['percentage', 80, 90],
		'MemUsage_p': ['percentage', 60, 65],
		'MemUsage': [None, 60, 65],
	}
	graph_index = ['MemUsage','SwapUsage']


