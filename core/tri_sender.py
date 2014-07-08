#-*- coding:utf-8 -*-
# send moniter change data program
import json,threading
import socket,time,sys
import key_gen,random_pass
import commands
import get_monitor_dic_fromDB
#from testWeb.models import *

def send_api(host,port,data):
    try:
        send_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print 'start connect proxy server/client'
        send_s.connect((host,port))
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        send_s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print '\033[34;1m sending Monitor Data to proxy server/client  .... \033[0m'
        #判断RSA认证结果
        RSA_status=send_s.recv(1024)
        if RSA_status == 'RSA_OK':
            #RSA认证通过后，发送监控项数据改变，这里有本机、代理。如何判断？
            print RSA_status
            send_s.send('MonitorDataChange'+'|'+str(len(data)))
            transfer_status=send_s.recv(1024)
            if transfer_status=='ReadyToReceiveData':
                #send_s.send(str(len(proxy_monitor_list_json)))
                print data
                send_s.send(data)
                #break       
            else:
                pass
        else:
            print 'RSA Virification error!'
    except socket.error:
        print socket.error
    finally:
        send_s.close()

#得到监控项状态
def get_monitor_status():
    proxy_list=trunk_servers.objects.all()
    for tc in trunk_servers.objects.all():
        pass
        #如何得到变化的监控数据

#首先要得到改变的监控项，找到其所属服务端(server/trunk_servers)，
#代理需要整理该代理中改变的监控主机，一块集中发送。
#1如何得到改变的监控项？

#向proxy server端，发送该局域网的监控数据
#???如何向本地主机发送监控项数据改变???得到该监控项hostname
def notice_change_data( hostname ):
    #改变的监控项
    moniter_data_change=get_monitor_dic_fromDB.get_change_monitor_dic(hostname)
    moniter_data_change_json=json.dumps(moniter_data_change)
    belongs_to=get_monitor_dic_fromDB.get_host_proxy(hostname)
    #本地内的主机进行直接向client端发送信息ts.id
    if belongs_to.name == "trunk_servers":
        host=get_monitor_dic_fromDB.get_host_ip(hostname)
        port=9997
        send_api(host,port,moniter_data_change_json)
    else:
        #代理的监控信息
        #host=get_monitor_dic_fromDB.get_proxy_ip(belongs_to)
        host=belongs_to.ip_address
        port=9999
        send_api(host,port,moniter_data_change_json)
    
def assets_data_clear(hostname ):
    #得到该监控项hostname的资产信息，进行清0
    #这里在redis、服务端、代理端中还会存在该hostname的资产信息？？怎么办？
    pass
#任务，线程中的任务出现死循环，与线程外的死循环的区别？？
def moniter_job( interval ):
    status_dic = {}
    #run single thread...
    result=[]
    def run():
        print 'going to run ...',name
        while True:
            status=get_monitor_status()
            if status:
                #数据改变进行推送
                send_api(host,port)
            else:
                print 'data not change'
            time.sleep(interval)
    result.append(threading.Thread(target=run, args=(name,t)).start())
    
#开启一个线程不断判断监控数据是否改变
if __name__ == '__main__':
    #moniter_job(3)
    notice_change_data( '5245')