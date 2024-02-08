#!/usr/local/bin/python3
import sys

lenn = len(sys.argv)
if (lenn != 1):
	print(f'parameters: {lenn - 1}')
	for i in range(1, lenn):
		print(f'{sys.argv[i]}: {len(sys.argv[i])}')

else:
	print('none')