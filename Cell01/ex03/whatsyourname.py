#!/usr/local/bin/python3
try:
	first_name = input('''Hey, what's your first name? : ''')
	last_name = input('And your last name? : ')
	print(f'Well, pleased to meet you, {first_name} {last_name}.')
except:
	print("\nError")
	# return(print("\nError"))