class Node:
    def __init__(self,nazwa,priorytet):
        self.nazwa = nazwa
        self.priorytet = priorytet
        self.next = None

class OneDirectionalList:
    def __init__(self):
        self.head = None

    def add(self, nazwa, priorytet):
        new_node = Node(nazwa,priorytet)
        if not self.head:
            self.head = new_node

        else:
            n = self.head

            if not n.next:
                n.next = new_node

            else:
                while n.next:
                    tmp = n.next
                    if new_node.priorytet >= tmp.priorytet:
                        break
                    n = n.next
                n.next = new_node
                new_node.next = tmp





    def printList(self):
        n = self.head
        while n:
            print(n.priorytet,n.nazwa)
            n = n.next

ll = OneDirectionalList()
ll.add('yyc5',5)
ll.add('yyc',1)
ll.add('yyc2',2)
ll.add('yyc5',5)
ll.add('yyc3',3)
ll.add('yyc2-2',2)
ll.add('yyc4',4)
ll.printList()