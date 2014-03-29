import random


import random


interval = {
        '3hour'    : 10800000,
        '1day'  : 86400000,
        '1week' : 604800,
        '1month': 2592000,
        '3month': 7776000,
        '6month' : 15552000,
        '1year': 31536000

}


max_points = 360000


import time
def draw():
        t_stamp = int(time.time()* 1000)
        for n, t in interval.items():
          if n == '1day':
                r_list = range(1,t,max_points)
                data_list = map(lambda x:[t_stamp + x, random.randrange(100)], r_list)
                for i in range(50,95):
                        data_list[i][1] = None:
                for i in data_list:
                        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i[0] / 1000))
                return data_list


"""

interval = {
	'30min' : 1800,
	'3hour'    : 10800,
	'1day'	: 86400,
	'1week' : 604800,
	'2week' : 1209600,
	'1month': 2592000,
	'3month': 7776000,
	'6month' : 15552000,
	'1year': 31536000
	
}


max_points = 600


import time

t_stamp = int(time.time() * 1000)
for n, t in interval.items():
  if n == '3hour':
	r_list = range(1,t, max_points)
	data_list = map(lambda x:[t_stamp + x, random.randrange(100)], r_list)
	print n,data_list



"""
