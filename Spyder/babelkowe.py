import random
tab = [0]*100

for i in range (100):
    tab[i] = random.randint(1,100)
    
for i in range (len(tab)-1):
    i = 0
    for j in range (len(tab)-1-i):
        if (tab[j]>tab[j+1]):
            tab[j],tab[j+1] = tab[j+1],tab[j]
            print(tab)
            i=1
    if i ==0:
        break
print (tab)
