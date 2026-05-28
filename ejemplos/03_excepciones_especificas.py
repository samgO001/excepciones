# ============================================
# Ejemplo 3: Excepciones específicas
# ============================================

print(" Ejemplo: Manejo de excepciones específicas \n")

def procesar_dato(valor, indice):
    """Función que puede generar varios tipos de errores."""
    lista = [10, 20, 30]
    numero = int(valor)       # puede lanzar ValueError
    elemento = lista[indice]  # puede lanzar IndexError
    return numero / elemento  # puede lanzar ZeroDivisionError

# Caso 1: ValueError
print("Caso 1: ValueError ")
try:
    procesar_dato("abc", 0)
except ValueError:
    print("Error: No se pudo convertir el valor a entero.")
except IndexError:
    print("Error: El índice no existe en la lista.")
except ZeroDivisionError:
    print("Error: División entre cero.")

# Caso 2: IndexError
print("\nCaso 2: IndexError ")
try:
    procesar_dato("5", 10)
except ValueError:
    print("Error: No se pudo convertir el valor a entero.")
except IndexError:
    print("Error: El índice no existe en la lista.")
except ZeroDivisionError:
    print("Error: División entre cero.")

# Caso 3: múltiples excepciones en una sola línea
print("\nCaso 3: Captura múltiple en una línea ")
try:
    procesar_dato("xyz", 99)
except (ValueError, IndexError) as e:
    print(f"Error de valor o índice: {e}")