#!/usr/local/bin/python3
import sys

lenn = len(sys.argv)
if (lenn == 1):
	print("none")
else:
	for i in range(1, lenn):
		print(sys.argv[i].lower())

