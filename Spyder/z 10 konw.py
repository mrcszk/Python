a = int(input("Podaj liczbe w systemie dziesietnym: "))
c = int(input("Podaj system na jaki chcesz zamienić:"))
#c = 5
lista= []

while a != 0:    
    b =  a % c
    if(b<10):
        lista.append(b)
    else:
        lista.append(chr(55 + b))
    a = a // c
print ("Twoja liczba w tym systemie wynosi: ", end='')
for e in reversed(lista):
    print (e, end='')
    
