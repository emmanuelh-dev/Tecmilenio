# Listas

materias = ['Espanol', 'Matematicas', 'Fisica', 'Quimica', 'Biologia']

print(materias)

print(materias[0])
print(materias[1])
print(materias[2])
print(materias[3])
print(materias[4])

print(materias[-1])
print(materias[-2])
print(materias[-3])
print(materias[-4])
print(materias[-5])

# Imprimir solo una parte
print(materias[2:])

# modificar la lista
materias[3] = 'Fisica 2'

print(materias)


# Iterar sobre materias

for materia in materias:
    print(materia)

# Agregar un elemento

materias.append('Hola')
print(materias)
