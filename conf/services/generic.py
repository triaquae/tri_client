
class DefaultService:
        name = 'DefaultService'
        interval = 300
        index_dic = None
	data_from = 'agent'
        graph_index = {
                'index' :[],
                'title' : name,
        }
        lt_operator = [] #if this sets to empty,all the status will be caculated in > mode , gt = > 

class upCheck(DefaultService):
        name = 'host status'
        interval = 30
        triggers= {
                'host_status' : [None],
        }
