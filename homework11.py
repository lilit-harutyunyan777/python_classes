# # 1. Write a Python script to concatenate following dictionaries to create a new one.
# # Sample Dictionary :

# # list_dict = [dict1, dict2, dict3, dict4]
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # # Try for as second version
# # dict1.update(dict2)
# # print(dict1)
# 1. 
def my_new_dictionary(dict1: dict):
	 dict5 = dict()
	 dict5.update(dict1)
	 dict5.update(dict2)
	 dict5.update(dict3)
	 dict5.update(dict4)
	 print(dict5)
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4={7:70,8:80}
my_new_dictionary(dict1)

# # 2. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# # Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def my_new_dict(my_dict1):
	my_dict1 = {}
	my_nums = range(1, n + 1)
	for i in my_nums:
		my_dict1[i] = i**2
	print(my_dict1)
n = int(input("number"))
my_new_dict(my_dict1)

# # 3. Write a Python program to drop empty Items from a given Dictionary.
# # Original Dictionary:
# # {‘c1’: ‘Red’, ‘c2’: ‘Green’, ‘c3’: None}
# # New Dictionary after dropping empty items:
# # {‘c1’: ‘Red’, ‘c2’: ‘Green’}
# # You need to use functions.

def my_dropped_dict(dict1: dict):
	for i in dict1.copy():
		if dict1.get(i) == None:
			dict1.pop(i, None)
	print(dict1)
dict1 = {"c1": "Red", "c2": "Green", "c3": None, "c5": "Yellow", "c6": None}
my_dropped_dict(dict1)



# 1 Write a Python program to create a shallow copy of sets.
# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
# 2. Write a Python program to find maximum and the minimum value in a set.
# 3. Write a Python program to find the elements in a given set that are not in another set