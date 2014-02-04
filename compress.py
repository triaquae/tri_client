import zlib,tarfile

def tar(file_list,target_file):
	with tarfile.open(target_file, 'w') as t:
		for filename in file_list:
			t.add(filename)
	return target_file
def untar(tar_file_name,target_path):
	t = tarfile.open(tar_file_name)
	t.extractall(path= target_path)
	t.close()

def compress(source_file, target_file, level=9):
    source_file = open(source_file, 'rb')
    target_file = open(target_file, 'wb')
    compress = zlib.compressobj(level)
    data = source_file.read(1024)
    while data:
        target_file.write(compress.compress(data))
        data = source_file.read(1024)
    target_file.write(compress.flush())
    return target_file
def decompress(source_file, target_file):
    source_file = open(source_file, 'rb')
    target_file = open(target_file, 'wb')
    decompress = zlib.decompressobj()
    data = source_file.read(1024)
    while data:
        target_file.write(decompress.decompress(data))
        data = source_file.read(1024)
    target_file.write(decompress.flush())


#decompress('test.dd.z','test.dd2')
