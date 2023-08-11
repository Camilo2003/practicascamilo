# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso,
# y muestra sus elementos por la pantalla

lista1=[]
lista2=[]

for i in range(5):
    lista1.append(input("Texto: "))

print(lista1)

tam=len(lista1)

while tam>0:
    tam=tam-1
    lista2.append(lista1[tam])

print(lista2)
