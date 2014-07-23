m_list = ['127.0.0.1', '192.168.91.190', '192.168.2.240', '10.0.0.121', '10.0.0.135', '10.0.0.134', '10.0.0.132', '10.0.0.107', '10.0.0.139', '10.0.0.125']

m_dic = {
	'10.0.0.143': {
		'cpu' : [ 80, 90],
		'apache': [],
		'mysql': [],
		},

	'10.0.0.142': {
                'cpu' : [ 80, 90],
                'apache': [],
                'oracle': [],
                }	
}

monitor_api = {
	'memory': 'grep -E "MemTotal|MemFree|Cached|SwapTotal|SwapFree"  /proc/meminfo' , 
	'cpu' : 'sar 1 1|awk....'

}
