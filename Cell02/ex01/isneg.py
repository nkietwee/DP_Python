#!/usr/local/bin/python3
try :
	age = int(input())
	if(age > 0):
		print('This number is positive.')
	elif (age < 0):
		print('This number is negative.')
	else:
		print('This number is both positive and negative.')
except :
	print("Error")