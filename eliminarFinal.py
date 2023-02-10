class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.cabeza = None

    def append(self, data):
        if not self.cabeza:
            self.cabeza = Nodo(data)
            self.cabeza.siguiente = self.cabeza
            self.cabeza.prev = self.cabeza
        else:
            nuevo_nodo = Nodo(data)
            cur = self.cabeza
            while cur.siguiente != self.cabeza:
                cur = cur.siguiente
            cur.siguiente = nuevo_nodo
            nuevo_nodo.prev = cur
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.prev = nuevo_nodo

    def remove_last(self):
        if not self.cabeza:
            return None
        elif self.cabeza.siguiente == self.cabeza:
            cur = self.cabeza
            self.cabeza = None
            return cur.dato
        else:
            cur = self.cabeza.prev
            prev_node = cur.prev
            prev_node.siguiente = self.cabeza
            self.cabeza.prev = prev_node
            return cur.dato

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
print("Lista circular original")
cur = cllist.cabeza 
while cur:
    print(cur.dato)
    cur = cur.siguiente
    if cur == cllist.cabeza:
        break

cllist.remove_last()
print("Removiendo el ultimo elemento")
cur = cllist.cabeza
while cur:
    print(cur.dato)
    cur = cur.siguiente
    if cur == cllist.cabeza:
        break