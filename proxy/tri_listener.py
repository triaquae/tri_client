#-*- coding:utf-8 -*-
# Listening server send monitor data program
import SocketServer,time
import pickle
import os,stat
from hashlib import md5
import db_connector,key_gen

import conf,json,threading
import socket,time,sys
import scripts,key_gen,random_pass
import scripts_conf
import commands
HOST = '10.168.0.218'    # The remote host
#HOST = '192.168.71.130'    # The remote host
PORT = 9998              # The same port as used by the server
hostname = 'localhost'
status_dic = {'services': {}}
last_check_dic = {}
interval_dic = {}
monitor_dic = {}

conf.BASE_DIR

block_list = []
data_dic = {}

#get all the services' monitor inverval and put it into interval_dic

#how to get interval_dic form db
#monitor_dic k=ip
def get_interval_dic(monitor_dic):
    global interval_dic
    for ip in monitor_dic.keys():
        for service in monitor_dic[ip].keys():
            #service :ip has service
            for p in monitor_dic[ip][service].keys():#
                #p:interval=,items=[]
                if p=='interval':
                    interval=monitor_dic[ip][service][p]
            if interval_dic.has_key(interval):
                interval_dic[interval]['name'][service] = monitor_dic[ip][service]
            else:
                interval_dic[interval] = { 'name' : { service : monitor_dic[ip][service]},'last_check': 0}
    return interval_dic

#the frist get monitor data所有以该代理为服务端的主机监控信息 
def get_monitor_dic():
    '''第一次连接时，请求得到所有以该代理为服务端的主机监控信息'''
    try:
        req_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        req_s.connect((HOST, PORT))
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        req_s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print 'get assets monitor configure info from server .... '
        req_s.send('GetMonitorItems')
        #如果服务端查不到数据时，会发生异常。
        monitor_data = req_s.recv(1024)
        #该客户端没有被监控
        if monitor_data=='no_monitor':
            req_s.send('get_data')
            #break
        else:
            monitor_dic=json.loads(monitor_data)
            #调用得到的监控数据方法
            get_interval_dic(monitor_dic)
            #send message
            req_s.send('get_data')
        #with open('d:\info_test.json', 'wb') as f:
            #json.dump(status_dic, f)
        #interval_dic = 
    except socket.error:
        print socket.error
    finally:
        req_s.close()
get_monitor_dic()

