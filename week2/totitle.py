aStr = 'What do you think "No Pain, No Gain"?'
tempStr = aStr.split('\"')
print(tempStr)
if tempStr[1].istitle():
	print('%s is the title' % tempStr[1])
else:
	print('%s is not the title' % tempStr[1])