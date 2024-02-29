import math

# input

X = int(input("digite una coordenada x: "))
Y = int(input("digite una coordenada y: "))

#processing

if X==0:
    if Y==0:
        print("la coordenada" ,(X,Y),"esta en el origen")
    else:
        print("la coordenada" ,(X,Y),"esta en el eje Y")
elif Y==0:
    print("la coordenada" ,(X,Y),"esta en el eje X")
elif X>0:
    if Y>0:
        print("la coorenada" ,(X,Y),"esta en el cuadrante 1")
    else:
        print("la coordenada" ,(X,Y),"esta en el cuadrante 4")
elif Y<0:
    print("la coordenada" ,(X,Y),"esta en el cuadrante 3")
else:
    print("la coordenada" ,(X,Y),"esta en el cuadrante 2")
    
    