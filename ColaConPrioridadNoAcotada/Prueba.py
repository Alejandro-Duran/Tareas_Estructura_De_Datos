from ColaConPrioridad import PriorityQueue

c1 = PriorityQueue()
print("\nPRUEBA METODO QUEUE")
c1.enqueue("Maestre",4)
c1.enqueue("Niños",2)
c1.enqueue("Mecanicos",4)
c1.enqueue("Hombres",3)
c1.enqueue("Vigia",4)
c1.enqueue("Capitan",5)
c1.enqueue("Timonel",4)
c1.enqueue("Mujeres",3)
c1.enqueue("3ra edad",2)
c1.enqueue("Niñas",1)
print(c1.to_string())
print("\nPRUEBA METODO DEQUEUE")
for i in range (c1.length()+1):
    print(c1.dequeue())
print("\n")    
print(c1.to_string())