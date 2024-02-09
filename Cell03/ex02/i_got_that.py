#!/usr/local/bin/python3
try:
	prompt = input('What you gotta say? : ')
	if (prompt == "STOP"):
		exit()
	while(True):
		word = input('I got that! Anything else? : ')
		if (word == "STOP"):
			break
except:
	print(end="")



