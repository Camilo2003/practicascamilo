#Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, 
#pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

lista1=[]
lista2=[]
lista3=[]

for i in range(5):
    lista1.append(int(input("Numero lista1")))

for i in range(5):
    lista2.append(int(input("Numero lista2")))

for i in range(5):
    lista3.append(lista1[i]+lista2[i])

#print(lista1)
#print(lista2)
print(lista3)