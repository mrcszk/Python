class Node:

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.name)

    def __int__(self):
        return int(self.score)

class myList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #wypisywanie listy od pocz±tku
    def printFromBeginning(self):

        n = self.head
        while n:
            print (n.name, n.score)
            n = n.next

    #wypisywanie listy od koñca
    def printFromEnd(self):

        n = self.tail
        while n:
            print (n.name, n.score)
            n = n.prev


    #dodawanie na pocz±tku listy
    def addAtBeginning(self, name, score):

        n = Node(name, score)
        n.prev = None
        n.next = self.head
        self.head = n
        self.size +=1
        if not self.tail:
            self.tail = n
        else:
            n.next.prev = n


    #dodawanie elementu na koñcu listy
    def addAtEnd(self, name, score):

        n = Node(name, score)
        n.next = None
        n.prev = self.tail
        self.tail = n
        self.size += 1
        if not self.head:
            self.head = n
        else:
            n.prev.next = n


    #dodawanie na N-tej pozycji listy
    def addAtN(self, name, score):

        print("Podaj numer miejsca (od 1 do " + str(self.size + 1) + "):")
        N = int(input())
        if N == 1:
            _list1.addAtBeginning(name,score)
        elif  N == self.size + 1:
            _list1.addAtEnd(name, score)
        elif N > self.size + 1 or N < 1:
            print("Poda³e¶ z³± pozycjê.")
        else:
            k = self.head
            for i in range (N-1):
                k = k.next
            newer = Node(name, score)
            newer.next = k
            newer.prev = k.prev
            self.size += 1
            k.prev.next = newer
            k.prev = newer


    #usuwanie pierwszego elementu listy
    def removeFromBeginning(self):

        n = self.head
        n.next.prev = None
        self.head = n.next
        self.size -= 1


    #usuwanie ostatniego elementu listy
    def removeFromEnd(self):

        n = self.tail
        n.prev.next = None
        self.tail = n.prev
        self.size -= 1

    #szukanie osoby z najwiêksz± liczb± punktów
    def findHighestScore(self):

        n = self.head
        max1 = n.score
        max_name = self.head.name
        while n:
            if max1 < n.score:
                max1 = n.score
                max_name = n.name

            n = n.next

        print("Najwiêksz± liczbê punktów zdoby³ mistrzunio " + max_name +". Gratulujemy!")


_list1 = myList()
_list1.addAtBeginning("Jacek", 15)
_list1.addAtBeginning("Staszek", 20)
_list1.addAtBeginning("Andrzej", 18)
_list1.addAtBeginning("Ola", 17)
_list1.addAtBeginning("Basia", 8)
_list1.addAtBeginning("Krzysiu", 13)
_list1.addAtBeginning("Olek", 12)
_list1.addAtEnd("Monika", 11)
_list1.addAtEnd("£ukasz", 9)
print("Czytamy listê od pocz±tku:")
_list1.printFromBeginning()
print("\nCzytamy listê od koñca:")
_list1.printFromEnd()
print("\nTestujemy dodawanie na N-te miejsce.\n")
_list1.addAtN("Zosia", 2)
_list1.printFromBeginning()
_list1.findHighestScore()
