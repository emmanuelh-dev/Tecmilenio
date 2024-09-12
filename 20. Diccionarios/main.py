dictionary = {
  'nombre': "Emmanuel",
  'apellido': "Hernandez",
  'edad': 21,
}

print(dictionary)

print(dictionary["nombre"])
print(dictionary.get('nombre'))

dictionary['edad'] = 20
print(dictionary)