import random

random.seed()

tab = [0]*50

for i in range (50):
    tab[i]= random.randint(1,100)
for i in range(len(tab)):
    minimum = i
    for j in range (i+1,len(tab)):
        if tab[j]<tab[minimum]:
            tab[j],tab[minimum]=tab[minimum],tab[j]
            
print (tab)