def receive_data(sock):
	return_data =''
	while True:
		data = sock.recv(4096)
		print '+:',data
		if data == 'EndOfDataConfirmationMark':
			print 'file transfer done==='
			break
		return_data += data
	return return_datr
