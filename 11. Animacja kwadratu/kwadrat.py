import random
random.seed()
import time
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
a = random.randrange(11)
b = random.randrange(11)
c = random.randrange(11)
d = random.randrange(11)
e = random.randrange(11)
f = random.randrange(11)
g = random.randrange(11)
i=7
while i>=0:
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
    if i<7:
        iks(a)
    pok(i)
    i-=1
    time.sleep(0.3)