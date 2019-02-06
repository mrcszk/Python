def przygotowanie(tekst):
    tekst = tekst.lower()
    for i in tekst:
        if  ord(i)<97 or ord(i)>122:
            tekst = tekst.replace(i,'')
    return tekst

def cezar(tekst, przesunięcie):
    zaszyfrowany = ""
    for i in tekst:
        if ord(i) + przesunięcie <= 122:
            zaszyfrowany += chr(ord(i)+przesunięcie)
        else:
            zaszyfrowany += chr(ord(i)+przesunięcie-26)
    return zaszyfrowany

def deCezar(kod, przesunięcie):
    odszyfrowany = ""
    for i in kod:
        if ord(i)-przesunięcie>=97:
            odszyfrowany += chr(ord(i)-przesunięcie)
        else:
            odszyfrowany += chr(ord(i)-przesunięcie+26)
    return odszyfrowany


print("Napisz coś: ", end="")
string = input()

print("Podaj długość przesunięcia: ", end="")
przesunięcie = int(input())

string = przygotowanie(string)
print("Naprawione:", string)

string = cezar(string, przesunięcie)
print("Zaszyfrowane:", string)

string = deCezar(string, przesunięcie)
print("Odszyfrowane:", string)
