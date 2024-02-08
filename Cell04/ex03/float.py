#!/usr/local/bin/python3
def isint(nbr):
	# global nbrr
	try:
		nbrr = int(nbr)
		# print("int")
		return(True)
	except ValueError:
		return(False)

def isfloat(nbr):
	# global nbrr
	try:
		nbrr = float(nbr)
		# print("float")
		return(True)
	except ValueError:
		return(False)

nbr = input('Give me a number: ')
# print(float(nbr))
# print(round(int(nbr)))
if(isint(nbr) == True):
	print('This number is an integer.')
elif(isfloat(nbr) == True ):
	print('This number is an decimal.')
else:
	print('Not number')


# if (isinstance(nbr, int)):
# 	print('This number is an integer.')
# elif (isinstance(nbr, float)):
# 	print('This number is an float.')