import random
import time
import os

size=int(input("Podaj rozmiar sawanny: ")) #XD
tab = [['.']*size for i in range(size)]
line=0
leng=3
while True:
    for i in range(size-1,0,-1):
        for j in range(size):
            tab[i][j]=tab[i-1][j]
    if leng==3:
        leng=0
        flag=1
        while flag:
            line=random.randrange(0,size)
            for j in range(size):
                if tab[j][line]=='x':
                    break
                if j==size-1:
                    flag=0
    for j in range(size):
        if (tab[1][j] == '.') or (tab[1][j] == 'x' and tab[2][j] == 'x' and tab[3][j] == 'x'):
            tab[0][j] = '.'
        else:
            tab[0][j] = 'x'
    tab[0][line]='x'
    for i in range(size):
        print("".join(tab[i]))
    time.sleep(0.3)
    os.system('cls')
    leng +=1