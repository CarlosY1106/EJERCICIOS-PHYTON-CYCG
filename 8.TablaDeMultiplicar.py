import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que solicita un numero al usuario y muestra la tabla de multiplicar de dicho numero

Num = int (input("Por favor ingrese un numero: "))
print("La tabla de multiplicar del numero", Num, "es:")

for i in range (1,11):
    print(Num, "*", i, "=", Num * i)