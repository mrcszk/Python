def cezar(zdanie):
    zdanie.lower()
    for i in zdanie:
        if (ord(i) <= 122 and ord(i) >= 97):
            zdanie = zdanie.replace(i, )


zdanie = input("Podaj zdanie:")
cezar(zdanie)
print(zdanie)