# ============================================
# Ejemplo 4: Lanzamiento de excepciones con raise
# ============================================

print(" Ejemplo: raise \n")

def verificar_edad(edad):
    """Valida que la edad sea un valor positivo y razonable."""
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad > 120:
        raise ValueError("La edad ingresada no es realista.")
    return f"Edad válida: {edad} años."

# Caso 1: Edad válida
print("Caso 1: Edad válida ")
try:
    print(verificar_edad(25))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Caso 2: Edad negativa
print("\nCaso 2: Edad negativa")
try:
    print(verificar_edad(-5))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Caso 3: Tipo incorrecto
print("\nCaso 3: Tipo incorrecto")
try:
    print(verificar_edad("veinte"))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Caso 4: Re-lanzar una excepción
print("\n Caso 4: Re-lanzar excepción ")
try:
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Excepción capturada internamente, re-lanzando")
        raise  # vuelve a lanzar la misma excepción
except ZeroDivisionError:
    print("Excepción capturada en el bloque externo.")