i = -1
a = int(input("Podaj liczbe w systemie dziesietnym: "))
c = int(input("Podaj system na jaki chcesz zamienić:"))
lista= []
while a != 0:
    i += 1
    b =int( a % c)
    if(b<=9):
        lista.insert(i, b)
    else:
        lista.insert(i, chr(55 + b))
    a = a // c

print ("Twoja liczba w tym systemie wynosi: ", end='')
for e in reversed(lista):
    print (e, end='')