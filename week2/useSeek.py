s = 'Tencent'
with open('companies.txt', mode = 'a+') as f:
	f.writelines('\n')
	f.writelines(s)
	f.seek(0, 0)
	names = f.readlines()
	for name in names:
		print(name)