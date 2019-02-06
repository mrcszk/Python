def dodawanie (a,b):
    return (a+b)
def odejmowanie (a,b):
    return a-b
def mnozenie (a,b):
    return a*b
def dzielenie (a,b):
    if (b==0):
        print ("Nie dziel przez 0")
        return ("0")
    return a/b
def potęgowanie (a,b):
    return a**b

def menu():
    print ("1.Dodawanie")
    print ("2.Odejmowanie")
    print ("3.Mnozenie")
    print ("4.Dzielenie")
    print ("5.Potegowanie")


a = int(input("Podaj liczbe a:"))
b = int(input("Podaj liczbe b:"))

c = input("Co chcesz zrobic?")
if(c=='+'):
    print("a + b =",dodawanie(a,b))
if(c=='-'):
    print("a - b =",odejmowanie(a,b))
if(c=='*'):
    print("a*b =",mnozenie(a,b))
if(c=='/'):
    print("a/b =",dzielenie(a,b))
if(c=='^'):
    print("a^b =",potęgowanie(a,b))