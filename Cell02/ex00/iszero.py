#!/usr/local/bin/python3
try :
	age = int(input())
	if(age == 0):
		print('This number is equal to zero.')
	else:
		print('This number is different from zero.')
except :
	print("Error")