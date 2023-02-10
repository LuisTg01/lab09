class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class CircularLinkedList:
    def __init__(self):
        self.cabeza = None

    def append(self, data):
        if not self.cabeza:
            self.cabeza = Node(data)
            self.cabeza.siguiente = self.cabeza
        else:
            nuevo_nodo = Node(data)
            cur = self.cabeza
            while cur.siguiente != self.cabeza:
                cur = cur.siguiente
            cur.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def display(self):
        cur = self.cabeza
        while cur:
            print(cur.dato)
            cur = cur.siguiente
            if cur == self.cabeza:
                break

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

print("lista circular")
cllist.display()
