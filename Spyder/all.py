#1
#liczby doskonale

# for i in range(2,10000):
#   liczba=i 
#   suma_dzielnikow=0 
#   for j in range(i-1,0,-1):
#     if liczba%j==0:
#       suma_dzielnikow+=j 
#   if suma_dzielnikow==liczba:
#     print(liczba)
    


#2
#palindrom

#def odwracanie(napis):
  #return napis[::-1]
  
#def palindrom(napis):
  #odwrotny=odwracanie(napis)
  #if odwrotny==napis:
    #return True
  #else:
    #return False
    
#napis=input("Podaj interesujący cię napis, aby sprawdzić, czy jest palindromem:")
#odpowiedz=palindrom(napis.lower())

#if odpowiedz==1:
  #print("To jest palindrom")
#else:
  #print("To nie jest palindrom")
  


#3
#deszcz

#from random import randint
#import time 
#import os 

#def cls():
  #os.system('cls' if os.name=='nt' else 'clear')
  
#tab=["O","O","O","O","O","O","O","O","O"]

#while (1):
  #for i in range(0,8):
    #x=randint(0,8)
    #tab[x]="X"
    #print(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7],tab[8])
    #tab[x]="O"
  #cls()
  #time.sleep(0.3)
  
  
  
#4
#deszcz z tablicą dwuwymiarową

#from random import randint
#import time 

#size=int(input("Podaj rozmiar: "))

#while True:
  #board=[["O" for i in range (size)] for j in range (size)]
  #for i in range(1,size):
    #time.sleep(0.5)
    #x=randint(1,size)
    #board[x-1][i]="X"
    #for j in range(size):
      #print(board[j][i],end=" ")
    #board[j][x-1]="O"
    #if j==size-1:
      #print("\n")
      
      

#5      
#fibbonaci

#def fib_rek(n):
  #if n==0:
    #return 0 
  #if n==1:
    #return 1 
  #else:
    #return fib_rek(n-2)+fib_rek(n-1)
    
#print("rekurencyjnie:")
#print(fib_rek(0))
#print(fib_rek(1))
#print(fib_rek(2))
#print(fib_rek(3))
#print(fib_rek(5))
#print(fib_rek(7))
#print(fib_rek(13))

#def fib_iter(n):
  #if n==0:
    #return 0 
  #if n==1:
    #return 1 
  #else:
    #f1=f2=1 
    #for i in range(2,n):
      #temp=f1+f2
      #f1=f2
      #f2=temp
    #return f2
    
#print("iteracyjnie:")
#print(fib_iter(0))
#print(fib_iter(1))
#print(fib_iter(2))
#print(fib_iter(3))
#print(fib_iter(5))
#print(fib_iter(7))
#print(fib_iter(13))



#6
#trojkat Pascala

# def trojkat_pascala(k,w):
#   if k==1 or k==w:
#     return 1 
#   else:
#     return trojkat_pascala(k-1,w-1)+trojkat_pascala(k,w-1)
    
# n=int(input("podaj wysokosc: "))
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(str(trojkat_pascala(j,i)),end="")
#   print()
  
  
  
#7
#liczby zaprzyjaznione

#def szukanie_dzielinikow(a):
  #dzielniki=[]
  #for i in range(1,a):
    #if not a%i:
      #dzielniki.append(i)
  #return dzielniki
  
#def sumowanie_dzielnikow(a):
  #dzielniki=szukanie_dzielinikow(a)
  #suma=0
  #for i in range(len(dzielniki)):
    #suma+=dzielniki[i]
  #return suma
  
#n=int(input("Podaj gorny zakres: "))
#for k in range(1,n):
  #suma_k=sumowanie_dzielnikow(k)
  #suma_j=sumowanie_dzielnikow(suma_k)
  #if k==suma_j:
    #if not k==suma_k:
      #print(k,suma_k)
      
#8
#piątki 13tego

#nazwy_miesiecy=['styczen','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien','wrzesien','pazdziernik','listopad','grudzien']
#ilosc_dni_miesiaca=[31,28,31,30,31,30,31,31,30,31,30,31]
#dzien_miesiaca=1 
#dzien_tygodnia=1 
#ile=0 

#print("Piatki 13tego w latach 2001-2014")
#for i in range(2001,2015):
  #print("rok: "+str(i))
  #ilosc_dni_miesiaca[1]=28
  #if i%4==0:
    #ilosc_dni_miesiaca[1]=29
  #ob_miesiac=0
  #while ob_miesiac<12:
    #dzien_miesiaca+=1
    #dzien_tygodnia+=1
    #if dzien_miesiaca > ilosc_dni_miesiaca[ob_miesiac]:
      #dzien_miesiaca=1 
      #ob_miesiac+=1 
    #if dzien_tygodnia>7:
      #dzien_tygodnia=1 
    #if dzien_miesiaca==13 and dzien_tygodnia==5:
      #print(nazwy_miesiecy[ob_miesiac])
      #ile+=1
      
