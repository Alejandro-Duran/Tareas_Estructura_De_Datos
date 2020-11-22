class NodoDoble:
    def __init__(self, value, siguiente =  None, anterior = None):
        self.data = value
        self.siguiente = siguiente
        self.anterior = anterior

class DoubleLinked_List:
    def __init__ (self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.siguiente = self.__tail
        self.__tail.anterior = self.__head
        self.__size=0

    def is_empty(self):
        return self.__head.data == None

    def append (self, value):
        nuevo = NodoDoble(value)
        if self.__head.data == None:
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            self.__size+=1
            nuevo = NodoDoble(value,None,curr_node)
            curr_node.siguiente = nuevo
            self.__tail = curr_node.siguiente

    def get_size(self):
        return self.__size

    def find_from_head (self, value):
        contador = 0
        curr_node = self.__head
        while curr_node != None and value != curr_node.data:
            curr_node = curr_node.siguiente
            contador +=1
        if value == curr_node.data:
            print(f"El valor {value} esta en la posicion {contador}")
        else:
            print("El valor no existe")

    def find_from_tail (self, value):
        contador = self.__size
        curr_node = self.__tail
        while curr_node != None and value != curr_node.data:
            curr_node = curr_node.anterior
            contador -=1
        if value == curr_node.data:
            print(f"El valor {value} esta en la posicion {contador}")
        else:
            print("El valor no existe")

    def remove_head(self, value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
            print(self.__head.data)
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
                self.__size=-1
            else:
                print("El dato no existe en a lista")

    def remove_tail(self, value):
        curr_node = self.__tail
        if self.__tail.data == value:
            self.__tail = self.__tail.anterior
            print(self.__tail.data)
        else:
            siguiente = None
            while curr_node.data != value and curr_node.anterior != None:
                siguiente = curr_node
                curr_node = curr_node.anterior
            if curr_node.data == value:
                siguiente.anterior = curr_node.anterior
                self.__size=-1
            else:
                print("El dato no existe en a lista")

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f" <--{curr_node.data}-->", end="")
            curr_node = curr_node.siguiente
        print("")

    def revrse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f" <--{curr_node.data}-->", end="")
            curr_node = curr_node.anterior
        print("")
