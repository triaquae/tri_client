import triaquae_env

class MonitorModel:
	check_interval = 10
	alert_enabled = True
	alert_method = 'email'
	contact = 'lijie3721@126.com'	
	script = None
	


class apache(MonitorModel):
	from scripts import cpu
	script = cpu
	check_interval = 60

class loadMonitor(MonitorModel):
	from scripts import cpu
	script = cpu
class cpuMonitor(MonitorModel):
	from scripts import cpu
        script = cpu


#a = cpuMonitor()

#print a.script.monitor()
