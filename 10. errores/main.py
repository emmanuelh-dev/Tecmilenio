# Objetivo: Imprimir los números del 1 al 5


x = 1
while x <= 5: #Error de sintáxis
    print(x)
    x += 1

# Objetivo: Calcular la media de una lista de números


numeros = [10, 20, 30, 40, 50]
total = sum(numeros)
cantidad = len(numeros) #Error al poner "-5" en la línea 6
media = total / cantidad
print(f"La media es: {media}")


# Objetivo: Encontrar el mayor de dos números
a = 15
b = 10

if a > b:  # Error lógico: la condición debería ser a > b
    mayor = a
else:
    mayor = b

print(f"El mayor es: {mayor}")

# Objetivo: Calcular el descuento de un precio
precio = 200
descuento = 0.10  # Descuento del 10%

precio_con_descuento = precio - descuento * precio  
print(f"El precio con descuento es: {precio_con_descuento}")

#Colocación errónea del descuento

# Objetivo: Imprimir un mensaje de bienvenida
nombre = "Carlos"
print("Bienvenido", nombre)  

#Error al escribir el print, además faltó adicionar la variable "nombre"

# Objetivo: Concatenar un nombre y un número de identificación
nombre = "Ana"
identificacion = 12345

mensaje = "Hola, " + nombre + ". Tu ID es: ", + identificacion
print(mensaje)

#Faltó la fórmula para concatenar el nombre

# Objetivo: Comprobar si un número es par o impar
numero = 7

if numero % 2 == 0:  # Error de lógica: uso incorrecto de '=' en lugar de '=='
    print("El número es par")
else:
    print("El número es impar")


# Objetivo: Verificar si un número es positivo, negativo o cero
numero = -10

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")  
else:
    print("El número es cero")

#Error en la estructura del código