#Diego Ivan Garcia Monteon
#21310233 6E1
#Inteligencia Artificial


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

consulta = catalogo1 get('Modelo'), catalogo1['Precio'],catalogo2 ['Modelo'],catalogo2['Precio']
print (consulta)

#El resultado sera el mismo
#Para modificar un dato del diccionario sin modificar directamente

catalogo1['Precio']='85'
print(catalogo1.get('Precio'))

#Para usar el buble for en los diccionarios

for x in catalogo2:
    print (x)
    
#Pero si queremos leer los valores de cada elemento
for x,y in catalogo2.valueitems():
    print(x,y)