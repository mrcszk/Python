from random import randint
import time

size = int(input("Podaj rozmiar: "))

while True:
    board = [["O" for i in range(size)] for j in range(size)]
    for i in range(size):
        time.sleep(0.5)
        x=randint(1,size)
        board[x-1][i] = "X"
        for j in range(size):
            print(board[j][i], end=" ")
        board[j][x-1] = "O"
        if j==size-1:
            print("\n")
    print("\n"*100)