#监听Server端发送来的监控信息，以及考虑如何存储。
print '---------listen server send monitor info---------'
class ListenTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        def md5_file(filename):
            if os.path.isfile(filename):
                m =md5()
                with open(filename,'rb') as f:
                    m.update(f.read())
                return m.hexdigest()
            else:
                return None
        def receive_data(sock):
            return_data =''
            while True:
                data =sock.recv(4096)
                if data == 'EndOfDataConfirmationMark':
                    print 'file transfer done==='
                    break
                return_data += data
            return return_data
        # self.request is the TCP socket connected to the client    
        def RSA_verifyication(sock):
            raw_rsa_data=sock.recv(396)
            try:
                RSA_signal,encrypted_data,random_num_from_client = json.loads(raw_rsa_data)
            except ValueError:
                print '\033[41;1m.Wrong data format from %s,close connection!\033[0m' % self.client_address[0]
                return 0
            if RSA_signal=='RSA_KEY_Virification':
                try:
                    decrpted_data=key_gen.RSA_key.decrypt_RSA(key_gen.private_file,encrypted_data)
                except ValueError:
                    decrpted_data='Incorrect decryption'
                if decrpted_data !=random_num_from_client:
                    return 0
            else:
                return 0
        
        if RSA_verifyication(self.request)==0:
            #didn't pass the RSA virification
            err_msg= "\033[31;1mIP %s didn't pass the RSA virification,drop it!\033[0m" % self.client_address[0]
            pickle_data = '', err_msg
            self.request.sendall( pickle.dumps(pickle_data)  )
            print err_msg 
            block_list.append(self.client_address[0])
            if block_list.count(self.client_address[0]) > 5:
                print "Alert::malicious attack from:" , self.client_address[0]
        else:
            self.request.sendall('RSA_OK')
            #get connect client ip and port.
            host_ip,host_port=self.client_address
            print "{} wrote:",self.client_address[0]
            #get server and client send data_type judge server how to do
            self.data_type = self.request.recv(1024).strip()
            if self.data_type.startswith('MonitorServicesData'):
                #发送连接状态
                self.request.sendall('ReadyToReceiveData')
                #get_proxy_monitor_dic
                proxy_monitor_dic=json.loads(self.request.recv(4096))
                #下发这些监控信息，得到监控数据中具有的ip
                for k in proxy_monitor_dic.keys():
                    if k == 'ip':
                        client_ip=proxy_monitor_dic[k]
                        #向client端发送改变的监控信息
                        send2client(client_ip,9999,monitor_data_dic[client_ip])
                        
            elif self.data_type == 'ReportMonitorStatus':
                #数据是否发生变化
                data_status=get_data_status(client_ip)
                if data_status: #'monitor_items_info change'
                    self.request.send('MonitorItemsChange')
                    #得到请求连接的ip,self.client_address[0],得到该ip的监控信息
                    self.request.send(json.dumps(data_dic))
                else:
                    self.request.send('ReadyToReceiveData')
                    #raw_data_from_client = self.request.recv(8096)
                    #print '+++', raw_data_from_client
                    #接收数据状态时，发送数据的大小
                    signal_size = self.data_type.split("|")
                    raw_data_from_client_size = int(signal_size[1])
                    if raw_data_from_client_size <= 8096:
                        raw_data_from_client = self.request.recv(8096)
                    #else:
                    #   raw_data_from_client = self.request.recv(raw_data_from_client_size)
                    else:
                        raw_data_from_client = receive_data_by_size(self.request,raw_data_from_client_size)
                    status_data = json.loads( raw_data_from_client )
                    client_hostname =  status_data['hostname']
                    for name,service_status in status_data.items():
                        #print name,service_status
                        if type(service_status) is dict:service_status['last_check'] = time.time()
                        monitor_dic[ client_hostname][name] =  service_status
                    print "************get conn from %s------\n" %client_hostname
                    # push status data_type into JSON file
                    if client_hostname == 'localhost':
                        #print redis_connector.r.keys()
                        redis_connector.r['TriAquae_monitor_status'] = json.dumps(monitor_dic)
                        #redis_connector.r.save()
                        print 'status inserted into JSON file'
            elif self.data_type == 'GetMonitorItems':
                #如果不存在IP的监控项？？client_ip,不能使用 global data_dic
                #global data_dic
                data_dic=get_template_fromDB.get_one_host_items(str(client_ip))
                #get client_ip's items data_dic
                while 1:
                    if data_dic:
                        print data_dic
                        self.request.send(json.dumps(data_dic))
                    else:
                        #没有得到数据时，返回了一个0
                        self.request.send('no_monitor')
                        print 'ip has not monitor status'
                    #接收客户端是否接收成功！，注意这是阻塞等待接收？？？
                    self.data_status=self.request.recv(1024)
                    print self.data_status
                    #接收成功。
                    if self.data_status:
                        print self.data_status
                        break
                    else:
                        pass

def send2client(host,port,data):
    try:
        send_cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print 'start connect client host'
        RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
        encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
        send_cs.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
        print '\033[34;1m sending Monitor Data to proxy server  .... \033[0m'
        #判断RSA认证结果
        RSA_status=send_cs.recv(1024)
        if RSA_status == 'RSA_OK':
            #RSA认证通过后，发生数据状态，
            send_cs.send('MonitorServicesDataChange')
            transfer_status=send_cs.recv(1024)
            if transfer_status=='ReadyToReceiveData':
                #向client host端发送该主机监控数据
                send_cs.send( json.dumps(data) )
                #break       
            else:
                data_str=send_cs.recv(1024)
                monitor_dic=json.loads(data_str)
        else:
            print 'RSA Virification error!'
    except socket.error:
        print socket.error
    finally:
        send_cs.close()
                        
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9998
    # Create the server, binding to localhost on port 9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), ListenTCPHandler)
    server.serve_forever()
    
#将得到的监控信息本地保存
def save_monitor_data():
    with open('d:\info_test.json','wb') as f:
        json.dump('monitor_data_dic',f)
