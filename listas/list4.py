#Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo.
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

lista=[]
i=int(input("Numero: "))
while i>=0:
    lista.append(i)
    i=int(input("Numero: "))
    

print(lista)
