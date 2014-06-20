import time
import threading
data = [] 

def func(name,n):
	print 'func passed to Threding...',n
	time.sleep(2)
	data.append(name) 

#t = threading.Thread(target=func, args=('alex',))
#t1 = threading.Thread(target=func,args=('king',))
#t1.start()
#t.start()
result = []
for i in range(10):
	result.append(threading.Thread(target=func, args=('alex',i)).start())
	

status=[]
#time.sleep(2)
while True:
	if len(data) == 10:
		print data
		break
	else:time.sleep(1)
