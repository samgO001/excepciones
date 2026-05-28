# ============================================
# Ejemplo 1: try y except básico
# ============================================

print(" Ejemplo: try y except \n")

# Ejemplo básico: división entre cero
print("Caso 1: ZeroDivisionError ")
try:
    resultado = 10 / 0
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")

# Ejemplo básico: conversión de tipo
print("\nCaso 2: ValueError ")
try:
    numero = int("hola")
    print(f"Número: {numero}")
except ValueError:
    print("Error: El valor ingresado no es un número válido.")

# Captura general de excepción
print("\nCaso 3: Excepción genérica ")
try:
    lista = [1, 2, 3]
    print(lista[10])
except Exception as e:
    print(f"Ocurrió un error: {e}")