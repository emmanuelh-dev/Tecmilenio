#1.-Escribe un programa que tome dos matrices de igual tamaño (matrices bidimensionales) y devuelva una nueva matriz que sea la suma de las dos matrices originales.

# parto de que son iguales y no necesitan validacion

matrix1=[
  [1, 2, 3,],
  [4, 5, 6,],
  [7, 8, 9,],
]

matrix2 = [
  [8, 1, 6,],
  [3, 5, 7,],
  [4, 9, 2,]
]

matrix3 =[[0 for _ in range(len(matrix1))] for _ in range(len(matrix1))]

for i in range(len(matrix1)):
  print(i)
  for j in range(len(matrix1[i])):
    matrix3[i][j]= matrix1[i][j] + matrix2[i][j]

for mat in matrix3:
  print(mat)

#2. Crea un programa que multiplique dos matrices de tamaño adecuado. Recuerda que para multiplicar matrices, el número de columnas de la primera debe coincidir con el número de filas de la segunda
matrix4 =[[0 for _ in range(len(matrix1))] for _ in range(len(matrix1))]

for i in range(len(matrix1)):
  print(i)
  for j in range(len(matrix1[i])):
    matrix4[i][j]= matrix1[i][j] * matrix2[i][j]

for mat in matrix4:
  print(mat)


#3.- Escribe un programa que tome una matriz y devuelva su transpuesta (intercambiar filas por columnas)
#3.- Escribe un programa que tome una matriz y devuelva su transpuesta (intercambiar filas por columnas)

def traspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    matriz_traspuesta = [[0 for _ in range(filas)] for _ in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_traspuesta[j][i] = matriz[i][j]

    return matriz_traspuesta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matriz:
  print(row)

matriz_resultado = traspuesta(matriz)

for row in matriz_resultado:
  print(row)

#4.- Un cuadrado mágico es una matriz en la que la suma de cada fila, columna y diagonal es la misma. Escribe un programa que determine si una matriz dada es un cuadrado mágico.

def cuadro_magico(matrix):
  row = 0
  col = 0
  slash= 0
  for rows in matrix:
    for cols in matrix:
      for column in cols:
        col +=column
      
      
      
    print(f"col = {col}")
    return True

print(cuadro_magico(matrix1))
print(cuadro_magico(matrix2))