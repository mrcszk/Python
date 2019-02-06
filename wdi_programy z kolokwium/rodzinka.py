import sys

class Czlek:
 
    def __init__(self, nazwa,o,m):
        self.nazwa = nazwa
        self.o = o
        self.m = m
        self.dzieci=[]
 
    def __str__(self):
        return str(self.nazwa)
 
def wyszukaj(nazwa,n):
    if(n.nazwa==nazwa):
        return n
    for i in range(0,len(n.dzieci)):
        if(wyszukaj(nazwa,n.dzieci[i])!=None):
            return wyszukaj(nazwa,n.dzieci[i])
def wypisz(n,il):
    for i in range(0,il):
        sys.stdout.write (" ")
    print(n.nazwa)
    for i in range(0,len(n.dzieci)):
        wypisz(n.dzieci[i],il+1)
 
class drzewo:
 
    def __init__(self,nazwa):
        n=Czlek(nazwa,None,None)
        self.praszczor = n
        
    def dodajpotomka(self,nazwa,o,m):
        nowy=Czlek(nazwa,None,None)
        n=self.praszczor
        n=wyszukaj(o,self.praszczor)
        if(n!=None):
            n.dzieci.append(nowy)
            nowy.o=n
        n=wyszukaj(m,self.praszczor)
        if(n!=None):
            n.dzieci.append(nowy)
            nowy.m=n
        if(nowy.o==None and nowy.m==None):
            print ("niestety",nazwa," nie nalezy do rodziny")
        #n=Czlek(nazwa,o,m)
        #if(o!=None):
        #    o.dzieci.append(n)
        #if(m!=None):
        #    m.dzieci.append(n)
drz=drzewo('Adam')
drz.dodajpotomka('Kain','Adam',None)
drz.dodajpotomka('Abel','Adam',None)
drz.dodajpotomka('Ham','Abel',None)
drz.dodajpotomka('Ewa','Adam',None)
drz.dodajpotomka('Hame','Abel','Ewa')

wypisz(drz.praszczor,0)