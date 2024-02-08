#!/usr/local/bin/python3

import sys

lenn = len(sys.argv)
if (lenn == 1):
	print("none")
else:
	for i in range(1, lenn):
		len_arg = len(sys.argv[i])
		if (len(sys.argv[i]) < 8):
			print(sys.argv[i], end="")
			for j in range(8 - len_arg):
				print('Z', end="")
			print("\n", end="")
		else:
			for k in range(8):
				print(sys.argv[i][k], end="")
			print("\n", end="")


