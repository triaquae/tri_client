#!/usr/bin/env python
#Author: Alex Li

import time,sys,os
import datetime,db_connector
from Triaquae.hosts.models import OpsLog,OpsLogTemp
cur_dir = os.path.dirname(os.path.abspath(__file__))
date =time.strftime('%Y_%m_%d %H:%M:%S')
	

def RecordLogSummary(Action,LogType,TrackMark,RunUser='null',Cmd='null',TotalTasks= 0,Note='Null',tri_user='BatchExctution',success_numbers = 0,failed_numbers = 0):
	if Action == 'UPDATE':
		log_item = db_connector.OpsLog.objects.get(track_mark = TrackMark)
		log_item.success_num = len(db_connector.OpsLogTemp.objects.filter(track_mark = TrackMark,result='Success')) 
		log_item.failed_num = len(db_connector.OpsLogTemp.objects.filter(track_mark = TrackMark,result='Error'))
		log_item.save()
	
	if Action == 'CREATE':
		log_item = db_connector.OpsLog.objects.create(
		log_type = LogType,
		#tri_user = 'BatchExctution',
		tri_user = tri_user,
		run_user = RunUser,
		cmd 	= Cmd,
		total_task = TotalTasks,
		success_num = success_numbers,
		failed_num = failed_numbers,
		track_mark = TrackMark,
		note = Note,

		)
	
def RecordLog(Host,LogType,Cmd,Log,Result,trace_num,run_user,multi_run,Note='Null'):
	def transfer_log_format(Log_content):
		if len(Log_content) >1:
			return "%s  %s" % (Log_content[0],Log_content[1])
		else:
			return "%s" % Log_content[0]
	log_item = db_connector.OpsLogTemp.objects.create(
		ip = Host,
		event_type = LogType,
		cmd = Cmd,
		event_log = Log,
		result = Result,			
		note = Note,
		track_mark = trace_num,
		user = run_user
	)
	if multi_run == 1:
		RecordLogSummary('UPDATE',LogType,trace_num)	
	else:
		RecordLogSummary('CREATE',LogType,trace_num,run_user,Cmd,1)
		RecordLogSummary('UPDATE',LogType,trace_num)

#RecordLogSummary('CREATE','BatchRun','root','df -h',20,10,2,123,'/tmp/ops_log_123.log')
#Example
#RecordLog('192.168.2.140','CommandExcution','uname -a','Excution Result....','Success',80,'RunUser')

