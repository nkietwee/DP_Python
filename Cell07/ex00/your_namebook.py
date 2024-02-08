#!/usr/local/bin/python3

# your method definition here
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
def	array_of_names(tmp_dict):
	lst = []
	for key , value in tmp_dict.items():
		tmp = key[0].upper() + key[1:] + ' ' + value[0].upper() + value[1:]
		lst.append(tmp)
	return(lst)


print(array_of_names(persons))