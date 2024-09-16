import re
import math
import random
import string

# Ejercicio 1: Validación de Contraseña Segura
# Escribe un programa que reciba una contraseña del usuario y valide si es segura o no. Una contraseña se considera segura si cumple con los siguientes criterios:
# Tiene al menos 10 caracteres.
# Contiene al menos una letra mayúscula, una minúscula, un número y un carácter especial.
# Si la contraseña no es segura, el programa debe indicar cuál o cuáles criterios no cumple.

def validate_password(password):
    unmet_criteria = []

    if len(password) < 10:
        unmet_criteria.append("Must be at least 10 characters long")
    if not re.search(r"[A-Z]", password):
        unmet_criteria.append("Must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        unmet_criteria.append("Must contain at least one lowercase letter")
    if not re.search(r"\d", password):
        unmet_criteria.append("Must contain at least one digit")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        unmet_criteria.append("Must contain at least one special character")
    if not unmet_criteria:
        return "The password is secure"
    else:
        return f"The password is not secure. Missing the following criteria: {', '.join(unmet_criteria)}"

password = input("Enter your password: ")
result = validate_password(password)
print(result)

# Ejercicio 2: Calculadora de Conversión de Monedas
# Crea un programa que reciba una cantidad en una moneda específica (por ejemplo, USD, EUR, MXN) y convierta esa cantidad a otras dos monedas diferentes. Los tipos de cambio deben estar almacenados en un diccionario. El usuario ingresará la moneda de origen, la cantidad y las monedas de destino.
# El programa debe mostrar el resultado de las conversiones y validar si las monedas ingresadas son válidas.

exchange_rates = {
    'USD': {'EUR': 0.85, 'MXN': 17.0},
    'EUR': {'USD': 1.18, 'MXN': 20.0},
    'MXN': {'USD': 0.059, 'EUR': 0.050}
}

def convert_currency(origin, amount, target1, target2):
    if origin not in exchange_rates:
        return f"Origin currency '{origin}' is not valid."
    
    if target1 not in exchange_rates[origin] or target2 not in exchange_rates[origin]:
        return f"One or both target currencies are not valid for '{origin}'."
    
    conversion1 = amount * exchange_rates[origin][target1]
    conversion2 = amount * exchange_rates[origin][target2]
    
    return (f"{amount} {origin} is {conversion1:.2f} {target1} "
            f"and {conversion2:.2f} {target2}.")

origin = input("Enter the origin currency (USD, EUR, MXN): ").upper()
amount = float(input(f"Enter the amount in {origin}: "))
target1 = input("Enter the first target currency (USD, EUR, MXN): ").upper()
target2 = input("Enter the second target currency (USD, EUR, MXN): ").upper()

result = convert_currency(origin, amount, target1, target2)
print(result)


# Ejercicio 3: Sistema de Votación con Diccionarios
# Desarrolla un sistema de votación en el cual un usuario puede votar por un candidato (utilizando su nombre) en una elección. El programa debe aceptar múltiples votos y al final mostrar el total de votos para cada candidato. Si el candidato no existe, debe preguntar al usuario si desea agregarlo.
# Utiliza un diccionario para almacenar los nombres de los candidatos y sus votos.

def votar(candidatos, nombre):
    if nombre in candidatos:
        candidatos[nombre] += 1
    else:
        agregar = input(f"El candidato '{nombre}' no existe. ¿Deseas agregarlo? (s/n): ").lower()
        if agregar == 's':
            candidatos[nombre] = 1
        else:
            print(f"No se agregó el candidato '{nombre}'.")
    return candidatos

def mostrar_resultados(candidatos):
    print("\nResultados de la votación:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} votos")

candidatos = {}

while True:
    nombre = input("\nIngresa el nombre del candidato por el que deseas votar (o 'fin' para terminar): ").capitalize()

    if nombre.lower() == 'fin':
        break

    candidatos = votar(candidatos, nombre)

mostrar_resultados(candidatos)


# Ejercicio 4: Ordenar Lista de Palabras por Longitud
# Escribe un programa que reciba una lista de palabras introducida por el usuario (una sola línea separada por espacios). El programa debe ordenar la lista de palabras según su longitud y en caso de palabras con la misma longitud, debe ordenarlas alfabéticamente.

def ordenar_palabras(palabras):
    palabras_ordenadas = sorted(palabras, key=lambda x: (len(x), x))
    return palabras_ordenadas

entrada = input("Ingresa una lista de palabras separadas por espacios: ")
palabras = entrada.split()

resultado = ordenar_palabras(palabras)
print("Palabras ordenadas:", " ".join(resultado))


# Ejercicio 5: Sistema de Inventario con Diccionarios y Listas
# Imagina que eres responsable del inventario de una tienda. Crea un programa que gestione un inventario de productos utilizando un diccionario donde:
# La clave es el nombre del producto.
# El valor es una tupla con el precio y la cantidad disponible.
# El programa debe permitir al usuario:
# Consultar la cantidad y el precio de un producto específico.
# Agregar un nuevo producto o modificar uno existente.
# Mostrar todos los productos en stock.


def consultar_producto(inventario, producto):
    if producto in inventario:
        precio, cantidad = inventario[producto]
        print(f"{producto}: Precio - {precio}, Cantidad - {cantidad}")
    else:
        print(f"El producto '{producto}' no está en el inventario.")

def agregar_o_modificar_producto(inventario, producto, precio, cantidad):
    inventario[producto] = (precio, cantidad)
    print(f"Producto '{producto}' agregado/modificado con éxito.")

def mostrar_inventario(inventario):
    if inventario:
        print("\nInventario:")
        for producto, (precio, cantidad) in inventario.items():
            print(f"{producto}: Precio - {precio}, Cantidad - {cantidad}")
    else:
        print("El inventario está vacío.")

inventario = {}

while True:
    print("\nOpciones:")
    print("1. Consultar un producto")
    print("2. Agregar o modificar un producto")
    print("3. Mostrar todos los productos en stock")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ").capitalize()
        consultar_producto(inventario, producto)
    
    elif opcion == "2":
        producto = input("Ingresa el nombre del producto: ").capitalize()
        precio = float(input(f"Ingresa el precio de '{producto}': "))
        cantidad = int(input(f"Ingresa la cantidad disponible de '{producto}': "))
        agregar_o_modificar_producto(inventario, producto, precio, cantidad)
    
    elif opcion == "3":
        mostrar_inventario(inventario)
    
    elif opcion == "4":
        print("Saliendo del sistema de inventario.")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")


# Ejercicio 6: Análisis de Frecuencia de Palabras
# Escribe un programa que analice la frecuencia de cada palabra en un texto ingresado por el usuario. El programa debe ignorar mayúsculas y minúsculas, y contar las palabras repetidas. Muestra el resultado en un formato de diccionario, donde las claves son las palabras y los valores son las frecuencias.

def analizar_frecuencia(texto):
    palabras = texto.lower().split()
    frecuencia = {}

    for palabra in palabras:
        palabra_limpia = ''.join(caracter for caracter in palabra if caracter.isalnum())
        if palabra_limpia in frecuencia:
            frecuencia[palabra_limpia] += 1
        else:
            frecuencia[palabra_limpia] = 1
    return frecuencia

texto_usuario = input("Introduce un texto: ")

resultado = analizar_frecuencia(texto_usuario)
print(resultado)


# Ejercicio 7: Tuplas de Coordenadas y Distancia Mínima
# Crea un programa que reciba un conjunto de puntos en un plano 2D representados como tuplas (x, y). El programa debe calcular la distancia entre todos los puntos y devolver cuáles dos puntos están más cercanos entre sí. Usa la fórmula de distancia Euclidiana.

def distancia_euclidiana(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def puntos_mas_cercanos(puntos):
    min_distancia = float('inf')
    punto1 = punto2 = None

    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            dist = distancia_euclidiana(puntos[i], puntos[j])
            if dist < min_distancia:
                min_distancia = dist
                punto1, punto2 = puntos[i], puntos[j]

    return punto1, punto2, min_distancia

puntos = [(1, 2), (4, 6), (5, 8), (2, 1), (7, 5)]

p1, p2, distancia = puntos_mas_cercanos(puntos)
print(f"Los puntos más cercanos son {p1} y {p2} con una distancia de {distancia:.2f}")

# Ejercicio 8: Generador de Contraseñas Complejas
# Escribe un programa que genere una contraseña compleja de longitud variable según lo indicado por el usuario. La contraseña debe incluir:
# Letras mayúsculas y minúsculas.
# Números.
# Caracteres especiales.

def generar_contraseña(longitud):
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiales = string.punctuation

    todos_caracteres = letras_mayusculas + letras_minusculas + numeros + caracteres_especiales

    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiales)
    ]
    contraseña += random.choices(todos_caracteres, k=longitud - 4)

    random.shuffle(contraseña)

    return ''.join(contraseña)

longitud = int(input("Introduce la longitud deseada para la contraseña: "))

contraseña_generada = generar_contraseña(longitud)
print(f"Tu contraseña generada es: {contraseña_generada}")