# -*- coding:utf-8 -*-
# Monitoring  client program
import conf,json,threading
import socket,time,sys
import scripts,key_gen,random_pass
import scripts_conf
import commands
import pythoncom
HOST = '10.168.7.69'    # The remote host
PORT = 9999             # The same port as used by the server
hostname = 'localhost'
status_dic = {'services': {}}
last_check_dic = {}
interval_dic = {}

from assets_deal import * #处理资产数据是否变化
is_frist_assets_data=1
conf.BASE_DIR
'''
#get all the services' monitor inverval and put it into interval_dic
for k,v in conf.enabled_services.items():
    if k == 'services':
        for i in v:
            service_name,service = i[0],i[1]
            if interval_dic.has_key( service.check_interval):
                interval_dic[ service.check_interval ]['name'][service_name] = service
            else:
            
                interval_dic[ service.check_interval ] = { 'name' :  { service_name : service },
                                       'last_check': 0 }
            
'''
#how to get interval_dic form db
#monitor_dic k=ip
def get_interval_dic(monitor_dic):
    global interval_dic
    for ip in monitor_dic.keys():
        if ip == 'hostname':
            global hostname
            hostname=monitor_dic[ip]
        else:
            for service in monitor_dic[ip]:
                for m in service.keys():
                    #得到监控项和时间
                    if m=='interval':
                        interval=service[m]
                    else:
                        service_name=service[m]
                if interval_dic.has_key(interval):
                    interval_dic[interval]['name'][service_name] = service
                    #interval_dic[interval]['name'] = service_name
                else:
                    interval_dic[interval] = { 'name' : { service_name : service},'last_check': 0 }
    '''
    for ip in monitor_dic.keys():
        for service in monitor_dic[ip]:
            #monitor_dic[ip] is a service list 
            for m in service.keys():
                #得到监控项和时间
                if m=='interval':
                    interval=service[m]
                else:
                    service_name=service[m]
            if interval_dic.has_key(interval):
                interval_dic[interval]['name'][service_name] = service
                #interval_dic[interval]['name'] = service_name
            else:
                interval_dic[interval] = { 'name' : { service_name : service},'last_check': 0 }
                #interval_dic[interval] = { 'name': service_name ,'last_check': 0 }
    '''
    return interval_dic

#the frist get monitor data
def revc_data_by_size(sock,size):
    return_data = ''
    filename = time.time() 
    fp = open('/tmp/'+str(filename),'wb')
    restsize = size
    print "recving..."
    while restsize:
        if(restsize > 8096):
            data = sock.recv(8096)
            return_data += data
        else:
            data = sock.recv(restsize)
            return_data += data
        fp.write(data)
        restsize = restsize - len(data)
    print restsize
    fp.close()
    print "receving is done...............",restsize                    
    return return_data
    
def get_monitor_dic():
    '''第一次连接时，请求得到自己的监控项数据'''
    try:
        req_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        req_s.connect((HOST, PORT))
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        req_s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print 'get assets monitor configure info from server .... '
        #判断RSA认证结果
        RSA_status=req_s.recv(1024)
        if RSA_status == 'RSA_OK':
            #RSA认证通过后，发生数据状态，
            req_s.send('MonitorDataRequest'+'|'+'client')
            #接收到的数据大小如何确定
            monitor_data_size=req_s.recv(1024)
            if int(monitor_data_size) == 0:
                print 'no monitor_data'
                req_s.send('get_info')
                return 0
                #req_s.send('get_info')
            elif int(monitor_data_size) <=8096:
                monitor_data=req_s.recv(8096)
            else:
                monitor_data=revc_data_by_size(req_s,int(monitor_data_size))
            print 'get monitor data'
            req_s.send('get_info')
            monitor_dic=json.loads(monitor_data)
            #调用得到的监控数据方法
            interval_dic=get_interval_dic(monitor_dic)
            #send message
            req_s.send('get_data')
            #处理监控项数据，并存储到文件中。
            #{'10.168.7.35': [{'services': u'cpu', 'interval': 30L},,]}
            with open('d:\interval_data_temp.json', 'wb') as f:
                json.dump(interval_dic, f) 
            return interval_dic
        else:
            print 'rsa error.......'
    except socket.error:
        print socket.error
    finally:
        req_s.close()
        
