    #!python3
    #auto hand dealer
from itertools import count
import random
deck = ["As","Ac","Ad","Ah","2s","2c","2d","2h","3s","3c","3d","3h","4s","4c","4d","4h","5s","5c","5d","5h","6s","6c","6d","6h","7s","7c","7d","7h","8s","8c","8d","8h","9s","9c","9d","9h","10s","10c","10d","10h","Js","Jc","Jd","Jh","Qs","Qc","Qd","Qh","Ks","Kc","Kd","Kh",]
random.shuffle(deck)
count=0
def hands() :
    a = deck[1]
    b = deck[2]
    c = deck[3]
    d = deck[4]
    e = deck[5]
    f = deck[6]
    g = deck[7]
    h = deck[8]
    i = deck[9]
    j = deck[10]

    print(f"player one's hand is {a,b,c,d,e}\nPlayer twos hand is {f,g,h,i,j}")


def main():
    hands()
    
main()

    
