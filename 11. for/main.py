#1.- Crea un programa donde solicites al usuario una palabra o una frase y pueda contar la cantidad de vocales ya sean mayúsculas o minúsculas que se tiene en lo ingresado

def programa():
  palabra = input("IIngresa una palabra o frase:")
  
  letras = 0
  for i in palabra: 
    print(i)
    letras +=1
  print(letras)
  
# programa()

# 2.- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

def piramide():
  rows = int(input("Ingresa un numero entero: "))
  for i in range(rows):
    for j in range(i+1):
     print(' *', end=" ")
    print()
# piramide()

# 3.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def edad():
  age = int(input("Ingresa tu edad: "))
  for i in range(age):
    print(f"Has cumplido {i+1} años")
# edad()

# 5.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repetir():
  palabra = input("Ingresa una palabra: ")
  for i in range(10):
    print(palabra)
# repetir()

# 6.- realiza un código que  itere sobre una secuencia de números del 1 al 10, clasificándolos según si son pares, divisibles por 3 o ninguno de los dos.

def pares():
  for i in range(10):
    if i % 2 == 0:
      print(f"{i} es par")
    elif i % 3 == 0:
      print(f"{i} es divisible por 3")
    else: 
      print(f"{i} no es ni par ni divisible por 3")
pares()