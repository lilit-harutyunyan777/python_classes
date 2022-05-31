# 13. Write a Python function to print the numbers of a given list after removing even numbers from it


# def my_num_after_removing(my_list_: list):
# 	my_new_list = []
# 	for i in my_list_:
# 		if i % 2 != 0:
# 			my_new_list.append(i)
# 	print(my_new_list)

# my_list_ = [2, 7,5,8]
# my_num_after_removing(my_list_)


# set_1 = {1, 2, 3, 4, 1, 1}
# print(set_1)


# list_1 = [1, 1, 1, 5, 6]

# print(list(set(list_1)))


set_1 = set()
set_1.add(1)

set_1 = {1, 3, 5}
set_2 = {2, 3, 4}


result = set_1.difference(set_2)
print(result)

set_1.difference_update(set_2)
print(set_1)