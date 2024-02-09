#!/usr/local/bin/python3
import math
try:
	nbr = input('Give me a number: ')
	def isint(nbr):
		try:
			int(nbr)
			return(True)
		except ValueError:
			return(False)

	def isfloat(nbr):
		try:
			float(nbr)
			return(True)
		except ValueError:
			return(False)

	if (isint(nbr) == True):
		print(math.ceil(int(nbr)))
	elif (isfloat(nbr) == True):
		print(math.ceil(float(nbr)))
	else:
		print("Error")
except:
	print("Error")
