def przygotowanie(tekst):
    tekst = tekst.lower()
    for i in tekst:
        if  ord(i)<97 or ord(i)>122:
            tekst = tekst.replace(i,'')
    return tekst

def zKluczem(tekst, klucz):
    zaszyfrowany = ""
    k = 0
    for i in tekst:
        j = klucz[k%len(klucz)]
        przesunięcie = ord(j) - 96
        if ord(i) + przesunięcie <= 122:
            zaszyfrowany += chr(ord(i)+przesunięcie)
        else:
            zaszyfrowany += chr(ord(i)+przesunięcie-26)
        k += 1

    return zaszyfrowany

def deZKluczem(kod, klucz):
    odszyfrowany = ""
    k = 0
    for i in kod:
        j = klucz[k%len(klucz)]
        przesunięcie = ord(j) - 96
        if ord(i)-przesunięcie>=97:
            odszyfrowany += chr(ord(i)-przesunięcie)
        else:
            odszyfrowany += chr(ord(i)-przesunięcie+26)
        k += 1
    return odszyfrowany


print("Napisz coś: ", end="")
string = input()

print("Podaj klucz: ", end="")
klucz = input()
klucz = przygotowanie(klucz)

string = przygotowanie(string)
print("Naprawione:", string)

string = zKluczem(string, klucz)
print("Zaszyfrowane:", string)

string = deZKluczem(string, klucz)
print("Odszyfrowane:", string)
