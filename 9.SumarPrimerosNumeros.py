import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que solicita un numero y muestra la suma de los primeros n numeros
Num = int (input("Por favor ingrese un numero: "))
print("La suma de los primeros", Num, "numeros es: ")

Sumatoria = 0
for i in range (1, Num + 1):
    Sumatoria += i
print("La suma es:", Sumatoria)