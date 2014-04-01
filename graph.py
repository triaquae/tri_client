import random


interval = {
	'5min' : ['exact', 2000],   # exact stands for real time interval, 2000 stands for max point 
	'10min' : [600, 2016],   # keeps data for 2 weeks, interval 10 mins
        '20min'    : [1200, 2160], # keeps data for 30 days, interval 20 mins
        '1hour'  : [3600, 2160], # keeps data for 90 days, interval 60 mins
        '2hour' : [7200,  2160 ], # keeps data for 180 days, interval 180 mins
        '4hour': [14400, 2190] , # keeps data for 365 days, interval 4 hours
        '12hour': [43200, 2190], # keeps data for 3 years , interval 12 hours
        '24hour' : [86400, 2160], # keeps data for 5 years, interval 24 hours
}




import time
def draw():
        t_stamp = int(time.time())
        for n, v in interval.items():
          if n == '4hour':
                r_list = range(1,v[0]*v[1] ,  v[0])  # step is v[0] 
		data_list = map(lambda x:[t_stamp + x, random.randrange(100)], r_list)
                for i in range(50,95):
                       data_list[i][1] = None
                for i in data_list:
                    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i[0] )), 'data:', i[1]
                return data_list


draw()
