#!/usr/local/bin/python3
import sys
import re

lenn = len(sys.argv)
if (lenn == 3):
	rea = re.findall(sys.argv[1], sys.argv[2])
	print(len(rea))
else:
	print("none")