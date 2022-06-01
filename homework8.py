#1
def triangle_area(b,h):
    area_ = 1/2 * b * h
    return(area_)
b = float(input("Base"))
h = float(input("Height"))
print("The area of a triangle is", triangle_area(b,h))
#2
def reverse_word(text):
    reversed_text = text[::-1]
    return reversed_text
text = input("text")
print(reverse_word(text))
#3
def upper_lower_count(my_word):
        check_upper_count = 0
        check_lower_count = 0
        for i in my_word:
            if i.isalpha():
                if i.isupper():
                    check_upper_count+=1
                else:
                    check_lower_count+=1
        print(f"Upper case letters: {check_upper_count} and lower case letters: {check_lower_count}")
        # return check_upper_count
        # return check_lower_count     nayel
my_word = input("Word")
upper_lower_count(my_word)
#4
def palindrom_checker(word):
    word_d = word.replace(" ", "")
    if word_d[::] == word_d[::-1]:
        print(word_d, "is palindrome")
    else:
        print(word_d, "isn't palindrome")
word = "AnnA"
palindrom_checker(word)
#5
def prime_or_not(number):
    a = 0
    for i in range(2, my_number):
        if my_number % i == 0:
            a += 1
    if a == 0:
        print(f"{my_number} is prime")
    else:
        print(f"{my_number} isn't prime")
    return a
my_number = int(input("Write your number"))
prime_or_not(my_number)
