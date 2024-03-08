#Diego Ivan Garcia Monteon
#21310233 6E1
#Inteligencia Artificial

class Usuarios():
    
    def __init__(self, nombre, pin):
        self.nombre=nombre
        self.pin=pin
        
    def saludo(self):
        print('Hola '+ self.nombre + 'Bienvenido a su sesion')
        
    def despedida(self):
        print (self.pin + ', Hasta la proximausuario')
        
usuario1=Usuarios('Diego ', '1234')

usuario2=Usuarios('Karo', '4321')

usuario1.saludo()
        

