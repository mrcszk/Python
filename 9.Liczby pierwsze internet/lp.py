import time

start_time = time.time()
n = 100


def primes(limit):
    tab = []  # robocza lista liczb pierwszych, poniewaz jest to generator to sie zachowuje miedzy wywolaniami
    for i in range(2, limit):  # rozwazamy liczby od 2 w górę ale mniejsze niż limit
        for j in tab:  # dla wszystkich do tej pory znalezionych liczb pierwszych
            if i % j == 0: break  # sprawdzamy czy ktoras jest dzielnikiem, jesli jest to i nie jest liczba pierwsza
        else:  # a jesli nie ma mniejszej od i liczby pierwszej z tab ktora jest jej dzielnikiem to i jest liczba pierwsza
            yield i
            tab.append(i)


for i in primes(n):
    print(i)

# tutaj wstaw obliczenia
print("--- %s seconds ---" % (time.time() - start_time))