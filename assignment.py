#! python3

# SD Computing Studies Assignment

import random
import itertools 
score = 0
score = int(score)
def rand1():
    random1 = random.randint(1,100)
    random1 = float(random1)
    guess = input("\nguess the new number: ")
    guess = float(guess)
    def repeat():
        guess = input("guess the number: ")
        guess = float(guess)
        if guess > random1:
            print("that number is more than the random one\n")
        if guess < random1:
            print("that number is lower than the random one\n")
        if guess == random1:
            print(f"you got it! that was the number!")
            return False
        if guess != random1 or guess == 0:
            print("guess again!")
        return True
    if guess > random1:
        print("that number is more than the random one\n")
    if guess < random1:
        print("that number is lower than the random one\n")
    if guess == random1:
        print(f"you got it! that was the number!")
    if guess != random1 or guess == 0:
        print("guess again!")
    
    while True:
        if repeat() == False:
            rand1()
            break
        

def rand2():
    random2 = random.randint(1,2)
    random2 = int(random2)
    guess = input("\nguess heads or tails: ")
    if guess == "heads":
        if random2 == 1:
            print("\nyou got it! it was heads")
            rand2()
        else:
            print("\nsorry, but it was tails")
            rand2()
    elif guess == "tails":
        if random2 == 2:
            print("\nyou got it! it was tails")
            rand2()
        else:
            print("\nsorry, but it was heads")
            rand2()
    else: 
        print("\nsorry, but next time say either heads or tails")
        rand2()

def rand3():
    random3 = random.randint(1,3)
    random3 = int(random3)
    guess = input("\nrock, paper, or scissors? ")
    if guess == "rock":
        if random3 == 1:
            print("i choose... rock! looks like we tied")
            rand3()
        if random3 == 2:
            print("i choose... paper! looks like i win!")
            rand3() 
        if random3 == 3:
            print("i choose... scissors! looks like you won")
            rand3()
    elif guess == "paper":
        if random3 == 1:
            print("i choose... rock! looks like you won")
            rand3()
        if random3 == 2:
            print("i choose... paper! looks like we tied")
            rand3()
        if random3 == 3:
            print("i choose... scissors! looks like i win!")
            rand3()
    elif guess == "scissors":
        if random3 == 1:
            print("i choose... rock! looks i win!")
            rand3()
        if random3 == 2:
            print("i choose... paper! looks like you won")
            rand3()
        if random3 == 3:
            print("i choose... scissors! looks like we tied")
            rand3()
    else:
        print("next time say either rock, paper, or scissors")
        rand3()

def rand4():
    random4 = random.randint(1,6)
    random4 = int(random4)

if __name__ == "__main__":
    inval = ""
    while inval not in ['1','2','3','4']:
        print("\n\n\n")
        print("1. guess the number")
        print("2. heads or tails")
        print("3. rock paper scissors")
        print("4. dnd generator")
        inval = input("Choose an option: ")
    if inval == "1":
        rand1()
    if inval == "2":
        rand2()
    if inval == "3":
        rand3()
    if inval == "4":
        rand4()