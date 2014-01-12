import multiprocessing


# batch run process

result = []
def run(host):
	task = '''%s %s '%s' %s %s''' % (script,host,cmd,run_user,track_num)
	os.system(task)

if len(ip_list) < 50:
	thread_num = len(ip_list)
else:
	thread_num = 30
pool = multiprocessing.Pool(processes=thread_num)

for ip in ip_list:
	result.append(pool.apply_async(run,(ip,)) )
#time.sleep(5)
#pool.terminate()

pool.close()
pool.join()


for res in result:
	res.get(timeout=5)
