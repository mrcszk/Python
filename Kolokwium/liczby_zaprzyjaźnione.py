#program wypisujący pary liczb zaprzyjaźnionych mniejszych od n

def szukanie_dzielnikow(a):
  dzielniki = []
  for i in range(1,a):
    if not a%i:
      dzielniki.append(i)
  return dzielniki
  
def sumowanie_dzielników(a):
  dzielniki = szukanie_dzielnikow(a)
  suma = 0
  for i in range(len(dzielniki)):
    suma += dzielniki[i]
  return suma
  
n = int(input("Podaj liczbe n:"))

print("liczby zaprzyjaźnione:")
for k in range(1,n):
  suma_k = sumowanie_dzielników(k)
  suma_j = sumowanie_dzielników(suma_k)
  if k == suma_j:
    if not k == suma_k:
      print(k, suma_k)

print("liczby doskonałe:")      
for k in range(1,n):
  if sumowanie_dzielników(k) == k:
    print(k)