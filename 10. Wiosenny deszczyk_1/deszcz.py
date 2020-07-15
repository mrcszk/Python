import random
import time
import os

# for i in range(7):
#   for j in range(11):
#   print("o", end=' ')
#   print()
# print()


random.seed()
a = random.randrange(11)
time.sleep(0.3)
p = 0
# os.system("cls")
while p <= 7:
    for i in range(p):
        random.seed()

        b = random.randrange(11)
        for j in range(11):

            if ((j == a and i == p) or j == a + b):
                print("x", end=' ')
            else:
                print("o", end=' ')
        print()
    for i in range(7 - p):
        for j in range(11):
            print("o", end=' ')
        print()
    print()
    p += 1
    time.sleep(0.3)
    os.system("cls")
#   def clear_screen():
#      print('\033[2J\033[0;0H')

