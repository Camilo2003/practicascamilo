#Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores),
#y posterior ordene los elementos de menor a mayor.

import random

lista=[]

for i in range(10):
    lista.append(random.randint(0,100))

print(lista)

tam=len(lista)

print(tam)

for i in range(tam):
    for j in range(tam-1):
        if lista[j]>lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux
        

print(lista)


