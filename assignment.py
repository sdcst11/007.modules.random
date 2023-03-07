#! python3

# SD Computing Studies Assignment

import random
import itertools 

def rand1(max):
    random1 = random.randint(1,100)
    random1 = float(random1)
    guess = input("guess the number: ")
    guess = float(guess)
    total = 1
    total = int(total)
    def repeat():
        guess = input("guess the number: ")
        guess = float(guess)
        if guess > random1:
            print("that number is more than the random one\n") and total + 1
        if guess < random1:
            print("that number is lower than the random one\n") and total + 1
        if guess == random1:
            print(f"you got it! that was the number! your total guesses was: {total}")
            return False
        if guess != random1 or guess == 0:
            print("guess again!")
        return True
    if guess > random1:
        print("that number is more than the random one\n") and total + 1
    if guess < random1:
        print("that number is lower than the random one\n") and total + 1
    if guess == random1:
        print("you got it! that was the number")
    if guess != random1 or guess == 0:
        print("guess again!") and total + 1
    
    while True:
        if repeat() == False:
            break

if __name__ == "__main__":
    inval = ""
    while inval not in ['1']:
        print("\n\n\n")
        print("1. guess the number")
        inval = input("Choose an option:")
    if inval == "1":
        rand1(max)