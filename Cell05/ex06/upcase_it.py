#!/usr/local/bin/python3
import sys

lenn = len(sys.argv)

if (lenn == 2):
	for i in range(1, lenn):
		print(sys.argv[i].upper())
else:
	print("none")
