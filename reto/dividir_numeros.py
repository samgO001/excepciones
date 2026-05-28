# ============================================
# Reto – Manejo de excepciones
# GA1-220501096-01-AA1-EV05
# ============================================

def dividir_numeros():
    """
    Solicita dos números al usuario, realiza la división
    y maneja correctamente ValueError y ZeroDivisionError.
    Siempre muestra 'Operación finalizada' al terminar.
    """
    try:
        # Solicitar datos al usuario
        num1 = int(input("Ingrese el primer número (dividendo): "))
        num2 = int(input("Ingrese el segundo número (divisor):  "))

        # Realizar la división
        resultado = num1 / num2

    except ValueError:
        print("\n Error: Solo se permiten números enteros. "
              "Por favor no ingrese letras ni caracteres especiales.")

    except ZeroDivisionError:
        print("\n Error: No es posible dividir entre cero. "
              "El divisor debe ser un número diferente a 0.")

    else:
        # Este bloque solo se ejecuta si NO hubo excepción
        print(f"\nResultado: {num1} ÷ {num2} = {resultado}")

    finally:
        # Este bloque se ejecuta SIEMPRE
        print("\nOperación finalizada")


# ── Punto de entrada ──────────────────────────────────────
if __name__ == "__main__":
  
    print("   Calculadora de División con Excepciones")

    dividir_numeros()