i = 0
a = int(input("Podaj liczbe w systemie binarnym: "))
b = 0

while a != 0:
    c = a % 10
    a = a// 10
    b += c * (2 ** i)
    i += 1;

print("Twoja liczba w systemie dziesiętnym wynosi:", b);
