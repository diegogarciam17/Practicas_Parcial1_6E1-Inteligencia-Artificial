#Diego Ivan GArcia Monteon }
#21310233 6E1 
#Inteligencia Artificial

#creamos una funcion de 4 parametros
def colores (color1,color2,color3,color4):
    print('El color 1 es '+ color1 + '.')
    
colores(color1='Rojo', color2='Azul',color3='Amarillo',color4='Violeta')
#Si se quiere la flexibilidad de args 
def colores (**kwargs):
    print('El color 1 es '+ kwargs[color1] + '.')
    
colores(color1='Rojo', color2='Azul',color3='Amarillo',color4='Violeta')
