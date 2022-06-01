# # # 1 You need to use functions.
# # # Take two lists, say for example these two:
# # #  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # #  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # # # and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# # 1.1
# def common_elements(a: list, b:list):
# 	c = a + b
# 	d = list()
# 	for i in c:
# 		if i in a and i in b and d.count(i) == 0:
# 			d.append(i)
# 	return d
# a = [1, 1, 2, 3]
# b = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(common_elements(a, b))

# # 1.2
# def common_elements(a: list, b:list):
# 	d = list(set(a + b))
# 	return(d)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(common_elements(a, b))

# # 2 Write a Python program to remove duplicates from a list of lists.
# # Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# # New List : [[10, 20], [30, 56, 25], [33], [40]]

# def remove_dublicates(a: list):
# 	b = list()
# 	for i in a:
# 		if not(i in b):
# 			b.append(i)
# 	return b
# a = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# print(remove_dublicates(a))

# # 3 Write a Python program to flatten a given nested list structure.
# # Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# # Flatten list:
# # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# def flatten_list(a: list):
# 	b = list()
# 	for i in a:
# 		if type(i) == int:
# 			b.append(i)
# 		elif type(i) == list:
# 			for j in i:
# 				b.append(j)
# 	return(b)
# a = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# print(flatten_list(a))




# 3.2
def flattern_list(list_: list):
	if type(list_1) is not list:
		raise ValueError("You have provided not list object")
	new_list = []
	for i in list_1:
		if type(i) is int:
			new_list.append(i)
		else:
			new_list.extend(i)

# # # 4 Write a program (using functions!) that asks the user for a long string 
# # containing multiple words. Print back to the user the same string, except with 
# # the words in backwards order, (read about split() function). For example, say I type the string:
# # >>> My name is Tigran
# # # <<< Tigran is name My
# def my_word_in_backwards_order(text_first):
# 	a = list()
# 	text_in_backwards_order = text_first.split(" ", )
# 	text_in_backwards_order.reverse()
# 	print(text_in_backwards_order)
# text_first = input("Write your text in order \n")
# my_word_in_backwards_order(text_first)

# def flattern_list_buggy(list_1: list):
# 	print("perfect")