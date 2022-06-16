from random import randint
import abc
from abc import ABC


class CowsAndBullsBase(ABC):
    def __init__(self):
        self.cows = 0
        self.bulls = 0
        self.number = None
        self.tries = 1

    def generate_num(self):
        num = ""
        while len(num) < 4:
            digit = str(randint(0, 9))
            if digit not in num:
                num += digit

        self.number = num
        print(self.number)

    def present(self):
        return f"cows: {self.cows} and bulls: {self.bulls}"

    @staticmethod
    def user_guess():
        guess = input("guess the number ")
        while not guess.isdigit() or len(guess) != 4:
            # raise ValueError("wrong value for guessing")
            guess = input("wrong value for guessing,guess the number ")
        return guess

    def reset_values(self, hard=False):
        self.cows, self.bulls = 0, 0
        self.tries += 1
        if hard:
            self.generate_num()
            self.tries = 0

    def check(self, guess):
        if guess == self.number:
            self.cows = 4
            return

        for i in range(4):
            if guess[i] in self.number:
                if guess[i] == self.number[i]:
                    self.cows += 1
                else:
                    self.bulls += 1

    def won(self):
        print(f"{self.present()}\n------{self.number}------\nYou have tried {self.tries} times")

    def play(self):
        tries = int(input("How many time do you want to try?"))
        while self.tries <= tries:
            self.generate_num()
            self.check(self.user_guess())
            if self.cows != 4:
                print(self.present())
            else:
                self.won()
                self.reset_values()
            self.tries += 1


my_game = CowsAndBullsBase()
my_game.play()