#Diego Ivan Garcia Monteon
#21310233 6E1
#Inteligencia Artificial

#Exite otro que al momento de que no se cumpla la condicional pueda ejecutar otra cosa con el condicional else
#En este ejemplo de no ser mayor de 18 años no ejecutara el programa
edad = 20
if edad > 18:
    print('Adelante usuario')
    
else:
    print('Alto ahi eres menor de 18 años')
    
#La falla que pueda presentar debido al operador ya que no contempla el numero 18 
#entonces la manera correcta sera con el operador mayor o igual que 18

edad = 20
if edad >= 18:
    print('Adelante usuario')
    
else:
    print('Alto ahi eres menor de 18 años')    
