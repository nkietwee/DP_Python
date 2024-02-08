#!/usr/local/bin/python3
try:
	strr = input()
	for i in range(len(strr)):
		# print(strr[i])
		if (strr[i] >= 'a' and strr[i] <= 'z'):
			print(strr[i].upper(), end='')
		elif (strr[i] >= 'A' and strr[i] <= 'Z'):
			print(strr[i].lower(), end='')
		else:
			print(strr[i], end='')
	print('\n', end='')
			# strr[i] = str
except:
	print("Error")