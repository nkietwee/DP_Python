#!/usr/local/bin/python3
try:
	nbr = int(input("Enter a number\n"))
	for i in range(10):
		print(f'{i} x {nbr} = {i * nbr}')
except :
	print("Error")