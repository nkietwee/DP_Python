#!/usr/local/bin/python3
try :
	first_nbr = int(input('Enter the first number:\n'))
	second_nbr = int(input('Enter the second number:\n'))
	result = first_nbr * second_nbr
	print(f'{first_nbr} x {second_nbr} = {result}')
	if(result > 0):
		print('The result is positive.')
	elif (result < 0):
		print('This result is negative.')
	else:
		print('This result is both positive and negative.')
except :
	print("Error")