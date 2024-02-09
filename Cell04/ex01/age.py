#!/usr/local/bin/python3
try:
	nbr = int(input('Please tell me your age: '))
	if(nbr <= 0):
		print("Age should be morethan 0")
		exit()
	print(f'You are currently {nbr} years old.')
	for i in range(10, 31, 10):
		print(f'''In {i} years, you'll be {nbr + i} years old.''')
except:
	print("Error")