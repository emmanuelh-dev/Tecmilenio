# Escribe un programa que solicite al usuario su peso (en kg) y su altura (en metros), y luego calcule su Índice de Masa Corporal (IMC). El programa debe clasificar el IMC en una de las siguientes categorías: bajo peso, normal, sobrepeso u obesidad. Imprime la categoría correspondiente junto con el valor del IMC.

def imc():
  peso = int(input("Ingresa tu peso en kilos"))
  altura = float(input("Ingresa tu alura en metros"))
  genero = int(input("Ingresa tu genero 1 = Hombre, 2 = Mujer"))
  resolver = peso / altura ** 2
  
  if (genero == 1):
    if(resolver < 20):
      print("Infrapeso: Coma mas")
    elif(resolver > 20 and resolver < 24.9):
      print("Peso ideal: Bien ahi")
    elif(resolver > 25 and resolver < 29.9):
      print("sobrepeso: come menos")
    elif(resolver > 30):
      print("Obesidads")
  if (genero == 2):
    if(resolver < 20):
      print("Infrapeso: Coma mas")
    elif(resolver > 20 and resolver < 23.9):
      print("Peso ideal: Bien ahi")
    elif(resolver > 24 and resolver < 28.9):
      print("sobrepeso: come menos")
    elif(resolver > 29):
      print("Obesidads")

# Crea un programa que solicite al usuario tres calificaciones (de 0 a 100) y calcule el promedio. Según el promedio, el programa debe determinar y mostrar si el usuario ha aprobado, está en la zona de recuperación, o ha reprobado, usando las siguientes reglas:
# Aprobado: Promedio mayor o igual a 70.
# Recuperación: Promedio entre 50 y 69.
# Reprobado: Promedio menor a 50.

def promedio():
  cal1 = float(input("Ingresa la calificacion 1"))
  cal2   = float(input("Ingresa la calificacion 2"))
  cal3  = float(input("Ingresa la calificacion 3"))
  
  promedio = (cal1 + cal2 + cal3) / 3
  
  if(promedio < 50):
    print("Reprobado  ")
  elif(promedio > 50 and promedio < 69):
    print("Recuperacion")
  elif (promedio > 70):
    print("Aprobado")

## Escribe un programa que pida al usuario un número de 5 dígitos y verifique si es un número capicúa (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda). El programa debe considerar que el número puede tener ceros al inicio.

def capicua():
  numero = input("INgresa un numero: ")
  separado= list(numero)
  invertido = separado[::-1]

  if(''.join(separado) == ''.join(invertido)):
    print("Es capicua")
  else:
    print("No es capicua")
#Escribe un programa que solicite al usuario tres números enteros y determine si forman 
# un triángulo válido. Un triángulo es válido si la suma de dos de sus lados siempre es mayor 
# que el tercer lado. Si el triángulo es válido, determina si es equilátero, isósceles o escaleno.

    
def es_triangulo():
  lado_uno= int(input("Ingresa el primer número entero: "))
  lado_dos= int(input("Ingresa el segundo número entero: "))
  lado_tres= int(input("Ingresa el tercer número entero: "))

  if(lado_uno + lado_dos > lado_tres) and (lado_tres + lado_uno > lado_dos) and (lado_dos + lado_tres > lado_uno):
      
      if (lado_uno == lado_dos == lado_tres):
          print("Es un triangulo equilátero")
      elif (lado_uno == lado_dos or lado_uno == lado_tres or lado_dos == lado_tres):
          print("Es un triángulo isóceles")
          
      else:
          print("Es un triángulo escaleno")

  else:
      print("Las medidas no coinciden con las de un triángulo verdadero.")

