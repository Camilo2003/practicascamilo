#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random


lista=[]

for i in range(1,10):
    lista.append(random.randint(1,10))


print(lista)

for i in lista:
    print(i,end="\t")
    print(i**2,end="\t")
    print(i**3)

print("Nuevo cambio")