#!/usr/local/bin/python3
try:
	nbr = int(input('Please tell me your age: '))
	print(f'You are currently {nbr} years old.')
	for i in range(10, 31, 10):
		print(f'''In {i} years, you'll be {nbr + i} years old.''')
except:
	print("Error")