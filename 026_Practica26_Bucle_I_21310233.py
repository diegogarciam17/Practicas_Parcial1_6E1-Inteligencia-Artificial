#Diego Ivan Garcia Monteon 
#21310233 6E1 
#Inteligencia Artificial

x = 1

while x < 10:
    print(x)
    x += 1

frase = "Lo que escribas, lo repito:"
frase += "\nIntroduce el comando 'salir' para finalizar el programa.\n"

mensaje = ""

while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)

print("Se ha salido del bucle.")

#While loop
x = 1

while x <= 10:
    print(x)
    x += 1
    
#while-else
x = 1
while x <=10:
  print(x)
  x += 1
else:
  print("Saliendo del bucle while...")    