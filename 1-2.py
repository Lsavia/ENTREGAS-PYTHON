
# Escribe un programa que solicite al usuario una cantidad de segundos y muestre
#cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
#hora, 1 minuto y 1 segundo.
print (" hola, mandame los segundos")
segundos = int (input())

minutos = segundos // 60
segundos =0
if( minutos > 60) :
    horas = minutos // 60
    minutos =0
    
print ( segundos , minutos, horas)
