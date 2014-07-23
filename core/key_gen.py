import global_setting
import RSA_key,sys,os


private_file, public_file = '%s/conf/.rsa_private.id' % global_setting.base_dir, '%s/conf/.rsa_public.id' %global_setting.base_dir
if not os.path.isfile(private_file):
	print "\033[31;1mError:RSA private key file %s is not exsit.\033[0m" % private_file
	sys.exit()

def new_key(private_filename, public_filename):
        private, public = RSA_key.generate_RSA()
	with open(private_filename,'wb') as f:
		f.write(private)

	with open(public_filename,'wb') as f:
		f.write(public)
	return 'New key generated!'
if __name__ == '__main__':
  try:
	if sys.argv[1].strip() == '-y':
		if os.path.isfile(private_file)	 or os.path.isfile(private_file):
			option= raw_input( 'RSA Key is already exist, if you generate a new one, you will need to copy the public key to all the remote clients again. Do you want to continue? (enter yes to continue):')
			if option.strip() == 'yes':
				print new_key(private_file, public_file)
			else:
				sys.exit()
		else:
			print new_key(private_file, public_file)
  except IndexError:
	print 'No valid argument detected, try -h for helps.'
	sys.exit()


"""
string = 'Alexander'

# encrypt data with public key
p_code = RSA_key.encrypt_RSA(public_file, string)


# decrypt data with private key
decrypted_string= RSA_key.decrypt_RSA(private_file,  p_code)

#
if string == decrypted_string : print "YES"
"""




