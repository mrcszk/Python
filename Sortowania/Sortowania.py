import random

random.seed()


def bąbelkowe(tablica):
    ilosc = len(tablica)
    for i in range(ilosc - 1):
        koniec = 1
        for j in range(ilosc - 1 - i):
            if (tablica[j] > tablica[j + 1]):
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
                koniec = 0
        if (koniec == 1):
            break


def przez_wybieranie(tablica):
    ilosc = len(tablica)
    for i in range(ilosc):
        minimum = i
        for j in range(i + 1, ilosc):
            if (tablica[j] < tablica[minimum]):
                minimum = j
        tablica[i], tablica[minimum] = tablica[minimum], tablica[i]


def przez_wstawianie(tablica):
    ilosc = len(tablica)
    for i in range(1, ilosc):
        element = tablica[i]
        j = i - 1
        while (tablica[j] > element and j >= 0):
            tablica[j + 1] = tablica[j]
            j -= 1
        tablica[j + 1] = element


def podział(p, k, tablica):
    j = p
    pivot = tablica[k]
    for i in range(p, k):
        if tablica[i] < pivot:
            t = tablica[i]
            tablica[i] = tablica[j]
            tablica[j] = t
            j += 1
    tablica[k] = tablica[j]
    tablica[j] = pivot
    return j


def szybkie(p, k, tablica):
    if p < k:
        s = podział(p, k, tablica)
        szybkie(p, s - 1, tablica)
        szybkie(s + 1, k, tablica)


def przez_scalanie(tablica):
    if len(tablica) > 1:
        środek = len(tablica) // 2
        L = tablica[:środek]
        P = tablica[środek:]

        przez_scalanie(L)
        przez_scalanie(P)

        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i] < P[j]:
                tablica[k] = L[i]
                i += 1
            else:
                tablica[k] = P[j]
                j += 1
            k += 1

        while i < len(L):
            tablica[k] = L[i]
            i += 1
            k += 1

        while j < len(P):
            tablica[k] = P[j]
            j += 1
            k += 1


def kopiec(tablica, n, root):
    najw = root
    l = 2 * root + 1
    p = 2 * root + 2
    if l < n and tablica[l] > tablica[najw]:
        najw = l

    if p < n and tablica[p] > tablica[najw]:
        najw = p
    if najw != root:
        tablica[root], tablica[najw] = tablica[najw], tablica[root]
        kopiec(tablica, n, najw)


def przez_kopcowanie(tablica):
    ilosc = len(tablica)
    for i in range(ilosc-1, -1, -1):
        kopiec(tablica, ilosc, i)
    for i in range(ilosc - 1, 0, -1):
        tablica[0], tablica[i] = tablica[i], tablica[0]
        kopiec(tablica, i, 0)


def kubełkowe(tab):
    ilosc = len(tab)
    kubełki = [[] for i in range(ilosc)]
    for i in range(ilosc):
        kubełki[tab[i] * ilosc // (max(tab) + 1)].append(tab[i])
    for i in range(ilosc):
        if len(kubełki[i]) > 1:
            przez_wstawianie(kubełki[i])
    j = 0
    for i in range(ilosc):
        for k in range(len(kubełki[i])):
            tab[j] = kubełki[i][k]
            j += 1


def funkcja(tablica, dzielnik):
    ilosc = len(tablica)
    sortowana = [0] * (ilosc)
    tmp = [0] * (10)
    for i in range(0, ilosc):
        indeks = (tablica[i] // dzielnik)
        tmp[(indeks) % 10] += 1
    for i in range(1, 10):
        tmp[i] += tmp[i - 1]
    i = ilosc - 1
    while i >= 0:
        indeks = (tablica[i] // dzielnik)
        sortowana[tmp[(indeks) % 10] - 1] = tablica[i]
        tmp[(indeks) % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(tablica)):
        tablica[i] = sortowana[i]


def pozycyjne(tablica):
    maks = max(tablica)
    dzielnik = 1
    while maks / dzielnik > 0:
        funkcja(tablica, dzielnik)
        dzielnik *= 10


tablica = [0] * 50
for i in range(50):
    tablica[i] = random.randint(1, 100)
print(tablica)

kopia = tablica[:]
bąbelkowe(kopia)
print(kopia)

kopia = tablica[:]
przez_wybieranie(kopia)
print(kopia)

kopia = tablica[:]
przez_wstawianie(kopia)
print(kopia)

kopia = tablica[:]
szybkie(0, len(kopia) - 1, kopia)
print(kopia)

kopia = tablica[:]
przez_scalanie(kopia)
print(kopia)

kopia = tablica[:]
przez_kopcowanie(kopia)
print(kopia)

kopia = tablica[:]
kubełkowe(kopia)
print(kopia)

kopia = tablica[:]
pozycyjne(kopia)
print(kopia)