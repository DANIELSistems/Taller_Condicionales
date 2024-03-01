#input

precio_costo=int(input("digite el costo del articulo: "))

#processing

if precio_costo<=3000:
        ganancia= precio_costo*0.15

elif precio_costo<=6000:
        ganancia=500

else:
        ganancia= precio_costo*0.25


precio_venta = precio_costo+ganancia

#output

print( " El producto tiene un costo de $" + str(precio_costo) + " con una ganancia de $" + str(ganancia) + " queda con un precio de venta de $" + str(precio_venta))





