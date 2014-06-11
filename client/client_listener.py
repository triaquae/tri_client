#-*- coding:utf-8 -*-
import SocketServer,time
import pickle
import monitor_list
import compress
import key_gen,json
import os,commands,stat,random
from hashlib import md5
recv_dir = 'recv/'
import sys

server_address = '127.0.0.1'
block_list = []
print '-----------------start listen monitor data changed----------------------'
class CListenTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        def md5_file(filename):
                if os.path.isfile(filename):
                        m = md5()
                        with open(filename, 'rb') as f:
                                m.update(f.read())
                        return m.hexdigest()
                else:
                        return None
        def receive_data(sock):
            return_data ='' 
            while True:
                data = sock.recv(4096)
            #print '\033[36;1m%s\033[0m' %data
                if data == 'EndOfDataConfirmationMark':
                    print 'file transfer done==='
                    break
                return_data += data
            #print '\033[34;1m=====\033[0m',return_data
            return return_data
            # self.request is the TCP socket connected to the client
        def receive_data_by_size(sock,size):
            return_data = ''
            filename = time.time() 
            fp = open('recv/'+str(filename)+'.txt','w+')
            restsize = size
            print "recving..."
            while 1:
                if(restsize > 8096):
                    data = sock.recv(8096)
                    return_data += data
                else:
                    data = sock.recv(restsize)
                    return_data += data
                if restsize ==0:
                    break
                fp.write(data)
                restsize = restsize - len(data)
            print restsize
                #if restsize <= 0:
                #    break
            fp.close()
            print "receving is done...............",restsize                    
            return return_data
        def RSA_verifyication(sock):
            raw_rsa_data = sock.recv(396)  #fixed key length
            #print '-------->',raw_rsa_data, len(raw_rsa_data)
            try:
                RSA_signal, encrypted_data,random_num_from_client = json.loads(raw_rsa_data)
            except ValueError:
                print '\033[41;1m.Wrong data format from %s,close connection!\033[0m' %  self.client_address[0]
                return 0
            if RSA_signal == 'RSA_KEY_Virification':
                #encrypted_data = "iwTgqSzMcNOHauWdXXc+rgfbWt6IUXmdIXUqNUJ2U7FZKISc2WR2yAJrq7ldR3TxQEppWgIo/Ycj\nA5gl0fGDVvAEvV02CKZ3gZEI6fWpiMoy6ucpFFDyVAWUrpiXdUOVKxOsDXGgeOObgvd1jsEQCo4i\ncLCBTWDn0HfyQic+Btm1txXc7Nw9jknUCZx6Y8I+6JaIYjNRLwJ6kSMwpTsfP37lvrQfdUkWu3bX\npV9z3hHOQ6+A8rlK7fmL1zk75TXDCmnrLY88UIv6BL4zPXtim4BCD7PlOvDG296br0VIcvF5uhqr\ntj7zOcbA81P1JBFm1nMJqLv+SB5sit923v05XA==\n"
                try:
                    decrpted_data = key_gen.RSA_key.decrypt_RSA(key_gen.private_file,encrypted_data)
                    #print decrpted_data,'+++++++', random_num_from_client
                except ValueError:
                    decrpted_data = 'Incorrect decryption'
                if decrpted_data != random_num_from_client:
                    return 0
            else:
                return 0    
        if RSA_verifyication(self.request) == 0: #didn't pass the RSA virification
            #if self.client_address[0] != server_address:
            err_msg= "\033[31;1mIP %s didn't pass the RSA virification,drop it!\033[0m" % self.client_address[0]
            pickle_data = '', err_msg
            self.request.sendall( pickle.dumps(pickle_data)  )
            print err_msg 
            block_list.append(self.client_address[0])
            if block_list.count(self.client_address[0]) > 5:
                print "Alert::malicious attack from:" , self.client_address[0]
        else:
            print "RSA virification passed!"
            self.request.sendall('RSA_OK')
            #开始接收服务端发来的通信消息
            self.data_type = self.request.recv(1024).strip()
            if self.data_type.startswith( 'MonitorDataChange'):
                #向proxy服务端发送开始准备接受数据
                self.request.send('ReadyToReceiveData')
                #接收改变的监控数据本地保存
                data_size=self.data_type.split("|")[1]
                #data_size=self.request.recv(1024)
                if data_size<=8096:
                    monitor_data_new=self.request.recv(8096)
                else:
                    monitor_data_new=receive_data_by_size(self.request,int(data_size))
                monitor_dic_new=json.loads(monitor_data_new)
                print monitor_dic_new
                filename='../recv/monitor_data_info.txt'
                with open(filename, 'wb') as f:
                    f.write(monitor_data_new)
                print 'write data into file....'
                #新的监控数据如何放到监控中
                
            elif self.data_type.startswith('RUN_Script|'):
                recv_data= self.data
                filename = "%s%s" %(recv_dir,recv_data.split('|')[1].strip())
                print '+++++|receiving file from server:',filename
                md5_key_from_client = self.data.split('|')[2]
                file_content = receive_data(self.request)
                print 'write data into file....'
                with open(filename, 'wb') as f:
                    f.write(file_content)
                md5_key= md5_file(filename)
                print '+++++|verfiying md5key---'
                if md5_key == md5_key_from_client:
                    print 'file transfer verification ok' 
                    self.request.send('FileTransferComplete')
                    os.system('chmod +rx %s ' % filename)
                    #os.chmod(filename,stat.S_IREAD+stat.S_IWOTH+stat.S_IXUSR+stat.S_IRWXO)
                    cmd = "nohup  %s > %s.log &" % (filename, filename)
                    print '\033[32;1mgoing to run script:\033[0m',cmd
                    result = os.system(cmd )
                    #print result,'||||+|||'
                else:
                    print "file not complete"
                    self.request.send('FileTransferNotComplete')
            elif self.data_type.startswith('SEND_FILE|'):
                file_info = self.data.split('|')
                md5_key_from_client = file_info[1]
                compress_mark = file_info[4]
                print compress_mark
                source_file = file_info[2].split('/')[-1]
                if file_info[3].endswith('/'):
                    dst_filename = '%s%s' %(file_info[3], source_file)
                else:
                    dst_filename = '%s/%s' %(file_info[3], source_file)
                print dst_filename
                print '+++++|receiving file from server:',dst_filename
                try:
                    with open(dst_filename, 'wb') as f:
                        self.request.send("FileOk2Send")
                        file_content = receive_data(self.request)
                        print 'write data into file....'
                        f.write(file_content)
                except IOError:
                    print dst_filename,'not exist'
                    self.request.send("FileTransferError:cannot save file to %s" % dst_filename )
                    return  "FileTransferError..."
                md5_key= md5_file(dst_filename )
                print '+++++|verfiying md5key---'
                if md5_key == md5_key_from_client:
                    print 'file transfer verification ok'
                    self.request.send('FileTransferComplete')
                    if compress_mark == 'tarAndCompressed':
                        temp_tar_file = 'temp/%s.tar' % source_file
                        compress.decompress(dst_filename, temp_tar_file)
                        compress.untar(temp_tar_file,file_info[3] )
                        os.remove(temp_tar_file)
                        os.remove(dst_filename)
                    elif compress_mark == 'compressed':
                        target_path = dst_filename.split('/%s' %source_file)[0]
                        print target_path
                        target_file = '%s/%s' %(target_path, source_file[:-2])
                        compress.decompress(dst_filename, target_file)
                        os.remove(dst_filename)
                    else:
                        print "file not complete"
                        self.request.send('FileTransferNotComplete')

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9997
    # Create the server, binding to localhost on port 9997
    try:
        server = SocketServer.ThreadingTCPServer((HOST, PORT), CListenTCPHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print 'prass ctrl+c,break'
        server.server_close()
        sys.exit()
        
#将得到的监控信息本地保存
def save_monitor_data(data):
    with open('d:\monitor_data.json','wb') as f:
        json.dump(data,f)