    #!python3
    #Bad dnd character roller
import random 
def menu() :
    menu = input("select an option: (1)Exit program (2)Run program again")
    if menu == 1 :
        exit()
def characterRoll() :
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    stats = ["null","strength","intelligence","wisdom","dexterity","constitution","charisma"]
    print(f"rolling dice now.....\n\nYou rolled{r1,r2,r3}!\n\n That means your character has {stats[r1]}, {stats[r2]} and {stats[r3]}!")
characterRoll()
menu()





