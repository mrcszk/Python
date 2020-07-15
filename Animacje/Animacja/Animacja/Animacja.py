import random
import time
import os
random.seed()
p=0
while True:
    while p<=7:
        for i in range(p):
            random.seed()
            a = random.randrange(11)
            for j in range(11):
                if (j == a):
                    print("x", end=' ')
                else:
                    print("o", end=' ')
            print()
        for i in range(7-p):
            for j in range(11):
                print("o", end=' ')
            print()
        print()
        p += 1
        time.sleep(0.3)
        os.system("cls")
    p=0
    


