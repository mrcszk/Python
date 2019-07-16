from math import sqrt
x = 8
y= 5
r = 3.0
size = 10 
tab = [['.']*(20) for i in range(size)]
for i in range (size):
    for j in range (20):
        p = (x-j)**2+(y-i)**2
        if float(sqrt(p))<=float(r):
            tab[i][j]=' '

for i in range(size) :
    print(" ".join(tab[i]))