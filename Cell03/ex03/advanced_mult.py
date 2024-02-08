#!/usr/local/bin/python3
try:
	import sys
	lenn = len(sys.argv)
	if (lenn == 1):
		for i in range(11):
			sum = 0
			print(f'Table de {i} :', end =" ")
			for j in range(11):
				print(f'{sum}', end =" ")
				sum = sum + i
			# print('\n')
			print('\n', end = "")
	else:
		print('none')
		exit()
except:
	print("Error")