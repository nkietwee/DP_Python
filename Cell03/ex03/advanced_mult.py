#!/usr/local/bin/python3

import sys
lenn = len(sys.argv)
if (lenn == 1):
	for i in range(0, 11):
		print(f"Table de {i} : ", end="")
		for j in range(0, 11):
			print(f"{i*j} ", end="")
		print()
else:
	print('none')
	



