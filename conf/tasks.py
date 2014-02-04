job='job'
schedule='schedule'
collect_result = 'collect_result'


# setup schedules
schedule_list = {
           'schedule_name1': '45 4 1,10,22 * * ' , # run at 4:45 of each first,10th,22th of the month.
           'schedule_name2': '0 4 1 jan * ',  # run at 4am of Jan 1st. 

}



# tasks 
task1={
    job: { 
	   #job 1
	   1: {
		     'script' :[],
                     'command':[],
		     'run_user': 'root'
               }, 
	   #job 2
           2: {
		     'script':['check_status.py'],
                     'command':['df -h', 'pwd'],
		     'run_user': 'alex'

               },

    }, # end job
    
    schedule: 'schedule_name13',
    # if set it to True,client will send the result back after the task is done
    collect_result: True,
}


task2 = {}
task3 = {}
