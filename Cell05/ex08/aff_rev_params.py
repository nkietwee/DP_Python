#!/usr/local/bin/python3
import sys
lenn = len(sys.argv)

if (lenn == 1 or lenn == 2):
	print("none")
else:
	for i in range(lenn - 1, 0, -1):
		# print(i)
		print(sys.argv[i])