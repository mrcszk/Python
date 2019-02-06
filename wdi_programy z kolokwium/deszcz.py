from random import randint
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else'clear')


tab = ["O","O","O","O","O","O","O","O","O"]

while(1):
    for i in range(0,8):
        
        x = randint(0,8)
    
        tab[x] = "X" 
        print(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7],tab[8])
        tab[x] = "O"
        
    cls()
    
    time.sleep(0.3)
