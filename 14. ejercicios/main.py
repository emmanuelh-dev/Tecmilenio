#Elabora una lista de 7 numeros y modifica 2 de ellos

numeros = [1,2,3,4,5,6,7]

numeros[3] = 3
numeros[6] = 6

print(numeros)

# Elabora una lista de frutas y que el usuario pueda cambiar una de las frutas

frutas = ['mango', 'fresa', 'coco']

print(frutas)
position = int(input("Ingresa la position de la fruta que quieres cambiar"))
fruta_nueva = input("Ingresa la fruta nueva")

frutas[position-1] = fruta_nueva

print(', '.join(frutas))

# elementos varios

lista = ["", "juan", 1, None, True]

for i in lista: 
  print(i)
