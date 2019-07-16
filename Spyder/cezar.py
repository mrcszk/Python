# =============================================================================
# napis = input("Podaj tekst do zaszyfrowania: ").casefold()
# for char in napis:
# 	if not char.isalpha():
# 		napis = napis.replace(char,'')
# przesunięcie =13 
# napis2 = ''  
# for i in napis:
#     if ord(i) + przesunięcie <= 122:
#         napis2 += chr(ord(i)+przesunięcie)
#     else:
#         napis2 += chr(ord(i)+przesunięcie-26)
#     
# print(napis2)
# =============================================================================

def przygotowanie(tekst):
    tekst = tekst.lower()
    for char in tekst:
        if not char.isalpha():
            tekst = tekst.replace(char,'')
    return tekst

def cezar(tekst, przesunięcie):
    zaszyfrowany = ""
    przesunięcie = przesunięcie%26
    for i in tekst:
        if ord(i) + przesunięcie <= 122:
            zaszyfrowany += chr(ord(i)+przesunięcie)
        else:
            zaszyfrowany += chr(ord(i)+przesunięcie-26)
    return zaszyfrowany

def brutus(kod, przesunięcie):
    odszyfrowany = ""
    przesunięcie = przesunięcie%26
    for i in kod:
        if ord(i)-przesunięcie>=97:
            odszyfrowany += chr(ord(i)-przesunięcie)
        else:
            odszyfrowany += chr(ord(i)-przesunięcie+26)
    return odszyfrowany


string = input("Napisz coś: ")
przesunięcie = int(input("Podaj długość przesunięcia: "))

string = przygotowanie(string)
print("Naprawione:", string)

string = cezar(string, przesunięcie)
print("Zaszyfrowane:", string)

string = brutus(string, przesunięcie)
print("Odszyfrowane:", string)
