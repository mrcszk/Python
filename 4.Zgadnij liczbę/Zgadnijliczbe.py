import random

random.seed()
losowana = random.randrange(10)

a = int(input("Podaj liczbę: "))

while (a != losowana):

    if (a > losowana):
        print ("Liczba za duża.")
        a = int(input("Podaj liczbę: "))
    else:
        print ("Liczba za mała.")
        a = int(input("Podaj liczbę: "))
else:
    print ("Gratulacje, zgadłes.")
