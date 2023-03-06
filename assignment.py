#! python3

# SD Computing Studies Assignment

import random

def rand1(max):
    random1 = random.randint(1,100)
    guess = ""
    random1 = int(random1)
    guess = int(guess)
    while guess not in random1:
        print("guess the number!")
    guess = input("guess the number!")
    if guess > random1:
        print("that number is lower than the random one\n")
    if guess < random1:
        print("that number is more than the random one\n")
    if guess == random1:
        print("you got it! that was the number")
    