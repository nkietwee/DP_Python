#!/usr/local/bin/python3
import sys

lenn = len(sys.argv)
if (lenn == 1):
	print('none')
else:
	for i in range(1, lenn):
		if (sys.argv[i].endswith("ism") == False):
			print(sys.argv[i], end='')
		else:
			print(sys.argv[i])
		# cnt = sys.argv[i].endswith("ism")
	print()