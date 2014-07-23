import sys

t=open('testread.py','wb')
with open(sys.argv[1], 'rb') as f:
	while True:
		data = f.read(100)
		if not data:break
		t.write( data)

t.close()
		
