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
    a1 = random.randint(1,6)
    b1 = random.randint(1,6)
    c1 = random.randint(1,6)
    a1 = int(a1)
    b1 = int(b1)
    c1 = int(c1)
    roll1 = a1 + b1 + c1
    a2 = random.randint(1,6)
    b2 = random.randint(1,6)
    c2 = random.randint(1,6)
    a2 = int(a2)
    b2 = int(b2)
    c2 = int(c2)
    roll2 = a2 + b2 + c2
    a3 = random.randint(1,6)
    b3 = random.randint(1,6)
    c3 = random.randint(1,6)
    a3 = int(a3)
    b3 = int(b3)
    c3 = int(c3)
    roll3 = a3 + b3 + c3
    a4 = random.randint(1,6)
    b4 = random.randint(1,6)
    c4 = random.randint(1,6)
    a4 = int(a4)
    b4 = int(b4)
    c4 = int(c4)
    roll4 = a4 + b4 + c4
    a5 = random.randint(1,6)
    b5 = random.randint(1,6)
    c5 = random.randint(1,6)
    a5 = int(a5)
    b5 = int(b5)
    c5 = int(c5)
    roll5 = a5 + b5 + c5
    a6 = random.randint(1,6)
    b6 = random.randint(1,6)
    c6 = random.randint(1,6)
    a6 = int(a6)
    b6 = int(b6)
    c6 = int(c6)
    roll6 = a6 + b6 + c6
    order = [roll1, roll2, roll3, roll4, roll5, roll6]
    order.sort()
    print(f"here are the numbers you rolled: {order}")
    stats = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]
    num1 = order[0]
    stats1 = input(f"what will you use the smallest number you rolled for? ({num1})? \n {stats}\n:")
    if stats1 in stats:
        stats.remove(stats1)
    num2 = order[1]
    stats2 = input(f"what will you use the second smallest number you rolled for? ({num2})? \n {stats}\n:")
    if stats2 in stats:
        stats.remove(stats2)
    num3 = order[2]
    stats3 = input(f"what will you use the third smallest number you rolled for? ({num3})? \n {stats}\n:")
    if stats3 in stats:
        stats.remove(stats3)
    num4 = order[3]
    stats4 = input(f"what will you use the third biggest number you rolled for? ({num4})? \n {stats}\n:")
    if stats4 in stats:
        stats.remove(stats4)
    num5 = order[4]
    stats5 = input(f"what will you use the second biggest number you rolled for? ({num5})? \n {stats}\n:")
    if stats5 in stats:
        stats.remove(stats5)
    stats6 = stats[0]
    num6 = order[5]
    print(f"here are your stats:\n{stats1}: {num1}\n{stats2}: {num2}\n{stats3}: {num3}\n{stats4}: {num4}\n{stats5}: {num5}\n{stats6}: {num6}")

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