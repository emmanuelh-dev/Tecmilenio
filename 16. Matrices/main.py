#Matrices en python

#Matriz de 3x3

matrix = [
  [1,2,3,],
  [4,5,6],
  [8,9,10],
]

print(matrix)

#Print just rows
for row in matrix:
  print(row)
  
# Print all

for row in matrix:
  for col in row:
    print(col)