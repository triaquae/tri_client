#!/usr/bin/env python 
import redis
r = redis.Redis(host='localhost', port=6379, db=0) 

def get_redis(host_ip='localhost',port=6379,db=0):
    
    return redis.Redis(host=host_ip,port=port,db=db)