#print("Piatek 13tego wystapil "+str(ile)+" razy")



#9 ???
#nawiasy

#class Nawias():
  #def _init_(self,rodzaj):
    #self.rodzaj=rodzaj
    #self.next=None
    
#class ListaNawiasow():
  #def _init_(self):
    #self.head=None
    #self.rozmiar=0 
    
  #def dodawanie(self,rodzaj):
    #if self.head==None:
      #nowy=Nawias(rodzaj)
      #self.head=nowy
      #self.rozmiar+=1 
    #else:
      #nowy=Nawias(rodzaj)
      #nowy.next=self.head
      #self.head=nowy
      #self.rozmiar+=1 
      
  #def usuwanie(self):
    #self.head=self.head.next
    #self.rozmiar-=1
    
#wyrazenie_nawiasowe='[[()({()})]]'
#lista=ListaNawiasow()

#for i in wyrazenie_nawiasowe:
  #if i=='(' or i=='[' or i=='{':
    #lista.dodawanie(i)
  #elif i==')':
    #if lista.head.rodzaj=='(':
      #lista.usuwanie()
    #else:
      #lista.dodawanie(i)
  #elif i=='[':
    #if lista.head.rodzaj==']':
      #lista.usuwanie()
    #else:
      #lista.dodawanie(i)
  #elif i=='}':
    #if lista.head.rodzaj=='{':
      #lista.usuwanie()
    #else:
      #lista.dodawanie(i)
      
#if not lista.rozmiar:
  #print("Wszystkie nawiasy sa zamkniete")
#else:
  #print("Nie wszystkie nawiasy sa zamkniete")
  
  
  
#10 
#waz na sawannie

#import random
#import os 
#import time

#size=int(input("podaj rozmiar sawanny: "))
#tab=[["."]*size for i in range (size)]
#leng=3 
#line=0 

#while True:
  #for i in range(size-1,0,-1):
    #for j in range(size):
      #tab[i][j]=tab[i-1][j]
  #if leng==3:
    #leng=0 
    #flag=1
    #while flag:
      #line=random.randrange(0,size)
      #for j in range(size):
        #if tab[j][line]=='x':
          #break
        #if j==size-1:
          #flag=0 
  #for i in range(size):
    #if (tab[1][i]=='.') or (tab[1][i]=='x' and tab[2][i]=='x' and tab[3][i]=='x'):
      #tab[0][i]='.'
    #else:
      #tab[0][i]='x'
  #tab[0][line]='x'
  #for j in range(size):
    #print("".join(tab[j]))
  #time.sleep(0.5)
  #os.system('cls')
  #leng+=1
  
  
  
#11 
#sortowanie

#import random
#tablica_liczb=[]
#for i in range(50):
  #tablica_liczb.append(random.randrange(50))
#print("Nieposortowana tablica liczb: ",tablica_liczb)

#def sortowanie_babelkowe(tablica_liczb):
  #for i in range(len(tablica_liczb)-1,0,-1):
    #for j in range(i):
      #if tablica_liczb[j]>tablica_liczb[j+1]:
        #tablica_liczb[j],tablica_liczb[j+1]=tablica_liczb[j+1],tablica_liczb[j]
#sortowanie_babelkowe(tablica_liczb)
#print("Posortowana tablica liczb(sortowanie babelkowe): ",tablica_liczb)
  
#def sortowanie_przez_wybieranie(tablica_liczb):
  #for i in range(len(tablica_liczb)-1,0,-1):
    #max=0 
    #for j in range(i):
      #max=j 
    #temp=tablica_liczb[j]
    #tablica_liczb[j]=tablica_liczb[max]
    #tablica_liczb[max]=temp 
#sortowanie_przez_wybieranie(tablica_liczb)
#print("Posortowana tablica liczb(sortowanie przez wybeiranie): ",tablica_liczb)

#def sortowanie_przez_wstawianie(tablica_liczb):
  #for i in range(1,len(tablica_liczb)):
    #j=i-1
    #while j>=0  and tablica_liczb[j]>tablica_liczb[i]:
      #tablica_liczb[j+1]=tablica_liczb[j]
      #j=j-1 
      #tablica_liczb[j+1]=tablica_liczb[i]
#sortowanie_przez_wstawianie(tablica_liczb)
#print("Posortowana tablica liczb: ", tablica_liczb)



#12 
#konwersja dowolona systemów liczbowych

