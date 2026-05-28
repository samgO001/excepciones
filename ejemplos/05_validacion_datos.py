# ============================================
# Ejemplo 5: Validación de datos con excepciones
# ============================================

print("Ejemplo: Validación de datos\n")

def validar_nombre(nombre):
    if not isinstance(nombre, str) or len(nombre.strip()) == 0:
        raise ValueError("El nombre no puede estar vacío.")
    if any(char.isdigit() for char in nombre):
        raise ValueError("El nombre no puede contener números.")
    return nombre.strip().title()

def validar_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError(f"El correo '{email}' no tiene un formato válido.")
    return email.lower()

def validar_nota(nota):
    nota = float(nota)  # puede lanzar ValueError
    if not (0.0 <= nota <= 5.0):
        raise ValueError("La nota debe estar entre 0.0 y 5.0.")
    return nota

def registrar_estudiante(nombre, email, nota):
    """Registra un estudiante con validación completa."""
    print(f"Registrando: {nombre} | {email} | {nota}")
    nombre_ok  = validar_nombre(nombre)
    email_ok   = validar_email(email)
    nota_ok    = validar_nota(nota)
    print(f"  Registro exitoso → {nombre_ok}, {email_ok}, nota: {nota_ok}")

# Pruebas
casos = [
    ("Ana Gómez",  "ana@correo.com",  "4.5"),   # válido
    ("",           "ana@correo.com",  "4.5"),   # nombre vacío
    ("Juan123",    "juan@correo.com", "3.0"),   # nombre con número
    ("Luis Pérez", "luissinmail",     "4.0"),   # email inválido
    ("María",      "maria@correo.co", "6.0"),   # nota fuera de rango
    ("Pedro",      "pedro@correo.co", "abc"),   # nota no numérica
]

for nombre, email, nota in casos:
    print()
    try:
        registrar_estudiante(nombre, email, nota)
    except ValueError as e:
        print(f"   Error de validación: {e}")
    except Exception as e:
        print(f"   Error inesperado: {e}")