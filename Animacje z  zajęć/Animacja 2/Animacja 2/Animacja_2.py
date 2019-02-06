import random
random.seed()
import time
import os
def iks(x):
    for i in range(1):
        for j in range(11):
            if (j == x):
                print("x", end=' ')
            else:
                print("o", end=' ')
        print()
def pok(x):
    for i in range(x):
        for j in range(11):
            print("o", end=' ')
        print()
    print()
while True:
    a = random.randrange(11)
    b = random.randrange(11)
    c = random.randrange(11)
    d = random.randrange(11)
    e = random.randrange(11)
    f = random.randrange(11)
    g = random.randrange(11)
    h = random.randrange(11)
    i=7
    while i>=-1:
        if i<0:
            iks(h)
        if i<1:
            iks(g)
        if i<2:
            iks(f) 
        if i<3:
            iks(e)
        if i<4:
            iks(d)
        if i<5:
            iks(c)
        if i<6:
            iks(b)
        if -1<i<7:
            iks(a)
        pok(i)  
        i-=1
        time.sleep(1)
        os.system('cls')
