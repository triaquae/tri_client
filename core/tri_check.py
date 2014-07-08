#!/usr/bin/python
#-*- coding:utf-8 -*-
import threading
import time
import tri_sender

class MonitorThread(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval=interval
        self.thread_stop=False
    
    def run(self):
        print 'monitor data_dic '
        status=get_data_status():
        while not self.thread_stop:
            print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())
            if status:
                #host=proxy_server_net_ip,p
                tri_sender.sender_api(host,port)
            else:
                print 'data not change'
            time.sleep(self.interval)
    def stop(self):
        self.thread_stop=True
        
#得到监控数据是否变化    
def get_data_status(ip):
    '''每次请求发送时间之前，首先判断该客户端监控项是否发生变化'''
    status = 0
    global data_dic
    new_data_dic=get_template_fromDB.get_one_host_items(str(client_ip))
    if new_data_dic!=data_dic:
        status=1
        data_dic=new_data_dic
    return status

    
#monitorthread=MonitorThread(1,3)
#monitorthread.start()
if __name__ == '__main__':
    monitorthread=MonitorThread(1,3)
    monitorthread.start()
    time.sleep(9)
    monitorthread.stop
    
    
    
    