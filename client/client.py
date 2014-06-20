# -*- coding:utf-8 -*-
# Monitoring  client program
import conf,json,threading
import socket,time,sys
import plugins,key_gen,random_pass
import plugin_conf
import commands
import importlib
from monitor_data_deal import *
HOST = '10.168.0.218'    # The remote host
PORT = 9998             # The same port as used by the server
hostname = 'localhost'
status_dic = {'services': {}}
last_check_dic = {}
interval_dic = {}

monitor_file_md5=0
conf.BASE_DIR

def pprint(msg,msg_type):
    if sys.platform.startswith("win"):
        if msg_type == 'err':
            print 'Error:%s' % msg
        elif msg_type == 'success':
            print '%s' % msg
        else:
            pass
    else:
        if msg_type == 'err':
            print '\033[31;1mError:%s\033[0m' % msg
        elif msg_type == 'success':
            print '\033[32;1m%s\033[0m' % msg
        else:
            pass
    
#monitor_dic k=ip
def get_interval_dic(monitor_data):
    #[{'monitor_type': u'agent', 'plugin': u'plugin.assets', u'id': 4L, 'check_interval': 5L, 'name': u'window assets'}, ]
    global interval_dic
    for k in monitor_data.keys():
        if k == 'hostname':
            global hostname
            hostname=monitor_data[k]
        else:
            for service in monitor_data[k]:
                for m in service.keys():
                    #得到监控项、时间、插件脚本名
                    if m=='check_interval':
                        interval=service[m]
                    elif m=='name':
                        service_name=service[m]
                    elif m=='plugin':
                        service_plugin=service[m]
                if interval_dic.has_key(interval):
                    interval_dic[interval]['name'][service_name] = service['plugin']
                else:
                    interval_dic[interval]={'name':{service_name:service['plugin']},'last_check': 0}
    return interval_dic

#the frist get monitor data
def revc_data_by_size(sock,size):
    return_data = ''
    filename = time.time() 
    #fp = open('/tmp/'+str(filename),'wb')
    restsize = size
    print "recving..."
    while restsize:
        if(restsize > 8096):
            data = sock.recv(8096)
            return_data += data
        else:
            data = sock.recv(restsize)
            return_data += data
        #fp.write(data)
        restsize = restsize - len(data)
    print restsize
    #fp.close()
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
                print 'no monitor_data configured for this host'
                #req_s.send('get_info')
                return 0
            elif int(monitor_data_size) <=8096:
                monitor_data=req_s.recv(8096)
            else:
                monitor_data=revc_data_by_size(req_s,int(monitor_data_size))
                #将监控的数据放到文件中,并对文件生成md5密钥
                filename='../recv/monitor_date_frist.json'
                generate_file(filename,monitor_data)
                global monitor_file_md5
                monitor_file_md5=generate_file_md5value(filename)
            if len(monitor_data) == int(monitor_data_size): #data received success
                interval_dic=get_interval_dic(json.loads(monitor_data))
                return interval_dic
            else:
                pprint('Could not retrieve the monitor list for this host,please check with your Monitor server', 'err')
                sys.exit()
            #将监控的数据放到文件中,并对文件生成md5密钥
        else:
            pprint('RSA authentication failed.......','err')
            sys.exit()
    except socket.error:
        pprint(socket.error, 'err')
    finally:
        req_s.close()

def multi_job(m_list, m_interval,frist_invoke=1):
    status_dic = {}
    #run single thread...
    def run(name,m_api,frist_invoke=1):
        print 'going to run ...',name
        """
        fun=getattr(scripts_conf,name)
        #得到某个监控项的资产信息
        #pythoncom.CoInitialize()
        status_dic[name] = fun()
        
        if sys.platform.startswith("win"):
            import pythoncom
            pythoncom.CoInitialize()
        """
        plugin_module=importlib.import_module(m_api)
        status_dic[name]=plugin_module.monitor(frist_invoke)
        #
        interval_dic[m_interval]['last_check'] = time.time()
        return interval_dic[m_interval]
    result = [] 
    for name, t in m_list.items():
        result.append(threading.Thread(target=run, args=(name,t,frist_invoke)).start())
    # get result
    while True:
        if len(status_dic) == len(m_list): #all threads are finished.
            return status_dic
            break
        else: 
            time.sleep(1)

