a = int(input("Podaj liczbę n>=2: "))
e = 1
s = a
i = 2
while (e <= a):
    while (i <= e):
        print(" " * i)
        print(" " * s, "x" * i)
        i += 2
        s -= 1

    e += 2
    i = 1
    s = a
