#!/usr/local/bin/python3

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
def average(class_tmp):
	lenn = len(class_tmp)
	sum = 0
	for key in class_tmp.values():
		sum = sum + key
	return(sum / lenn)

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")