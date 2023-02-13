    #!python3
    #Better dnd character roller
import random 
stats = ["discarded","strength","intelligence","wisdom","dexterity","constitution","charisma"]
def menu() :
    menu = int(input("select an option: (1)Exit program (2)Roll 4 dice discard lowest (3)roll 3 dice reroll ones (4)standard 3 dice roll"))
    if menu == 1 :
        exit() 
    elif menu == 2 :
        print(r4dl())
    if menu == 3 :
            r3r1()
    elif menu == 4 :
        characterRoll()
def characterRoll() :
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    print(f"rolling dice now.....\n\nYou rolled{r1,r2,r3}!\n\n That means your character has {stats[r1]}, {stats[r2]} and {stats[r3]}!")
def r4dl():
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    r4 = random.randint(1,6)
    lowest = min(r1,r2,r3,r4) 


    print(f"you rolled {r1,r2,r3,r4} the lowest was {lowest} and will be discarded leaving you with {stats[r1]}, {stats[r2]} and {stats[r3]}" )
def r3r1():
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    if r1 == 1 or r2 == 1 or r3 == 1 :
        r1 = random.randint(2,6)
        r2 = random.randint(2,6)
        r3 = random.randint(2,6)
        print(f"You rolled {r1,r2,r3}")
    elif r1 and r2 and r3 != 1 :
        print(f"You're final rolls are {r1,r2,r3}")
            
            
        
    
menu()
    





