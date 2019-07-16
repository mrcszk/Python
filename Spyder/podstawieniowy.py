def przygotowanie(tekst):
    tekst = tekst.lower()
    for i in tekst:
        if  ord(i)<97 or ord(i)>122:
            tekst = tekst.replace(i,'')
    return tekst

#funkcja generuj_alfabet() jest zrobiona tylko dla sportu
#zasadniczo możnaby od razu podać, że alfabet = "wietnamskybcdfghjlopqruvxz"
#ale się chciałam pobawić ;-)

def generuj_alfabet(jakieś_słowo):
    alfabet = jakieś_słowo
    for i in range(26):
        alfabet += chr(i+97)
    for i in jakieś_słowo:
        do_usunięcia = alfabet.rfind(i)
        alfabet = alfabet[:do_usunięcia] + alfabet[do_usunięcia+1:]
        print (alfabet)
    return alfabet

def podstawieniowy(tekst, alfabet):
    zaszyfrowany = ""
    for i in tekst:
        zaszyfrowany += alfabet[ord(i)-97]
    return zaszyfrowany

def dePodstawieniowy(kod, alfabet):
    odszyfrowany = ""
    for i in kod:
        #odszyfrowany += alfabet[(ord(i)+97)%26]
        odszyfrowany += chr(alfabet.find(i)+97)
    return odszyfrowany

alfabet = generuj_alfabet("wietnamsky")
print("Alfabet to:", alfabet)

string = input("Napisz coś: ")

string = przygotowanie(string)
print("Naprawione:", string)

string = podstawieniowy(string, alfabet)
print("Zaszyfrowane:", string)

string = dePodstawieniowy(string, alfabet)
print("Odszyfrowane:", string)