def send_data(result_dic):
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
            result_dic_json=json.dumps(result_dic)
            sendSignalAndSize = 'MonitorResultDataCollect'+'|'+str(len(result_dic_json))+'|'+'client'
            client_s.send(sendSignalAndSize)
            transferSignal = client_s.recv(1024)
            if transferSignal == 'ReadyToReceiveData':
                client_s.send(result_dic_json)
            else:
                pass
    except socket.error:
        print socket.error
    finally:
        client_s.close()
    print "wait for the next round..."
    
def monitor_api(m_dic, m_interval):
    #global is_frist_assets_data
    #不同监控时间，得到的监控项资产信息不同，这里用多个文件来保存。？？？
    monitor_dic={}
    #if is_frist_assets_data:
    if not m_dic['last_check']:
        monitor_data= multi_job(m_dic['name'], m_interval,frist_invoke=1)
    else:
        monitor_data= multi_job(m_dic['name'], m_interval,frist_invoke=0)
    #添加主机名key，外包一层
    monitor_dic['hostname'] = hostname
    monitor_dic['result_values']=monitor_data
    send_data(monitor_dic)
    
'''
    if not m_dic['last_check']:
        #是0时，表面是第一次收集该间隔的资产信息
        monitor_data= multi_job(m_dic['name'], m_interval)
        #monitor_data['change_mark']=1
        #添加主机名key，外包一层
        monitor_dic['hostname'] = hostname
        monitor_dic['result_values']=monitor_data
        assets_filename='../recv/assets_'+str(m_interval)+'.json'
        generate_file(assets_filename,monitor_dic)
        is_frist_assets_data=0
        print 'frist assets data sending .....'
        print monitor_dic
        send_data(monitor_dic)
    else:

        monitor_new_data = multi_job(m_dic['name'], m_interval)
        monitor_new_dic['hostname'] = hostname
        monitor_new_dic['result_values'] = monitor_new_data
        assets_newfile='../recv/assets_'+str(m_interval)+'_tmp.json'
        generate_file(assets_newfile,monitor_new_dic)
        file_md5_old=generate_file_md5value('../recv/assets_'+str(m_interval)+'.json')
        file_md5_new=generate_file_md5value(assets_newfile)
        #比较文件md5值是否相同,在第二次才开始比较
        #filecmp.cmp(r'e:\1.txt',r'e:\2.txt') 
        #
        
        if file_md5_old == file_md5_new:
            print 'assets no change........'
        else:
            assets_old_dic=read_file('../recv/assets_'+str(m_interval)+'.json')
            assets_change_dic=get_monitor_data_change(json.loads(assets_old_dic),assets_new_dic)
            #只发送改变的监控项
            assets_change_dic['hostname']=hostname
            print 'assets data change sending.....'
            generate_file('../recv/assets_'+str(m_interval)+'.json',assets_change_dic)
            send_data(assets_change_dic)
'''
# Trigger the monitor api
connect_num=4
while True:
    if len(interval_dic):
        '''
        monitor_file_md5_new=generate_file_md5value('../recv/monitor_date_frist.json')
        if monitor_file_md5_new != monitor_file_md5:
            #读取新的监控项数据
            monitor_data=read_file('../recv/monitor_date_frist.json')
            monitor_dic=json.loads(monitor_data)
            #调用得到的新的监控数据方法
            interval_dic=get_interval_dic(monitor_dic)
            print 'used new monitor data to collect assets'
            #是否要发送一个标识，通知服务器端更新资产信息；
            #还是在服务器端直接将该主机的资产信息清0
        else:
            pass
        '''
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

if __name__ == '__main__':
    '''
    monitor_list_from_server = get_monitor_dic() #may have duplicate items
    monitor_list= [] 
    for service in  monitor_list_from_server:
        if service not in monitor_list:
            monitor_list.append(service)
        else:pass #ignore duplicate service item
    for i in monitor_list:
        print i['plugin']
    '''
    pass
