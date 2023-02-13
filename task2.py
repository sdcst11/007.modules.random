    #!python3
    #coin toss
import random 
while True :
    y = str
    x = random.randint(1,2)
    if x == 1 :
        x = "heads"
    if x == 2 :
        x = "tails"
    y = str(input('Guess "heads" or "tails" here.'))
    if x != y :
        print("Incorrect!")
    if x == y :
        print("you guessed it correct!")
        menu = int(input("Please select an option (1)Exit program (2) Run program again"))
        if menu == 1 :
            exit()

    
        
    
        
        