#from scripts import sys_Info,cpu,memory,disk,netinfo
#from scripts import *
from plugins import upCheck
def upCheck_info():
	return upCheck.monitor()

"""
def sys_info():
    return sys_Info.monitor()
    
def cpu_info():
    return cpu.monitor()
    
def mem_info():
    return memory.monitor()

def disk_info():
    return disk.monitor()

def net_info():
    return netinfo.monitor()
"""
