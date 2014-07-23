# Monitoring  client program
import json,threading
import socket,time,sys
import key_gen,random_pass


def server_connector(status_dic, HOST,PORT ):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))
	except socket.error:
		sys.exit( "TriAquae Master server couldn't be connected!")
		
	RSA_signal,random_num = 'RSA_KEY_Virification', str(random_pass.randomPassword(10))

	encrypted_data = key_gen.RSA_key.encrypt_RSA(key_gen.public_file,random_num)

	s.sendall(json.dumps( (RSA_signal,encrypted_data, random_num) )) 

	print '\033[34;1m getting data from triaquae server .... \033[0m' 
	s.send('SyncConfigDataToTrunkServer')
	transferSignal = s.recv(1024)
	if transferSignal == 'ReadyToReceiveStatusData':
		s.sendall(json.dumps(status_dic))
	s.close()
	print "wait for the next round..."
	

#server_connector('get configure data from server', '10.168.7.101', 9998)
