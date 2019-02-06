import random

random.seed()
losowana = random.randrange(10)

a = int(input("Podaj liczbę: "))
while True:
    if (a == losowana):
        print ("Gratulacje, zgadłes.")
        break;
    else:
        if (a > losowana):
            print ("Liczba za duża.")
            a = int(input("Podaj liczbę: "))
        else:
            print ("Liczba za mała.")
            a = int(input("Podaj liczbę: "))

