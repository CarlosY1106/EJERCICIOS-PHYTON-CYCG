import os
os.system('cls' if os.name == 'nt' else 'clear')

# Programa que solicita un numero al usuario y determina si es positivo, negativo o cero
Num = int(input("Por favor ingrese un numero: "))

if Num>0:
    print("El numero que ingreso es positivo")
else:
    if Num<0:
        print("El numero que ingreso es negativo")
    else:
        print("El numero que ingreso es cero")