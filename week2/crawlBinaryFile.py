import requests
#how to save binary file
r = requests.get('https://www.baidu.com/img/bd_logo1.png')
with open('logo.png', mode = 'wb') as f:
	f.write(r.content)