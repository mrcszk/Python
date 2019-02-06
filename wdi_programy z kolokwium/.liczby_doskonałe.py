#program wypisujący liczby doskonałe mniejsze od n

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

for k in range(1,n):
  if sumowanie_dzielników(k) == k:
    print(k)