from DoblementeLigadas import DoubleLinked_List
dl = DoubleLinked_List()
print(f"DL esta vacia ? {dl.is_empty()}")
dl.append(10)
dl.append(5)
dl.append(6)
dl.append(20)
print(f"Tamaño de la lista {dl.get_size()}")
print("\n Transversal")
dl.transversal()
print(f"DL esta vacia ? {dl.is_empty()}")
print("\n Reverse Transversal")
dl.revrse_transversal()
print("\n Buscando por cabeza")
dl.find_from_head(20)
print("\n Buscando por cola")
dl.find_from_tail(5)
print("\n Borrando por cabeza")
dl.remove_head(5)
dl.transversal()
print("\n Borrando por cola")
dl.remove_tail(6)
dl.revrse_transversal()
