#!/usr/local/bin/python3
import sys

lenn = len(sys.argv)
if (lenn == 2):
	cnt = sys.argv[1].count('z')
	print('z' * cnt if cnt > 0 else "none")
else:
	print('none')