# Crea un programa que solicite al usuario un número entero positivo. Luego, verifica si el número es un número primo o no. Un número es primo si solo es divisible por 1 y por sí mismo.
def resolver(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_primo():
  numero = int(input("Ingresa un número: "))
  if resolver(numero):
      print(numero,"es un número primo")
  else:
      print(numero, "no es un número primo") 

# Crea un programa que simule un cajero automático. Solicita al usuario un PIN de 4 dígitos y verifica si es correcto (puedes usar "1234" como PIN correcto). Si el PIN es incorrecto, el usuario tiene tres intentos para ingresar el PIN correcto. Si el PIN es correcto, solicita al usuario que elija entre las siguientes opciones:
# Ver saldo.
# Retirar dinero.
# Depositar dinero. Muestra el saldo después de cada operación. Si el usuario falla los tres intentos, el programa debe bloquear el acceso.

def cajero():
  nip = 0000
  correct = 0
  while(correct < 4):
    pin = int(input("Ingresa tu pin"))
    if(pin == nip):
      correct = 0
      print(f" Ver saldo \n Retirar dinero \n Depositar dinero")
    correct += 1
  print("Exediste los intentos")
  #Escribe un programa que solicite al usuario un mes (como número entre 1 y 12) y un día 
# (como número entre 1 y 31), y luego determine a qué estación del año pertenece esa fecha. 
# Considera las siguientes estaciones en el hemisferio norte:
#	Primavera: 21 de marzo al 20 de junio.
#	Verano: 21 de junio al 22 de septiembre.
#	Otoño: 23 de septiembre al 20 de diciembre.
#	Invierno: 21 de diciembre al 20 de marzo.


def determinar_estacion(mes, dia):

    primavera_inicio = (3, 21)
    primavera_fin = (6, 20)
    verano_inicio = (6, 21)
    verano_fin = (9, 22)
    otono_inicio = (9, 23)
    otono_fin = (12, 20)
    invierno_inicio = (12, 21)
    invierno_fin = (3, 20)
    
    
    fecha = (mes, dia)
    
    
    if (primavera_inicio <= fecha <= primavera_fin) or \
       (primavera_inicio <= fecha <= (12, 31)) or \
       ((1, 1) <= fecha <= primavera_fin):
        return "Primavera"
    elif verano_inicio <= fecha <= verano_fin:
        return "Verano"
    elif otono_inicio <= fecha <= otono_fin:
        return "Otoño"
    elif (invierno_inicio <= fecha <= (12, 31)) or ((1, 1) <= fecha <= invierno_fin):
        return "Invierno"


def pedir_mes():
  mes = int(input("Ingrese el mes (1-12): "))
  dia = int(input("Ingrese el día (1-31): "))


  if 1 <= mes <= 12 and 1 <= dia <= 31:
      estacion = determinar_estacion(mes, dia)
      print(f"La fecha {mes}/{dia} pertenece a la estación: {estacion}")
  else:
      print("Fecha inválida. Por favor, ingrese un mes entre 1 y 12, y un día entre 1 y 31.")
      
# Escribe un programa que solicite al usuario un número entre 1 y 7 y luego determine a qué día de la semana corresponde (1 para lunes, 2 para martes, ..., 7 para domingo). Además, si el número ingresado corresponde a un día de fin de semana (sábado o domingo), el programa debe indicar que es un día no laboral.
def es_laboral():
  numero = int(input("Ingrese un número entre 1 y 7"))

  if numero < 1 or numero > 7:
    print("Número inválido. Ingrese un número entre 1 y 7.")
  else:
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    dia = dias_semana[numero - 1]
    print(f"Cae en {dia}")

    if dia in ["Sabado", "Domingo"]:
      print("Es fin de semana! Día no laboral")
    else:
      print("Es un día laboral.")

# Crea un programa que simule un sistema de calificación para una tienda en línea. Solicita al usuario que ingrese una calificación de 1 a 5 estrellas y luego pide una breve reseña. Si la calificación es de 4 o 5 estrellas, imprime "Gracias por tu reseña positiva". Si la calificación es de 3 estrellas, imprime "Gracias por tu reseña, trabajaremos en mejorar". Si la calificación es de 1 o 2 estrellas, solicita al usuario que proporcione más detalles sobre su experiencia negativa para mejorar el servicio.

def resegnas():
  calificacion = int(input('Ingresa el numero de estrellas'))
  resena = input("Ingresa una breve resena")
  
  if(calificacion >= 4 ):
    print("Gracias por tu reseña positiva")
  elif(calificacion == 3 ):
    print("Gracias por tu reseña, trabajaremos en mejorar")
  else:
    input(f"Ingresa mas detalles")
#1 imc()
#2 promedio()
#3 capicua()
#4 es_triangulo()
#5 es_primo()
#7 cajero()
#8 pedir_mes()
#9 es_laboral()
#10 resegnas()