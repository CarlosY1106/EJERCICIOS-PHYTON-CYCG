import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que solicita un numero y determina si es par o impar

Num = int (input("Por favor ingrese un numero: "))
if Num %2 == 0:
    print("El numero que ingreso es par")
else:
    print("El numero que ingreso es impar")