print get_monitor_dic()

def multi_job(m_list, m_interval):
    status_dic = {}
    #run single thread...
    def run(name,m_api):
        print 'going to run ...',name
        fun=getattr(scripts_conf,name)
        #得到某个监控项的资产信息
        pythoncom.CoInitialize()
        status_dic[name] = fun()
        interval_dic[m_interval]['last_check'] = time.time()
        return interval_dic[m_interval]
    result = [] 
    for name, t in m_list.items():
        result.append(threading.Thread(target=run, args=(name,t)).start())
    # get result
    while True:
        if len(status_dic) == len(m_list): #all threads are finished.
            return status_dic
            break
        else: 
            time.sleep(1)

def send_data(assets_dic):
    try:
        client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_s.connect((HOST, PORT))
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        client_s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print '\033[34;1m sending status to Monitor server .... \033[0m' 
        #判断RSA认证结果
        RSA_status=client_s.recv(1024)
        if RSA_status == 'RSA_OK': 
            #RSA认证通过后，发生数据状态
            assets_dic_json=json.dumps(assets_dic)
            sendSignalAndSize = 'AssetsDataCollect'+'|'+str(len(assets_dic_json))+'|'+'client'
            client_s.send(sendSignalAndSize)
            transferSignal = client_s.recv(1024)
            if transferSignal == 'ReadyToReceiveData':
                client_s.send(json.dumps(assets_dic))
            else:
                pass
    except socket.error:
        print socket.error
    finally:
        client_s.close()
    print "wait for the next round..."
    
def monitor_api(m_dic, m_interval):
    global is_frist_assets_data
    #不同监控时间，得到的监控项资产信息不同，这里用多个文件来保存。？？？
    assets_dic={}
    if is_frist_assets_data:
        assets_dic = multi_job(m_dic['name'], m_interval)
        assets_dic['hostname'] = hostname
        generate_file('../recv/assets_tmp.log',assets_dic)
        is_frist_assets_data=0
        print 'frist assets data sending .....'
        print assets_dic
        send_data(assets_dic)
    else:
        assets_new_dic = multi_job(m_dic['name'], m_interval)
        assets_new_dic['hostname'] = hostname
        generate_file('../recv/assets_tmp1.log',assets_new_dic)
        file_md5_old=generate_file_md5value('../recv/assets_tmp.log')
        file_md5_new=generate_file_md5value('../recv/assets_tmp1.log')
        #比较文件md5值是否相同,在第二次才开始比较
        #filecmp.cmp(r'e:\1.txt',r'e:\2.txt') 
        #
        if file_md5_old == file_md5_new:
            print 'assets no change........'
        else:
            assets_change_dic=get_assets_data_change(assets_dic,assets_new_dic)
            generate_file('../recv/assets_tmp.log',assets_change_dic)
            assets_dic=assets_new_dic
            #只发送改变的监控项
            assets_change_dic['hostname']=hostname
            print 'assets data change sending.....'
            send_data(assets_change_dic)
        
        send_data(assets_new_dic)
# Trigger the monitor api
connect_num=4
while True:
    if len(interval_dic):
        for interval,monitor_dic in interval_dic.items():
            time_diff = time.time() - monitor_dic['last_check']  
            if time_diff >= interval:
                #print time_diff,'going to monitor %s ' % monitor_dic['name']
                monitor_api(monitor_dic, interval)
                #monitor_dic['last_check'] = time.time()
            else:
                print '%s hit the next inteval in %s seconds.' % (monitor_dic['name'].keys(), interval - time_diff )
        #monitor_api()
    else:
        #首次没有监控数据时
        if connect_num:
            print 'no monitor data...........'+str(connect_num)
            get_monitor_dic()
            connect_num -=1
        else:
            break
    time.sleep(5)

