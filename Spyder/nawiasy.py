class Nawias():
    def __init__(self, rodzaj):
        self.rodzaj = rodzaj
        self.next = None

class ListaNawiasow():
    def __init__(self):
        self.head = None
        self.rozmiar = 0

    def dodawanie(self, rodzaj):
        if self.head == None:
            nowy = Nawias(rodzaj)
            self.head = nowy
            self.rozmiar += 1
        else:
            nowy = Nawias(rodzaj)
            nowy.next = self.head
            self.head = nowy
            self.rozmiar += 1

    def usuwanie(self):
        self.head = self.head.next
        self.rozmiar -= 1

wyrazenie_nawiasowe = "[[()({())]]"
lista = ListaNawiasow()

for i in wyrazenie_nawiasowe:
    if i == '(' or i == '[' or i == '{':
        lista.dodawanie(i)
    elif i == ')':
        if lista.head.rodzaj == '(':
            lista.usuwanie()
        else:
            lista.dodawanie(i)
    elif i == ']':
        if lista.head.rodzaj == '[':
            lista.usuwanie()
        else:
            lista.dodawanie(i)
    elif i == '}':
        if lista.head.rodzaj == '{':
            lista.usuwanie()
        else:
            lista.dodawanie(i)

if not lista.rozmiar:
    print('Hurra! Wszystkie nawiasy sa zamkniete!')
else:
    print('Nie wszystkie nawiasy sa zamkniete!')