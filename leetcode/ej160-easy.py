#clase para los nodos
class ListaNodos:
    def __init__(self, val):
        self.val = val
        self.next = None

#función para encontrar la intersección
def intersecciondenodos(headA, headB):
    p1 = headA
    p2 = headB

    #si alguno termina lo mandamos al inicio del otro
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1  #puede ser el nodo de intersección o None (no hay intersección)

#nos nodos compartidos
c1 = ListaNodos(8)
c2 = ListaNodos(4)
c3 = ListaNodos(5)
c1.next = c2
c2.next = c3

#lista A: 4 → 1 → 8 → 4 → 5
a1 = ListaNodos(4)
a2 = ListaNodos(1)
a1.next = a2
a2.next = c1  #conecta al nodo compartido

#lista B: 5 → 6 → 1 → 8 → 4 → 5
b1 = ListaNodos(5)
b2 = ListaNodos(6)
b3 = ListaNodos(1)
b1.next = b2
b2.next = b3
b3.next = c1  #conecta al nodo compartido

interseccion = intersecciondenodos(a1, b1)
if interseccion:
    print("Las listas se cruzan en el nodo con valor:", interseccion.val)
else:
    print("Las listas no se cruzan.")
