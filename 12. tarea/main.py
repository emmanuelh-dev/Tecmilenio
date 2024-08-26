# Elabora un programa que realice el cálculo del precio de entrada para los visitantes que desean recorrer
# el Museo de Antropología e Historia de tu ciudad, el cual debe considerar los siguientes descuentos:

# Tipo de visitante:
# - Adulto mayor: 12%
# - Profesor: 10%
# - Estudiante: 10%

# El precio de entrada es de $30 para menores de edad y $45 para mayores de 18 años,
# mientras que los niños menores de tres años no pagan boleto.

# Estas son las restricciones para elaborar el programa:
# - El usuario del programa debe indicar el número de visitantes que pagarán boleto,
#   si son mayores de edad y el tipo de visitante.
# - La tabla anterior debe estar programada como una tabla de verdad y solo aplicar un tipo de descuento por boleto.
# - Tienes la libertad de utilizar un ciclo for o while, según el que consideres más apropiado.
# - Independientemente del tipo de ciclo, este deberá tener una cláusula break, así como una continue.
# - El programa deberá indicar el total a pagar de todas las personas, considerando sus respectivos descuentos.

def numeros(text):
    while True:
        try:
            value = int(input(text))
            return value
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números válidos.")
            continue

def tipo_visitante_valido():
    opciones = ['adulto mayor', 'profesor', 'estudiante', 'ninguno']
    while True:
        tipo = input("Ingresa el tipo de visitante (adulto mayor, profesor, estudiante, ninguno): ").lower()
        if tipo == '':
          return 'ninguno'
        if tipo in opciones:
            return tipo
        else:
            print("Tipo de visitante no válido. Por favor, selecciona una opción válida.")

def museo():
    descuentos = {
        'adulto mayor': 0.12,
        'profesor': 0.10,
        'estudiante': 0.10
    }

    precio_menor = 30
    precio_adulto = 45
    total_a_pagar = 0

    while True:
        # Solicitar numero de visitantes
        visitantes = numeros("Ingresa el número de visitantes: ")
        if visitantes <= 0:
            print("El número de visitantes debe ser mayor a cero.")
            continue

        # Procesar cada visitante
        for i in range(visitantes):
            edad = numeros(f"Ingrese la edad del visitante {i + 1}: ")

            if edad < 3:
                print("El visitante no paga boleto por ser menor de 3 años.")
                continue  # Saltar a la siguiente iteracinn, ya que no paga

            # Determinar precio base según la edad
            if edad < 18:
                precio = precio_menor
            else:
                precio = precio_adulto

            # Validar tipo de visitante
            tipo_visitante = tipo_visitante_valido()

            # Verificar si aplica algún descuento
            if tipo_visitante in descuentos:
                descuento = descuentos[tipo_visitante]
                precio_con_descuento = precio * (1 - descuento)
                print(f"Aplicando un descuento del {int(descuento * 100)}%. Precio final: ${precio_con_descuento:.2f}")
            else:
                print(f"No aplica descuento. Precio final: ${precio:.2f}")
                precio_con_descuento = precio

            # Sumar al total
            total_a_pagar += precio_con_descuento

        # Imprimir el total a pagar
        print(f"Total a pagar por {visitantes} visitantes: ${total_a_pagar:.2f}")
        break

museo()
