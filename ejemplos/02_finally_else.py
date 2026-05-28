# ============================================
# Ejemplo 2: finally y else
# ============================================

print("Ejemplo: finally y else\n")

# else se ejecuta solo si NO ocurrió ninguna excepción
# finally se ejecuta SIEMPRE, haya o no excepción

print("Caso 1: Sin error (se ejecuta else) ")
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: División entre cero.")
else:
    print(f"División exitosa. Resultado: {resultado}")
finally:
    print("Bloque finally: esto siempre se ejecuta.\n")

print("Caso 2: Con error (no se ejecuta else) ")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División entre cero.")
else:
    print(f"División exitosa. Resultado: {resultado}")
finally:
    print("Bloque finally: esto siempre se ejecuta.")