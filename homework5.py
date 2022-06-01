# # # # # 1. Write a python program to check whether a number is divisible by 5 or 11 or not.
# # my_number = int(input("Write number\n"))
# # if not(my_number) % 5 or not(my_number % 11):
# # 	print("Divisible by 5 or 11")
# # else:
# # 	print("Not divisible by 5 or 11")
# # # # #2.Write an app that takes a number. If the number is divisible by 3, it should return “Fizz”. If it is divisible by 5, it should return “Buzz”. If it is divisible by both 3 and 5, it should return “FizzBuzz”. Otherwise, it should return the same number.
# # my_number = int(input("Write number\n"))
# # if not(my_number) % 3 and my_number % 5:
# # 	print("Fizz")
# # elif my_number % 3 and not(my_number % 5):
# # 	print("Buzz")
# # elif not(my_number % 3) and not(my_number % 5):
# # 	print("FizzBuzz")
# # else:
# # 	print(my_number)


 
# # # # # # 3 #Write a Python program to find the first appearance of the substring ‘not’ and ‘poor’ from a given string,
# # # # #  if ‘not’ follows the ‘poor’, replace the whole ‘not’...‘poor’ substring with ‘good’. 
# # # # #  Return the resulting string.
# # # # # #  ex.1
# # # # # #  Sample String : ‘The lyrics is not that poor!’
# # # # # #  Expected Result : ‘The lyrics is good!’
# # # # # # ex.2
# # # # # #   Sample String : ‘The lyrics is poor!’
# # # # # #   Expected Result : ‘The lyrics is poor!’

# # sample_sentence = input("Write your text here\n")
# # my_new_sentence = sample_sentence.replace("not", "good")
# # if sample_sentence.find("not") < sample_sentence.find("poor"):
# # 	print(my_new_sentence[0:(sample_sentence.index("not")+4):1])
# # else:
# # 	print(sample_sentence)




sentence = input("write")
not_index = sentence.find("not")
poor_index = sentence.find("poor")
if not_index >= 0 and poor_index > not_index:
	sentence = sentence.replace(sentence[not_index: poor_index +4], "good")
print(sentence)
# # # # 4. Write a Python program to get a string from a given string where all occurrences of its first char 
# # # # have been changed to ‘$’, except the first char itself. Go to the editor
# # #  ex.1
# # # # 	Sample String : ‘restart’
# # # #  	Expected Result : ‘resta$t’
# # # # ex.2
# # # #   	Sample String : ‘abacdaa’
# # # #  	Expected Result : ‘ab$cd$$’
# # my_word = input("Write your word\n")
# # first_letter = ord(my_word[0])
# # my_new_word = my_word.replace(chr(first_letter), "$") 
# # my_finally_word = chr(first_letter) + my_new_word[1::1]
# # # print(my_finally_word)


# # # new_sentence = sentence[0] + sentence[1].replace(sentence[0], "$")
# # # print(new_sentence)



# # # name = input("tell your name\n")

# # # sentence = f"hello {name}"
# # # # print(sentence)

# # word ="Hello Python"

# # for i in word:
# # 	print(i)

# # # # for i in range(4):
# # # # 	print(i)

# # name = input("tell your name\n")
# # amount_of_prints = int(input("how many"))
# # sentence = f"hello {name}"
# # for i in range(amount_of_prints):
# # 	print(sentence)


# # for i in range(6):
# # 	if i % 2 == 0:
# # 		print("even")
# # # 	else:
# # # 		print("odd")

# # print()
# # for num in range(11):
# # 	print("{} * 5 = {}". format(num, num * 5))


# # user_num = int(input("tell the number: "))

# # for i in range(user_num)
# # 	if i % 15 == 0:
# # 		print("FizzBuss")

# # 	elif i % 3 == 0:
# # 		print("Fizz")
# # 	elif i % 5 == 0:
# # 		print("Buzz")
# # 	else:
# # 		print("")

# ​
# from datetime import datetime as dt
# ​
# year_str = str(dt.now().year)
# sum_of_digits = 0
# for digit in year_str:
# 	sum_of_digits += int(digit)
# print(sum_of_digits)



# text = "a0b0c0sfsf"
# count_num = 0
# if text[0].isdigit():
# 	count_num +=1
# if text[1].isdigit():
# 	count_num +=1
# if text[2].isdigit():
# 	count_num +=1
# if text[3].isdigit():
# 	count_num +=1


# text = "a0b0c0sfsf"
# count_num = 0
# count_letters = 0
# for dig in text:
# 	if dig.isdigit():
# 		count_num += 1
# 	elif dig.isalpha():
# 		count_letters += 1

# text = "a0b0c0sfsf"
# count_num = 0
# count_letters = 0

# for dig in text:
# 	if dig.isdigit():
# 		if int(dig) % 2 == 0
# 		count_num += 1
# 	elif dig.isalpha():
# 		count_letters += 1

# text = "a0b0c0sfsf"
# sum_num = 0
# count_letters = 0

# for j in text:
# 	if j.isdigit():
# # 		sum_num += int(j)

# text = "a0b0"
# count_num = 0

# for i in text:
# 	if i.isdigit() and False:
# 		count_num +=1
# 	else:
# # 		print("couldn't find")
# # 		continue
# # 	print("I've found one more number")

# text = "0755a0b0"
# count_num = 0

# for i in text:
# 	if i.isdigit() and False:
# 		count_num +=1
# 	else:
# 		print("couldn't find")
# # 		break
# # 	print("I've found one more number")

# sum_ = 0
# for i in range (1,21):
# 	if i == 3 or i == 13
# 	continue

# 	sum_ += i


# 	if sum  or i == 13
# 	continue

# 	sum_ += i