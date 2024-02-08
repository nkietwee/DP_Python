#!/usr/local/bin/python3
try:
	nbr = int(input('Enter a number less than 25\n'))
	if(nbr > 25):
		print('Error')
	else:
		while(nbr <= 25):
			print(f'Inside the loop, my variable is {nbr}')
			nbr+=1
except :
	print("Error")