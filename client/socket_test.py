#coding:utf-8
# Monitoring  client program
import conf,json,threading
import socket,time,sys
import scripts,key_gen,random_pass
import commands
HOST = '10.168.7.48'    # The remote host
#HOST = '192.168.71.130'    # The remote host
PORT = 9999              # The same port as used by the server
hostname = 'localhost'
status_dic = {'services': {}}
last_check_dic = {}
interval_dic = {}

conf.BASE_DIR

def socket_test():
    status_dic['hostname'] = hostname
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))
    encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)
    s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 
    print '\033[34;1m sending status to Monitor server .... \033[0m'

    jsondumps = json.dumps(status_dic)
    sendSignalAndSize = 'datasizetest'
    s.send(sendSignalAndSize)
    flag=s.recv(1024)
    print flag
    get_data=recv_data=s.recv(1024)
    data3=s.recv(1024)
    #print get_data
    print data3
    #发送标记'OK'不行，这里会有一个粘包的问题。
    '''
    while len(recv_data):  
        recv_data = s.recv(1024)
        get_data+=recv_data
    print type(json.loads(get_data))
    '''
    s.close()
    #with open('d:\info_test.json', 'wb') as f:
    #json.dump(status_dic, f)
    print "wait for the next round..."

#socket_test()
a=0
if a==0:
    print a
elif a<=2:
    print 'a<2'
else:
    print 'a>2'
    
