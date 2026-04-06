
#Escribe un programa que simule una caja registradora: el usuario ingresa precios de
#productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
#acumulado. Nota: utilizá la sentencia break cuando haga falta.
print("ingrese el precio del producto")
total =0
while True :
    print("ingrese el precio del producto (ingrese 0 para terminar)")
    num = int(input())
    if num == 0:
        break
    
    total= total +num
print (total)
