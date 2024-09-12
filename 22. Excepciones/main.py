# Name error

# n = 3
# print(n)

# key error

dict = {
  "name": "Juan",
  # "age": 18,
}

try:
    print(dict['age'])
except KeyError:
    print("La clave 'age' no existe en el diccionario.")
