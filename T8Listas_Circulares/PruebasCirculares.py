from Listas_Circulares import ListaCircular

lc = ListaCircular()
print(f"La lista esta vacia? {lc.is_empty()}")
lc.insert(1)
lc.insert(2)
lc.insert(0)
lc.insert(6)
lc.insert(3)
lc.insert(5)
lc.insert(4)
lc.insert(7)
lc.insert(-1)
lc.insert(7)
print(f"La lista esta vacia? {lc.is_empty()}")
lc.transversal()
lc.search(20)
lc.remove(-1)
lc.transversal()
lc.remove(7)
lc.transversal()
lc.remove(3)
lc.transversal()
lc.insert(20)
lc.insert(15)
lc.insert(-3)
lc.insert(45)
lc.insert(33)
lc.transversal()
lc.remove(33)
lc.remove(0)
lc.remove(5)
lc.remove(2)
lc.transversal()
lc.remove(-3)
lc.remove(1)
lc.remove(4)
lc.remove(6)
lc.remove(15)
lc.remove(20)
lc.remove(45)
lc.transversal()