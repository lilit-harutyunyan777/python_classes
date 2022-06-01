
# 1. Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a python app which will ask day number, and return the day name (a string)

day_of_the_week = int(input("Day of the week"))

# print(int(day_of_the_week == 0) * "Saturday", int(day_of_the_week == 1) * "Sunday", int(day_of_the_week == 2) * "Monday", int(day_of_the_week == 3) * "Tuesday", int(day_of_the_week == 4) * "Wednesday", int(day_of_the_week == 5) * "Thursday", int(day_of_the_week == 6) * "Friday", sep = "")

if day_of_the_week == 0:
	print("Saturday")
if day_of_the_week == 1:
	print("Sunday")
if day_of_the_week == 2:
	print("Monday")
if day_of_the_week == 3:
	print("Tuesday")
if day_of_the_week == 4:
	print("Wednesday")
if day_of_the_week == 5:
	print("Thursday")
if day_of_the_week == 6:
	print("Friday")

# # # # 2. Write a python program which takes string as input then checks if there is a space in string ( it means that users inputed the word or the sentence ) then print message for both cases
# users_text = input("Write text here\n")
# space_check = " " in users_text
# print(int(space_check) * "there is a space", int(not(space_check)) * "there isn't a space", sep = "")


# # 2.1(After chatting in Slack:)))
# users_text = input("Write text here\n")
# if " " in users_text:
# 	print("there is a space")
# else:
# 	print("there isn't a space")



# # 3. Write a Python program to add ‘ing’ at the end of a given string (length should be at least 3). If the given string already ends with ‘ing’ then add ‘ly’ instead. If the string length of the given string is less than 3, leave it unchanged. Sample String : ‘abc’ Expected Result : ‘abcing’ Sample String : ‘string’ Expected Result : ‘stringly’
# # HINT:  endswith

# check_word = input("Write word")
# lenght_of_word = len(check_word)

# if lenght_of_word >= 3:
# 	print(int(not(check_word.endswith("ing"))) * (check_word + "ing"), int(check_word.endswith("ing")) * (check_word + "ly"), sep = "")
# else:
# 	print(check_word)


# # 4. Write a python program to check leap year without using datetime library

# check_year = int(input("Write year"))
# check_devidable_by_four = check_year % 4
# check_devidable_by_hundred = check_year % 100
# check_devidable_by_four_hundred = check_year % 400
# if check_devidable_by_four == 0 and check_devidable_by_hundred != 0:
# 	print("leap year")
# elif check_devidable_by_four == 0 and check_devidable_by_hundred == 0:
# 	print(int(not(bool(check_devidable_by_four_hundred))) * "leap year")