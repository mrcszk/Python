import time
import math

zakres = int(input("Podaj zakres poszukiwania liczb pierwszych: "))
start_time = time.time()
liczba = 2
while liczba <= zakres:
    dzielnik = 1
    dzielniki = 0
    sqrt = int(math.sqrt(liczba))
    while dzielnik <= sqrt:
        if ((liczba) % (dzielnik) == 0):
            dzielniki += 1
        dzielnik += 1
    if dzielniki <= 1:
        print(liczba)

    liczba += 1

print("Program trwał %f sekund/y." % (time.time() - start_time))
