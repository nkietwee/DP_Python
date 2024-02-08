#!/usr/local/bin/python3

# your method definition here
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_redheads(dictt):
	lst = []
	for key, values in dictt.items():
		if (values == "red"):
			lst.append(key)
	return(lst)

print(find_the_redheads(dupont_family))