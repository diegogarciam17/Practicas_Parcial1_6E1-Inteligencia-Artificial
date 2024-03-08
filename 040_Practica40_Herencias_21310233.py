#Diego Ivan Garcia Monteon
#21310233 6E1
#Inteligencia Artificial

#Las herencias es para agregar acracteristicas de clases
# Esta es la superclase
class Usuarios:
	def __init__(self, nombre, apellidos)
		self.nombre = nombre
	self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:'+ self.nombre, '\nApellidos:', self.apellidos)
		
usuario1= Usuarios('Diego', 18)

usuario1.muestra_datos()

# Esta es la subclase
class UsuariosPremium(Usuarios):
	pass
