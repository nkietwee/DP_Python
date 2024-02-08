#!/usr/local/bin/python3
try :
	password = "Python is awesome"
	input_passwd = input()
	print('ACCESS GRANTED' if input_passwd == password else 'ACCESS DENIED')
except:
	print("Error")
# if (input_passwd == password):
# 	print('ACCESS GRANTED')
# else:
# 	print('ACCESS DENIED')
