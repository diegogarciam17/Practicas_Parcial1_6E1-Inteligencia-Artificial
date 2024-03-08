#Diego Ivan Garcia Monteon
#21310233 6E1
#Inteligencia Artificial
#Este funcionara pidiendo algun requerimiento pudiendolo almacenar en una variable
#Se pueden agregar tantos elif como necesites

edad = int(input('Cuantos años tienes?    '))
if edad <=0:
    print('Edad Erronea')

elif edad >=1 and edad <=17:
    print('Eres menor de edad.')

elif edad <=100:
    print('Eres mayor de edad.')
    
else:
    print('Edad erronea')