# # # 1.Let’s try a to find factorial of a number. To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example: 3! is equal to 1x2x3
a = 1
my_number = int(input("Write your number"))
for i in range(1, my_number + 1):
    a = a * i
print(f"{my_number}! is equal to {a}")

# # # 2.Write a Python program to construct the following pattern, using for loops.

# # # *
# # # * *
# # # * * *
# # # * * * *
# # # * * * * *
# # # * * * *
# # # * * *
# # # * *
# # # *


# # # 2.
for i in range(1,10):
    if i <= 5:
        print (i * "*")
    else:
        print ((10-i) * "*")

# 2.1
i = 0
while i < 5:
    print (i * "*")
    i = i + 1
while i < 10:
    print ((10-i) * "*")
    i = i + 1

# # # 3.  0,1,1,2,3,5,8,13,21
a = 0
b = 1
while a <= 50:
	print(a)
	c = a + b
	a = b
	b = c


# # 4.
import random
first_player_score = 0
second_player_score = 0
sum_first_player_score = 0
sum_second_player_score = 0
round = int(input("How many times do you want to play"))
for i in range(1,round+1):
    first_players_step = random.randint(1,3)
    second_players_step = random.randint(1,3)
    if first_players_step == 1:
        if second_players_step == 2:
            second_player_score += 1
        elif second_players_step == 3:
            first_player_score += 1
        else:
            pass
    if first_players_step == 2:
        if second_players_step == 1:
            first_player_score += 1
        elif second_players_step == 3:
            second_player_score += 1
        else:
            pass
    if first_players_step == 3:
        if second_players_step == 1:
            second_player_score += 1
        elif second_players_step == 2:
            first_player_score += 1
        else:
            pass
    print("Round", i ,f"First player's step is {first_players_step} and Second player's step is {second_players_step}")
    print(f"Score  {first_player_score} : {second_player_score}")
sum_first_player_score += first_player_score
sum_second_player_score += second_player_score

print(f"Game Over\nGame result is {sum_first_player_score}:{sum_second_player_score}")
