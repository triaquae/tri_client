#!/usr/bin/env python 
import redis_connector

r = redis_connector.get_redis()
r.set('aa','test')
print 'ok'
print r['aa']

'''
data_dic={'name':'zxv','age':22}
r.lpush('ls','str')
r.lpush('ls',data_dic)
'''
print r.lrange('ls',0,-1)

a_list=[1,2,3,4,5]
#r.lpush('ls',a_list)
result=r.lrange('ls',0,0)

len=r.llen('ls')
print len

for i in range(r.llen('ls')):
    value=r.lpop('ls')
    print value
    
b_list=result[0].strip("[]").split(",")
print type(b_list[0])