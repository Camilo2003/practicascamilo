#Escribir un programa que pregunte por una muestra de números, separados por comas, 
#los guarde en una lista y muestre por pantalla su media y desviación típica.

def suma(lista):
    sum=0
    for i in lista:
        sum=sum+i
    return sum

def media(lista):
    return suma(lista)/(len(lista))

#desviacion estandar suma cuadrados
def sumacuadrados(lista):
    suma=0
    for i in lista:
        suma=pow((i-media(lista)),2)+suma
    return suma

def varianza(lista):
    return sumacuadrados(lista)/(len(lista)-1)

def desvest(lista):
    return varianza(lista)**0.5


muestra=input("Muestra: ")
lista=muestra.split(",") #Divide cadena segun un delimitador
lista2=[]



for i in lista:
    lista2.append(float(i))



print(lista)
print(lista2)


print("La media es: ",media(lista2))
print("La desviacion estandar es: ",desvest(lista2))