# # Homework:
# # 1. Write a Python program to construct the following pattern, using for loops. (image_1)
for i in range(10):
	print(i * "*")


for i in range(10):
	for j in range(i):
		print("*", end ="")

	print()



# # # 2. Write a python program to count number of even digits in a number (ex: 2135 >>> 1)
count_num = 0
my_number = input("my number is\n")
for even_dig in my_number:
	if even_dig.isdigit() and int(even_dig) % 2 == 0:
		count_num += 1
	else:
		pass
print(count_num)

# # # # 3. Given a range of first 10 numbers, Iterate from start number to the end
# # #  number and print the sum of the current number and previous number(image_2)

for i in range(1,11):
	print("{} * {} = {}".format(i, i + 1,i*(i+1)))


# # # 4.1 Given a string, display only those characters which are present under even index number.

# my_name = input("Your name\n")
# for i in my_name:
#     index_num = my_name.find(i)
#     if index_num % 2 == 0:
#     	print(i)
#     else:
#         pass


# 4.2
my_second_name = my_name[::2]
print(my_second_name)

# # # 5. Create a program that asks the user for a number and then prints out all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# # #my_number = int(input("Your number: "))
my_number = int(input("Your number: "))
for i in range(1, my_number + 1):
    if my_number % i == 0 :
        print (i)
    else:
       pass
        

