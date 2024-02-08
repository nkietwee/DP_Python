#!/usr/local/bin/python3
try:
	arr =  [2, 8, 9, 48, 8, 22, -12, 2]
	new_arr = []
	for i in (arr): # i is value in arr
		new_arr.append(i + 2)
	# # other method
	# new_arr = arr.copy()
	# for i in range(len(arr)):
	# 	new_arr[i] = arr[i] + 2
	print(f'Original array: {arr}')
	print(f'New array: {new_arr}')
except:
	print("Error")
