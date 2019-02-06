a = int(input("Podaj długosć boku 1: "))
b = int(input("Podaj długosć boku 2: "))
c = int(input("Podaj długosć boku 3: "))

if (a>0 and b>0 and c>0 and (a+b)>c and (a+c)>b and (b+c)>a):
    p = (a+b+c)/2

    import math
    wynik = math.sqrt(p*(p-a)*(p-b)*(p-c))

    print("Pole wynosi: ",wynik)

else:
    print ("Podałes błędne dane.")