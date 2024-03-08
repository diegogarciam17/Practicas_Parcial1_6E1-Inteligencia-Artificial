#Diego Ivan Garcia Monteon
#21310233 6E1
#Inteligencia Artficial

class Usuarios:
	def __init__(self, nombre, apellidos)
		self.nombre = nombre
	self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios):
	def __init__(self, nombre, apellidos, instagram)
		self.nombre = nombre
	self.apellidos = apellidos
	self.instagram = instagram

	def muestra_datos_premium(self):
		print('El nombre de usuario es: '+ self.nombre, 'y tiene', self.edad, "años. Su insta es:", self.instagram)
