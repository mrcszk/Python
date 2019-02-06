from random import randint
import math

length = int(input("Podaj rozmiar tablicy: "))

tab = []
for i in range(length):
    x = randint(0, 25)
    tab.append(x)

print("Nieposortowana tablica: ", tab)


def swap(tab, left, right):
    tab[left], tab[right] = tab[right], tab[left]

#sortowanie przez wybieranie
def selectsort(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        swap(tab, i, min)
    return tab

#sortowanie przez wstawianie
def insertsort(tab):
    for i in range(1, len(tab)):
        for j in range(i, 0, -1):
            if tab[j-1] > tab[j]:
                swap(tab, j-1, j)
    return tab

#sortowanie bąbelkowe
def bubblesort(tab):
    for i in range(len(tab)):
        #for j in range(1, len(tab)-1):
        if tab[i+1] > tab[i+2]:
            swap(tab, i+2, i+1)
    return tab

#sortowanie stogowe (kopcowanie)
def heapsort(tab):

    y = randint(0,10)   #pozbywamy się martwego punktu
    tab.insert(0,y)

    for i in range(0,len(tab)):   #budujemy kopiec
        j = i               #dziecko
        k = math.floor(j/2) #rodzic
        x = tab[i]
        while k > 0 and tab[k] < x:
            tab[j] = tab[k]
            j = k
            k = math.floor(j/2)
        tab[j] = x


    for i in range(len(tab)-1, 1, -1):  #rozbieramy kopiec
        swap(tab, 1, i)
        j = 1
        k = 2
        while k < i:
            if k+1<i and tab[k+1]>tab[k]:
                m = k + 1
            else:
                m = k
            if tab[m] <= tab[j]:
                break
            swap(tab, j, m)
            j = m
            k = j+j

    tab.remove(y)

    return tab

#sortowanie szybkie
def quicksort(tab, lewy, prawy):

    pivot = lewy
    l = lewy
    p = prawy


    while p > l:
        if pivot == l:
            if tab[p] < tab[pivot]:
                swap(tab, p, pivot)
                pivot = p
                l += 1
            else:
                p -= 1

        if pivot == p:
            if tab[l] > tab[pivot]:
                swap(tab, l, pivot)
                pivot = l
                p -= 1
            else:
                l += 1

    if p+1 < prawy:
        quicksort(tab, p+1, prawy)

    if l > lewy:
        quicksort(tab, lewy, l-1)

    return tab

tab1 = tab2 = tab3 = tab4 = tab5 = tab

print("Selectsort: ", selectsort(tab1))
print("Bubblesort: ", bubblesort(tab2))
print("Insertsort: ", insertsort(tab3))
print("Heapsort:   ", heapsort(tab4))
print("Quicksort:  ", quicksort(tab5, 0, length-1))