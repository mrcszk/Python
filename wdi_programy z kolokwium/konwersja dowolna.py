liczba=int(input("Wpisz dowolną liczbę: "))
sys=0
sys1= int(input("Z jakiego systemu? "))
while sys<2 or sys>36:
    sys=int(input("Wpisz podstawę(od 2 do 36): "))
    if sys<2 and sys>36:
        print ("Wpisz podstawę od 2 do 36: ")
liczba1=0
mnoznik=1
while liczba:
    reszta=liczba%10
    liczba = liczba//10
    liczba1 += reszta*mnoznik
    mnoznik*=sys1
wynik=""
wynik1=""
mnoznik=1
while liczba1:
    reszta=liczba1%sys
    liczba1 = liczba1//sys
    if (reszta<=9):
        wynik += str(reszta)
    else:
        wynik += chr(65+reszta-10)
for i in range (len(wynik)):
    wynik1 += wynik[len(wynik)-i-1]
print ("Wynik przeliczenia na system docelowy to: ", wynik1)   