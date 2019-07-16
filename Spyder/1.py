import random
import time

d=5
y=8
waz=[]
random.seed()
x=0
while x!=3:
    if x==0:
        a=random.randint(0,d-1)
        waz.insert(0,a)
        x+=1
    elif x==1:
        while True:
            a=random.randint(0,d-1)
            if a!=waz[0]:
                break
        waz.insert(0,a)
        x+=1
    else:
        while True:
            a=random.randint(0,d-1)
            if a!=waz[0] and a!=waz[1]:
                break
        waz.insert(0,a)
        x+=1
print(waz)

c=0
for m in range (0,4):
    
    for i in range (0, y):
        wiersz=''
        for j in range (0,d):
            if (waz[0]==j):
                wiersz+='x '
                c+=1
            else:
                wiersz+='o '
                
        if c==3:
            while True:
                a=random.randint(0,d-1)
                if a!=waz[0] and a!=waz[1] and a!=waz[2]:
                    break
            waz.insert(0,a)
            c=0
        print(wiersz)
    time.sleep(0.3)
    print('\n' *3)