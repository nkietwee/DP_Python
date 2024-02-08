#!/usr/local/bin/python3

# your method definition here
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
def	famous_births(tmp_dict):
	for key, value in tmp_dict.items():
		print(f'{women_scientists[key]["name"]} is a great scientist born in {women_scientists[key]["date_of_birth"]}.' )

famous_births(women_scientists)
# Ada Lovelace is a great scientist born in 1815