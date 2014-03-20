import triaquae_env
from scripts import load,cpu,memory,upCheck
class MonitorModel:
	check_interval = 30
	alert_enabled = True
	alert_method = 'email'
	contact = 'lijie3721@126.com'	
	script = None
	
class upCheck(MonitorModel):
	check_interval = 30
	script = upCheck
class apache(MonitorModel):
	script = cpu
	check_interval = 60

class memoryMonitor(MonitorModel):
	script = memory	
class loadMonitor(MonitorModel):
	check_interval = 120 
	script = load
class cpuMonitor(MonitorModel):
        script = cpu


#a = cpuMonitor()

#print a.script.monitor()
