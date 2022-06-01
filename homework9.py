# # # # # 1. Write a function that takes two tuples and checks if they are the same

def the_same_tuples(first_tuple: tuple, second_tuple: tuple):
	valid_ = 1
	if len(first_tuple) == len(second_tuple):
		for i in first_tuple:
			if i in second_tuple and first_tuple.count(i) == second_tuple.count(i):
				check = True
			else:
				check = False
		valid_ = valid_ * check
		return(bool(valid_))
	else:
		return(False)
first_tuple = (1, 3, 5, "Abc")
second_tuple = ("Abc",1, 5, 3, 1)
print(the_same_tuples(first_tuple, second_tuple))


# 2. Write a function that takes tuples and checks if their letter counts are the same:
# 	ex. check_string_amount((“Abc”, “d”, False, “gh”), (“a”, “and”, “gh”, 5) >>> True
# # 
def letter_counts(first_tuple: tuple, second_tuple: tuple):
	letter_count_first = 0
	letter_count_second = 0
	for i in first_tuple:
		if type(i) == str:
			letter_count_first += len(i)
	for j in second_tuple:
		if type(j) == str:
			letter_count_second += len(j)
	if letter_count_first == letter_count_second:
		return True
	else:
		return False
first_tuple = (7,"ABCyvaa",3, False,)
second_tuple = (5,"K",3, False,"Aaaxx")

print(letter_counts(first_tuple, second_tuple))


# # 3. Write a function that takes two tuples and returns a new tuple with common values
# # 	ex. (1, 3, 4) (3, 5, 6) >>> (3,)
def new_tuple(first_tuple: tuple, second_tuple: tuple):
	my_new_tuple = tuple()
	for i in first_tuple:
		if i in second_tuple:
		  my_new_tuple += (i,)
	return(my_new_tuple)
first_tuple = (1, 20, "Hi")
second_tuple = (1,"Hello", "Hi","BMW",True)
print(new_tuple(first_tuple, second_tuple))

# # 4. Write a function that takes a tuple and returns new version without duplicate values of it.

def remove_dublicates(my_tuple,):
	my_new_tuple = tuple()
	for i in my_tuple:
		if not(i in my_new_tuple):
			my_new_tuple += (i,)
	return(my_new_tuple)
my_tuple = (1, 5, "Pass", True, "Exam", 1, "Exam")
print(remove_dublicates(my_tuple))
