#!/usr/local/bin/python3
import sys

lenn = len(sys.argv)
if (lenn == 2):
	prompt = input('What was the parameter? ')
	if (prompt == sys.argv[1]):
		print('Good job!')
	else:
		print('Nope, sorry...')
else:
	print('none')