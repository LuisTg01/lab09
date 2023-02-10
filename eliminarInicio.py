class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.cabeza = None

    def append(self, data):
        if not self.cabeza:
            self.cabeza = Node(data)
            self.cabeza.siguiente = self.cabeza
            self.cabeza.prev = self.cabeza
        else:
            new_node = Node(data)
            cur = self.cabeza
            while cur.siguiente != self.cabeza:
                cur = cur.siguiente
            cur.siguiente = new_node
            new_node.prev = cur
            new_node.siguiente = self.cabeza
            self.cabeza.prev = new_node

    def remove_head(self):
        if not self.cabeza:
            return None
        elif self.cabeza.siguiente == self.cabeza:
            cur = self.cabeza
            self.cabeza = None
            return cur.dato
        else:
            cur = self.cabeza
            while cur.siguiente != self.cabeza:
                cur = cur.siguiente
            cur.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
            self.cabeza.prev = cur
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

cllist.remove_head()
print("Eliminando el primer elemento")
cur = cllist.cabeza
while cur:
    print(cur.dato)
    cur = cur.siguiente
    if cur == cllist.cabeza:
        break
