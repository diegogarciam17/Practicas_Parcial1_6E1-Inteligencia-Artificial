#Diego Ivan Garcia Monteon
#21310233 6E1
#Inteligencia Artificial

class Usuarios:
    def __init__(usuario, nombre, edad):
    self.nombre=nombre
    self,edad=edad
    
    def muestra_datos(self):
        print('Usuario: '+ self.nombre, self.edad)
        
usuario1= usuarios('Diego', 18)
usuario1.muestra_datos()

usuario1.edad= 23
usuario1.muestra_datos()