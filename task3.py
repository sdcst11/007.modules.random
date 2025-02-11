    #!python3
import random
while True :
    x = random.randint(1,3)
    if x == 1 :
        x = "rock"
    if x == 2 :
        x = "paper" 
    if x == 3 :
        x = "scissors"
    y = str(input("please choose either rock, paper or scissors : "))
    if x == y :
        print(f"The computer also picked {x} tie game!")
    elif x == "paper" and y == "rock" :
        print(f"The computer picked {x} you lose!")
    if x == "paper" and y == "scissors" :
        print(f"The computer picked {x} you Win!")
    elif x == "rock" and y == "paper" :
        print(f"The computer picked {x} you Win!")
    if x == "rock" and y == "scissors" :
        print(f"the computer picked {x} you Lose!")
    elif x == "scissors" and y == "paper" :
        print(f"the computer picked {x} you Lose!")
    if  x == "scissors" and y == "rock":
        print(f"the computer picked {x} You Win")
    menu = int(input("Please select and option (1)exit program (2)Run program again\nSELECTION: "))
    if menu == 1:
        print("exiting...")
        exit()