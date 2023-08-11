#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene
# (por ejemplo, 30) y 
#el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

meses=["Enero ","Febrero","Marzo","Abril","Mayo","Junio","julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias=[31,28,31,30,31,30,31,31,30,31,30,31]

n=int(input("Numero: "))
pos=n-1

print("El mes " + meses[pos]," tiene ",dias[pos]," dias")

