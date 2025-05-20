import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que solicita la base y la altura de un rectangulo para calcular su area

Base = int (input("Por favor ingrese la base del rectangulo: "))
Altura = int (input ("Por favor ingreses la altura del rectangulo: "))

Area = (Base * Altura)
print ("El area del rectangulo es igual a: ", Area)