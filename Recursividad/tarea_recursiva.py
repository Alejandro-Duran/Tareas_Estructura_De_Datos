from Pila import Pila

print("Ejercicio 1: Lista Python de enteros con suma recursiva")
def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def main():
    datos =[4,2,3,5] # 14
    res = suma_lista_rec(datos)
    print(res)

main()
print("---------------------------------------------------")
print("Ejercicio 2: Conteo regresivo usando recursividad\n")

def cuenta_regresiva(n):
    if n == 0:
        return str(n) + "\n\nCuenta regresiva terminada"
    else:
        return str(n) + "\n" + cuenta_regresiva(n-1)

def main2():
    print(cuenta_regresiva(10))

main2()

print("------------------------------------------------")
print("Ejercicio 3: Sacar valor medio de una pila\n")

pops = []
p = Pila()
def mitad_pila(n, mitad):
    if n == mitad+1:
        return "'"+ str(p.pop()) + "' Es el valor medio de la pila"
    else:
        pops.append(p.pop())
        return mitad_pila(n-1, mitad)

def main3():
    print("Pila inicial")
    for num in range (1,12):
        p.push(num)
    p.to_string()
    mitad = int(p.lenght()/2)
    print (mitad_pila(p.lenght(), mitad))
    for i in range (len(pops)-1,-1,-1):
        p.push(pops[i])
    print("Pila sin valor medio")
    return p.to_string()

main3()
