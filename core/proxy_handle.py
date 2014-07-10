#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading
import redis_connector
import socket
import key_gen,random_pass
import json

'''
for i in range(5):
    redis_connector.r.set('test','{"a":123}')
    timestamp = time.time()
    redis_connector.r[timestamp]={'b':i}
    #print redis_connector.r.keys()
    time.sleep(1)
    #print redis_connector.r.get(timestamp)
print redis_connector.r.keys()

for k in redis_connector.r.keys():
    print redis_connector.r.get(k)

def db_check(r):
    data_list=[]
    def run(r):
        while 1:
            if r.dbsize():
                for k in r.keys():
                    data=r.get(k)
                    r.delete(k)
                    data_list.append(data)
                    print data
            
            time.sleep(10)
    threading.Thread(target=run, args=(r,)).start()
    #get 
    #print data_list
#db_check(redis_connector.r)
'''
def get_redis_data(r):
    assets_data_list=[]
    if r.dbsize():
        for k in r.keys():
            #得到一条资产信息,这里是以字符串的形式存在的，需要转换
            #assets_data=r.get(k)
            assets_data_json=r[k]
            assets_data=json.loads(assets_data_json)
            r.delete(k)
            assets_data_list.append(assets_data)
        #return assets_data_list
    else:
        print 'redis not assert data info......'
    return assets_data_list

def data_handler():
    #把收集到的信息进行处理并发送到server端
    assets_data_list=get_redis_data(redis_connector.r)
    if len(assets_data_list):
        #处理收集到的资产信息,将一个主机的监控项放到一块，放到server做
        #for assets_data in assets_data_list:
        #    pass
        #直接加proxy ip转发
        proxy_assets_data={}
        proxy_assets_data[HOST]=assets_data_list
        send_data(0,S_HOST,PORT,json.dumps(proxy_assets_data))
    else:
        pass
    
def send_data(is2client,host,port,data):
    try:
        send_cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        send_cs.connect((host, port))
        print 'start connect client/server host'
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        print '1----'
        send_cs.send(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print '\033[34;1m sending Monitor Data to proxy server  .... \033[0m'
        #判断RSA认证结果
        RSA_status=send_cs.recv(1024)
        if RSA_status == 'RSA_OK':
            #RSA认证通过后，发生数据状态，
            if is2client:
                #向client端分发监控项数据
                send_cs.send('MonitorDataChange'+'|'+str(len(data)))
                print 'MonitorDataChange........'
            else:
                #向server端上传资产数据
                send_cs.send('MonitorResultDataCollect'+'|'+str(len(data))+'|'+'proxy')
                print 'MonitorResultDataCollect...............'
            transfer_status=send_cs.recv(1024)
            if transfer_status=='ReadyToReceiveData':
                #向client/server host端发送该主机监控数据/或资产数据
                #send_cs.send(str(len(json.dumps(data))))
                print data
                send_cs.send( data )
        else:
            print 'RSA Virification error!'
    except socket.error:
        print socket.error
    finally:
        send_cs.close()

def test():
    for i in range(4):
        data={'b':i}
        data_json=json.dumps(data)
        redis_connector.r[i]=data_json
    time.sleep(3)
    for k in redis_connector.r.keys():
        d=redis_connector.r[k]
        print d
        print json.loads(d)
#test()

counter = 0
HOST='10.168.7.105'
S_HOST='10.168.7.105'
PORT=9998
while True:
    print '----Alert Checking Executed...>>>>' ,counter
    counter += 1
    data_handler()
    #p = subprocess.Popen('python /home/alex/tri_client/status_data_optimzation.py', stdout=subprocess.PIPE, shell=True)
    #print monitor_list
    time.sleep(5)
