class Nodo:
    def __init__(self, value, siguiente = None):
        self.data = value
        self.next = siguiente

class ListaCircular:
    def __init__(self):
        self.__ref = Nodo(None,None)

    def is_empty(self):
        return self.__ref.data == None

    def insert(self, value):
        if self.__ref.data == None:
            nuevo = Nodo(value, value)
            self.__ref = nuevo
            self.__ref.next = self.__ref
        elif self.__ref.data == self.__ref.next:
            if self.__ref.data < value:
                nuevo = Nodo(value, self.__ref)
                self.__ref.next = nuevo
                self.__ref = self.__ref.next
            elif self.__ref.data > value:
                nuevo = Nodo(value, self.__ref)
                self.__ref.next = nuevo
        elif self.__ref.data != self.__ref.next:
            if self.__ref.data < value:
                nuevo = Nodo (value, self.__ref.next)
                self.__ref.next = nuevo
                self.__ref = self.__ref.next
            elif self.__ref.next.data > value:
                nuevo = Nodo (value, self.__ref.next)
                self.__ref.next = nuevo
            elif self.__ref.data > value and self.__ref.next.data < value:
                curr_node = self.__ref.next
                prev=None
                while value > curr_node.data and curr_node.data != value:
                    prev = curr_node
                    curr_node = curr_node.next
                if curr_node.data == value:
                    print("Ese dato ya fue ingresado")
                else:
                    nuevo = Nodo(value, curr_node)
                    prev.next = nuevo
            elif value == self.__ref.data or value == self.__ref.next.data:
                print("Ese dato ya fue ingresado")

    def search (self, value):
        contador = 0
        curr_node = self.__ref.next
        while curr_node != self.__ref and curr_node.data != value:
            curr_node = curr_node.next
            contador+=1
        if curr_node.data == value:
            print(f"Tu valor esta en la posición {contador}")
        else:
            print("El dato ingresado no existe en la lista")

    def remove(self, value):
        prev=None
        if self.__ref.data == None:
            print("La lista esta vacia, no se puede eliminar nada")
        else:
            curr_node = self.__ref.next
            while self.__ref != curr_node and curr_node.data != value:
                prev = curr_node
                curr_node = curr_node.next
            if curr_node == self.__ref and curr_node.data == value:
                if prev==None:
                    self.__ref.data=None
                else:
                    self.__ref = prev
                    prev.next = curr_node.next
            elif curr_node == self.__ref.next:
                self.__ref.next=self.__ref.next.next
            elif curr_node != self.__ref and curr_node != self.__ref.next:
                prev.next = curr_node.next
            else:
                print("El dato no esta en la lista")

    def transversal(self):
        if self.__ref.data == None:
            print("La lista esta vacia")
        else:
            curr_node = self.__ref.next
            while curr_node != self.__ref and curr_node != None:
                print(f" {curr_node.data} -->", end="")
                curr_node = curr_node.next
            if curr_node.data != None:
                print(f" {curr_node.data} -->", end="")
                print ("")
