# =============================================================================
# 
# 
# from random import randint
# import time
# import os
# 
# def cls():
#     os.system('cls' if os.name=='nt' else'clear')
# n=0
# 
# tab = ["O","O","O","O","O","O","O","O","O"]
# 
# while(n<10):
#     for i in range(0,8):
#         
#         x = randint(0,8)
#     
#         tab[x] = "X" 
#         print(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7],tab[8])
#         tab[x] = "O"
#         
#     os.system('clear')
#     n+=1
#     time.sleep(0.3)
# =============================================================================
    
import random
import time
import os
#for i in range(7):
 #   for j in range(11):
     #   print("o", end=' ')
 #   print()
#print()



random.seed()

time.sleep(0.3)
p=0
#os.system("cls")
while p<=7:
    for i in range(p):
        a = random.randrange(11)
        for j in range(11):

            if (j == a):
                print("X", end=' ')
            else:
                print("O", end=' ')
        print()
    for i in range(7-p):
        for j in range(11):
            print("O", end=' ')
        print()
    print()
    p += 1
    time.sleep(0.3)
    os.system("cls")
# =============================================================================
# import time
# import random
# import os
#  
# EMPTY = 0       # index "pustego powietrza"
# TOKEN = 'ox'    # oznaczenia
# #TOKEN = u' ♪'    # alternatywne oznaczenia (wymagana czcionka unicode)
# SIZE  = 10      # rozmiar tablicy
# INTERVAL = 1    # częstotliwość odświeżania planszy
#  
# # plansza SIZExSIZE
# board = [[TOKEN [EMPTY] for _ in range (SIZE)] for _ in range (SIZE)]
#  
# while True:
#    # nowy (górny) wiersz
#    new_row = [random.choice (TOKEN) for _ in range (SIZE)] 
#    # dodaj "na górze" planszy
#    board.insert (0, new_row)
#    # usuń ostatni wiersz planszy
#    del board [-1]
#  
#    # wyświetl planszę
#    for row in board:
#        print (''.join (row))
#  
#    # opóźnienie
#    time.sleep (INTERVAL)
#    # reset terminala
#    os.system ('clear')
# 
# =============================================================================
