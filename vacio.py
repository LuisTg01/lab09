class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.cabeza = None

    def is_empty(self):
        return self.cabeza is None

cllist = CircularLinkedList()
print("¿la lista circular esta vacia?: ", cllist.is_empty())
