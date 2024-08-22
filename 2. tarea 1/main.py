import math

def resolver_formula_general():
    # Pedir los valores de a, b y c
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    c = float(input("Introduce el valor de c: "))
    
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    # Verificar si el discriminante es negativo, positivo o cero
    if discriminante > 0:
        # Dos soluciones reales
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Las soluciones son {raiz1} y {raiz2}"
    elif discriminante == 0:
        # Una solución real (raíces iguales)
        raiz = -b / (2*a)
        return f"La solución es {raiz}"
    else:
        # Soluciones complejas
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        return f"Las soluciones son {parte_real} + {parte_imaginaria}i y {parte_real} - {parte_imaginaria}i"

# Llamar a la función
resultado = resolver_formula_general()
print(resultado)
