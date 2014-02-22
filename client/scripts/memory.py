#!/usr/bin/env python
import commands


def monitor():
	shell_command ="grep 'MemTotal\|MemFree\|Buffers\|^Cached\|SwapTotal\|SwapFree' /proc/meminfo"
	
	status,result = commands.getstatusoutput(shell_command)
	if status != 0: #cmd exec error
		value_dic = {'status':status}
	else:
		value_dic = {'status':status}
		for i in result.split('kB\n'):
			key= i.split()[0].strip(':') # factor name
			value = i.split()[1]   # factor value
			value_dic[ key] =  value
	return value_dic

if __name__ == '__main__':
	print monitor()
