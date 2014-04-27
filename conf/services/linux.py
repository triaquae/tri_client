from generic import DefaultService

class ngnix(DefaultService):
	name = "Ngnix status"
	interval = 30
	triggers ={
		'alive': [int , 1]
	} 
class cpu(DefaultService):
	name = 'cpu'
	interval = 30 
	triggers = {
		'iowait': ['percentage', 5.5,90],
		'system': ['percentage', 5,90],
		'idle': ['percentage', 20,10], 
		'user': ['percentage', 80,90],
		'steal': ['percentage', 80,90],
		'nice': [None, 80,90],
	}
	graph_index ={
		'index' :['iowait','system','idle','user'], 
		'title' :'CPU usage',
		}
	lt_operator = ['idle']
class load(DefaultService):
        name = 'load'
        interval = 300
        triggers = {
                'uptime': ['string', 'd',90],
                #'ptime': ['string', 'd',90],
                'load1': [int, 4,9],
                'load5': [int, 3,7],
                'load15': [int, 3,9],
        }
        graph_index = {
		'index':['load1', 'load5', 'load15'],
		 'title': 'Load status' ,
	}
class memory(DefaultService):
	name = 'memory'
	triggers = {
		'SwapUsage_p':['percentage', 66, 91],
		'MemUsage_p': ['percentage', 68, 92],
		'MemUsage': [None, 60, 65],
	}
	graph_index = {
		'index': ['MemUsage','SwapUsage'],
		
	}

