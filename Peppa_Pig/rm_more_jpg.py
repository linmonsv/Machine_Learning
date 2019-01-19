import os, sys

path = "train/000"
dirs = os.listdir(path)

rm_file_names = []
for file in dirs:
	file_ext = file.split('.')
	if file_ext[1] == 'jpg':
		tmp_file_name = file_ext[0] + '.xml'
		if tmp_file_name not in dirs:
			rm_file_names.append(file)
rm_file_names.sort()
for file in rm_file_names:
	print('rm', os.path.join(path, file))
	os.system('rm -rf ' + os.path.join(path, file))

