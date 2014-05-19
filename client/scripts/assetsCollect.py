#!/usr/bin/env python 


import xml2json
import json,time
import subprocess,os.path

def monitor():
    shell_command = 'dxdiag /x d:\hard.xml'
    status = subprocess.call(shell_command,shell=True)

    time.sleep(5);

    if status != 0:
        value_dic = {'status':stauts}
    else:
    	if os.path.exists('d:\hard.xml'):
            asset_raw_data = file('d:\hard.xml').read()
            asset_to_json = xml2json.xml2json(asset_raw_data)
            asset_to_dict = json.loads(asset_to_json)
            value_dic = {
                    'asset':asset_to_dict,
                    'status':status
            }
        else:
        	value_dic = {'status':1}


    return value_dic

'''
asset_raw_data = file('hardinfor.txt').read()

asset_to_json = xml2json.xml2json(asset_raw_data)

asset_to_dict = json.loads(asset_to_json)


for k,v in asset_to_dict['DxDiag'].items():
	print '\033[42;1m--- %s----\033[0m' % k
	"""
	for name,info in v.items():
		if type(info) is dict:
			for n,i in info.items():
				print n,i
		else:
			print info
	"""
	if k == 'SystemDevices':
		for n,i in v.items():	
			print n,'\n'
			for d in i:print d['Name']
	elif k == 'SystemInformation':
		for n,i in v.items():
			print n,i
	else:
		pass #print k	
'''

if __name__ == '__main__':
    print monitor()