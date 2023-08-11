#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
#(comprendidas entre 0 y 10).
#A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas=[]

for i in range(5):
    notas.append(int(input("Nota: ")))

max=0
min=notas[0]
sum=0

for i in notas:
    if max<i:
        max=i
    elif min>i:
        min=i
    sum=sum+i

print("Notas: ", notas)
print("Mayor: ",max,"menor: ",min,"promedio: ",sum/5)
