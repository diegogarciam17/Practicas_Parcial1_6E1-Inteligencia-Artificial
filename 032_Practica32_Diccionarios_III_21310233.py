#Diego Ivan Garcia Monteon 
#21310233 6E1 
#INteligencia Artificial

catalogo1 = {

    'Categoria': 'Teclado',
    'Modelo': 'Hyper x Alloy FPS Pro'
    'Precio': '89.99'
    }

catalogo2 = {
    'Categoria': 'Teclado',
    'Modelo': 'Corsair K55 RGB'
    'Precio': '59.99'
    }
#Usando el metodo len en los diccionarios
print (len(catalogo1) + len(catalogo2))

#Usando el metodo pop (para eliminiar elemento en cncreto de las listas)
catalogo.pop('Categoria')
print(catalogo1) #Para indicar lo que se borro

#Otra funcion es usando la parabra ya antes vista del
del catalogo1['Precio']
print (catalogo1)

#tambien se puede borrar todo un diccionario
del catalogo1 #Maraca error al compilar ya que esta borrando la variable
print (catalogo1)

#otra manera de eliminar el diccionario es usando clear
catalogo1.clear()
print(catalogo1)

#para modificiar el precio de catalogo1
catalogo1['Precio']='85'
print(catalogo)

#Para agregar elementos al diccionario
catalogo1['Color']='Negro'
print (catalogo1)

#crear con el metodo copy
catalogoCopia =catalogo1.copy()
print(catalogoCopia)

#crear con el metodo dict
catalogoCopia =c dict(catalogo1)
print(catalogoCopia)


