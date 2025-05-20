import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que solicita tres numeros y determina cual es el mayor de los tres o si son iguales

Num1 = int(input("Por favor ingrese el primer numero: "))
Num2 = int(input("Por favor ingrese el segundo numero: "))
Num3 = int(input("Por favor ingrese el tercer numero: "))

if Num1 > Num2 and Num1 > Num3:
    print("El primer numero es el mayor de los tres")
else:
    if Num2 > Num1 and Num2 > Num3:
        print("El segundo numero es el mayor de los tres")
    else:
        if Num3 > Num1 and Num3 > Num2:
            print("El tercer numero es el mayor de los tres")
        else:
            print("Los tres numeros son iguales")