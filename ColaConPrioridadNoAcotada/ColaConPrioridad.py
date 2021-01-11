class PriorityQueue:
    def __init__( self ):
        self.__data = list() # o tambien puedes declararlo asi list []

    def is_empty( self ):
        return len(self.__data) == 0

    def length ( self ):
        return len(self.__data)

    def enqueue (self, cargo, prioridad):
        element = (cargo, prioridad)
        self.__data.append(element)
        if len(self.__data) > 0:
            for i in range (len(self.__data)-1):
                for j in range (len(self.__data)-1):
                    if self.__data[j][1] > self.__data[j+1][1]:
                        aux = self.__data[j]
                        self.__data[j] = self.__data[j+1]
                        self.__data[j+1] = aux


    def dequeue (self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return "El barco ha sido abandonado en su totalidad"

    def to_string(self):
        cadena =""
        for element in self.__data:
            cadena = cadena + "|" + str(element)
        cadena = cadena + "|"
        return cadena
