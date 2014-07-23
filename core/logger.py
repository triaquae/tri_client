import logging,global_setting 
import os,time

logfile= os.path.join(global_setting.base_dir,time.strftime('log/triaquae_%Y%m.log') )
logging.basicConfig(filename =os.path.join(os.getcwd(), logfile ), filemode='a+', 
	format= '%(asctime)s - [%(filename)s] %(levelname)s: %(message)s' , level=logging.INFO)




def log(level=str,message=str):
	if level == 'debug':
		logging.debug(message)
	elif level == 'info':
		logging.info(message)
	elif level == 'warning':
		logging.warning(message)
	elif level == 'error':
		logging.error(message)
	elif level == 'critical' :
		logging.critical(message)


log('info', 'just test...')	

