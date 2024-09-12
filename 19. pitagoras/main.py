# Realizarás un programa en Python para mostrar la tabla de Pitágoras, la cual permite visualizar cuál será el resultado del producto de dos números,
# así que solicitarás dos factores (cifras) para obtener el resultado de su multiplicación.
def pitagoras():
  num1 = int(input("Ingresa el primer numero "))
  num2 = int(input("Ingresa el segundo numero "))

  print("Tabla de pitagoras")
  for i in range(num1):
    for j in range(num2):
      print(f"{i * j:4}", end=" ")
    print()
  
pitagoras()