#!/usr/local/bin/python3
import sys

lenn = len(sys.argv)
if (lenn == 3):
	lst = []
	start = int(sys.argv[1])
	end = int(sys.argv[2])
	if (start < end):
		for i in range(start, end+1):
			lst.append(i)
	print(lst)
else:
	print('none')