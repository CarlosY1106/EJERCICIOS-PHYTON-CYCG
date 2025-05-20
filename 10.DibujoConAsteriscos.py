import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que solicita un numero positivo y dibuja una linea de asteriscos con dicho numero

Num = int (input ("Por favor ingrese un numero entero positivo: "))

print("La linea de asteriscos del tamaño", Num, "es:")
for i in range (Num):
    print("*", end="") 
print()
