import os
print(os.getcwd())
print(os.listdir())

os.mkdir(f"{os.getcwd()}/Dir1")
os.mkdir(f"{os.getcwd()}/Dir1/Dir2")
os.makedirs(f"{os.getcwd()}/Dir1/Dir3/Dir4")
open('readme.txt', 'w')
my_answer = input("Do you want to delete all folders?/ Y or N\n")
if my_answer == "Y":
    os.rmdir(f"{os.getcwd()}/Dir1/Dir3/Dir4")
    os.rmdir(f"{os.getcwd()}/Dir1/Dir3")
    os.rmdir(f"{os.getcwd()}/Dir1/Dir2")
    os.rmdir(f"{os.getcwd()}/Dir1")

