def szukanie_dzielnikow(a):
    dzielniki = []
    for i in range(1,a):
        if not a%i:
            dzielniki.append(i)
    return dzielniki
def sumowanie_dzielnikow(a):
    dzielniki = szukanie_dzielnikow(a)
    suma = 0
    for i in range(len(dzielniki)):
        suma += dzielniki[i]
    return suma
n = int(input("Podaj liczbe, do ktorej bedziemy szukac liczb doskonalych: "))
print ("Liczby doskonale:", end = ' ')
for k in range (1,n):
    if sumowanie_dzielnikow(k) == k:
        print (k, end = ', ')
       
print("\nliczby zaprzyjaźnione:")
for k in range(1,n):
  suma_k = sumowanie_dzielnikow(k)
  suma_j = sumowanie_dzielnikow(suma_k)
  if k == suma_j:
    if not k == suma_k:
      print(k, suma_k)
      
# =============================================================================
# for i in range(2,10000):
#    liczba=i 
#    suma_dzielnikow=0 
#    for j in range(i-1,0,-1):
#      if liczba%j==0:
#        suma_dzielnikow+=j 
#    if suma_dzielnikow==liczba:
#        print(liczba)
# =============================================================================
    