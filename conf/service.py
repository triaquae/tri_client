

class DefaultService:
	name = 'DefaultService'
	interval = 300
	index_dic = None
	graph_index = None


class cpu(DefaultService):
	name = 'cpu'
	interval = 30
	index_dic = {
		'iowait': ['percentage', 80,90],
		'system': ['percentage', 80,90],
		'idle': ['percentage', 80,90],
		'user': ['percentage', 80,90],
		'steal': ['percentage', 80,90],
		'nice': [None, 80,90],
	}
	graph_index = ['iowait', 'system', 'idle', 'user']

class load(DefaultService):
        name = 'load'
        interval = 230
        index_dic = {
                'uptime': [None, 80,90],
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
	}
	graph_index = ['MemUsage','SwapUsage']


