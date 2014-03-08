

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


class memory(DefaultService):
	name = 'memory'
	index_dic = {
		'MemTotal': ['number', 1024, 512],
		'MemFree' : ['percentage', 80, 90],
		'Buffers' : ['percentage', 80, 90],
		'Cached' : ['percentage', 80, 90],
		'SwapTotal': ['percentage', 80, 90],
		'SwapFree': ['percentage', 80, 90],
	}
	graph_index = ['MemTotal', 'MemFree', 'Cached', 'SwapFree']


