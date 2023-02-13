#! python3
#number guessing game 
import random
x = random.randint(1,100)
y = 0
count = 0 
while True :
    count = count+1
    y = int(input("Try to guess a number from 1 - 100! you're guess here: "))
    if x > y :
        print("Try guessing a higher number!")
    if y > x : 
        print("try guessing a lower number")
    if x == y :
        print(f"The number was {x} and you guessed it in only {count} tries!")
        break

# SD Computing Studies Assignment
