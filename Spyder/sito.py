from math import sqrt
#n=200
def sito(n):
    tab = []
    for i in range (2,n+1):
        tab.append(i)
    for i in range(2,int(sqrt(n))+1):
        for j in range(2,n//i+1):
            if j*i in (tab):
                tab.remove(j*i)
    return tab
n = int(input("Podaj wielkoć listy: "))
print(sito (n))