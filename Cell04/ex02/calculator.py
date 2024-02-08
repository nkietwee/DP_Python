#!/usr/local/bin/python3
try:
	first_nbr = int(input('Give me the first number: '))
	second_nbr = int(input('Give me the second number: '))
	print('Thank you!')
	sym = ('+' ,'-' ,'*', '/')
	for i in sym:
		print(f'{first_nbr} {i} {second_nbr} = {eval(str(first_nbr) + str(i) + str(second_nbr))}')
except:
	print("Error")

# other method

# print(f'{first_nbr} + {second_nbr} = {first_nbr + second_nbr}')
# print(f'{first_nbr} - {second_nbr} = {first_nbr - second_nbr}')
# print(f'{first_nbr} * {second_nbr} = {first_nbr * second_nbr}')
# print(f'{first_nbr} / {second_nbr} = {first_nbr / second_nbr}')



