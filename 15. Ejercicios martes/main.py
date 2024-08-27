# 1.- Dada una lista de palabras, cuenta cuántas veces aparece la palabra "Python" en la lista.
palabras1 = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]
aparece = 0
for palabra in palabras1:
  print(palabra)
  if (palabra == "Python"):
    aparece+=1
print(f"Aparece {aparece} veces")

# 2.- Dada una lista de cadenas de texto, convierte todas las cadenas a mayúsculas sin usar métodos como upper().

frases = ["hola", "mundo", "python", "es", "genial"]
print(f"{frases}")
def convertir_a_mayusculas(frase):
    resultado = ""
    for caracter in frase:
        if 'a' <= caracter <= 'z':
            resultado += chr(ord(caracter) - 32)
        else:
            resultado += caracter
    return resultado

frases_mayusculas = [convertir_a_mayusculas(frase) for frase in frases]

print(frases_mayusculas)


# 3.- Dada una lista de palabras, elimina todas aquellas palabras que tengan menos de 4 caracteres.
palabras2 = ["sol", "luna", "cielo", "mar", "estrella", "pez"]
nueva_lista = []
for palabra in palabras2:
  if len(palabra) >=4:
    nueva_lista.append(palabra)
print(f"La lista se veria{nueva_lista}")
# 4.- Dada una lista de números, encuentra el número máximo sin usar la función max().
numeros = [15, 22, 8, 34, 9, 6, 17]
numero_mayor = 0
for numero in numeros:
  if(numero > numero_mayor):
    numero_mayor = numero
print(f"Numero mayor {numero_mayor}")
# 5.- Dada una lista de números enteros, cuenta cuántos números son positivos.
numeros2 = [-3, 5, -7, 2, -8, 10, -4, 6]
positivos = 0
for numero in numeros2:
  if(numero > 0):
    positivos += 1
print(f"Positios {positivos}")
# 6.-Dada una lista, invierte el orden de los elementos sin usar métodos como reverse().
numeros3 = [1, 2, 3, 4, 5]
nuevo=[]
for numero in numeros3:
  nuevo.append(numeros3[len(numeros3)-1])
print(numeros3)
print(nuevo)
# 7.- Dada una lista de números, encuentra y muestra la media (promedio) de los elementos de la lista.
numeros4 = [4, 7, 2, 9, 3, 8, 5]
total = len(numeros4)
suma = 0
for numero in numeros4:
  suma += numero
  
print(f"El promedio es {(suma/total)}")