with open("companies.txt") as f:
	name = f.readlines()
	print(name)
	for i in range(0, len(name)):
		print(name[i])
		name[i] = str(i + 1) + ' ' + name[i]

with open("scompanies.txt", "w") as f:
	f.writelines(name)