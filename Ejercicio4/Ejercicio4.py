import math

# input

peso=int(input("Digite su peso: "))
altura=float(input("Digite su altura: "))

#processing

IMC=(peso/altura/2)

#output

if IMC<16:
    print("criterio de ingreso al hospital")

elif IMC>16 and IMC<17:
    print("usted tiene infrapeso")

elif IMC>17 and IMC<18:
    print("usted tiene bajo peso")

elif IMC>18 and IMC<25:
    print("usted tiene un peso saludable")

elif IMC>25 and IMC<30:
    print("usted tiene sobre peso(obesidad grado 1)")

elif IMC>30 and IMC<35:
    print("usted tiene sobre peso cronico(obesidad de grado 2)")

elif IMC>35 and IMC<40:
    print("usted tiene obesidad premorbida(obesidad grado 3)")

elif IMC>40:
    print("usted tiene obesidad morbida(obesida grado 4)")
    
    



