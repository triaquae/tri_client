import key

"""
private, public = key.generate_RSA()

private_file, public_file = 'private.txt', 'public.txt'

with open(private_file,'wb') as f:
	f.write(private)

with open(public_file,'wb') as f:
	f.write(public)

"""

private_file, public_file = 'private.txt', 'public.txt'

p_code = key.encrypt_RSA(public_file, 'what the fuck...dfdfdf')


print key.decrypt_RSA(private_file,  p_code)
#print key.decrypt_RSA(public_file,  p_code)





