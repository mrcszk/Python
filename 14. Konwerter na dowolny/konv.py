i = 0
a = int(input("Podaj liczbe: "))
f = int(input("W jakim systemie jest Twoja liczba: "))
c = int(input("Podaj system na jaki chcesz zamienić:"))
b = 0

while a != 0:
    d = a % 10;
    a = int(a / 10);
    b += d * (f ** i)
    i += 1;

# print("Twoja liczba w systemie dziesiętnym wynosi:",b);

i = 0
a = b
lista = []
while a != 0:
    i += 1
    b = int(a % c)
    if (b <= 9):
        lista.insert(i, b)
    else:
        lista.insert(i, chr(55 + b))
    a = a // c
print("Twoja liczba w tym systemie wynosi: ", end='')
for e in reversed(lista):
    print(e, end='')