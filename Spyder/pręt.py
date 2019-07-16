import math
def pierwsze(n):
    if (n < 2):
        return False
    for i in range (2,int(math.sqrt(n))):
        if (n % i == 0):
            return False
        i+=1
    return True
string = input("Podaj liste liczb: ")
lista = string.split()
lista2 = [0] * len(lista)
a=0
b=0
bylo = 0
for i in range(len(lista)):
    lista[i] = int(lista[i])
for i in range(len(lista)):
    for j in range(a):
        if lista2[j] == lista[i]:
            lista2[a] = lista[i]
            a += 1
            bylo = 1
            break
    if bylo == 0:
        for j in range (0,len(lista)):
            if lista [i] == lista[j]:
                b+=1
        if b%2==1 :
            w = pierwsze(lista[i])
            if w is True:
                b=0
                continue
            else:
                lista2[a] = lista[i]
                a += 1
        else:
            lista2[a] = lista[i]
            a += 1
        b=0
    else:
        bylo = 0


print ("Liczby: ")
for a in lista2:
    if a!=0:
        print (a, end=' ')
