# ============================================
# Ejemplo 6: Excepciones personalizadas
# ============================================

print("Ejemplo: Excepciones personalizadas \n")

# --- Definición de excepciones personalizadas ---

class ErrorAplicacion(Exception):
    """Clase base para excepciones de la aplicación."""
    pass

class SaldoInsuficienteError(ErrorAplicacion):
    """Se lanza cuando el saldo no alcanza para la operación."""
    def __init__(self, saldo_actual, monto_requerido):
        self.saldo_actual    = saldo_actual
        self.monto_requerido = monto_requerido
        super().__init__(
            f"Saldo insuficiente. Tiene ${saldo_actual:.2f} "
            f"pero necesita ${monto_requerido:.2f}."
        )

class CuentaBloqueadaError(ErrorAplicacion):
    """Se lanza cuando la cuenta está bloqueada."""
    def __init__(self, motivo="razones de seguridad"):
        super().__init__(f"Cuenta bloqueada por {motivo}.")

class MontoInvalidoError(ErrorAplicacion):
    """Se lanza cuando el monto es negativo o cero."""
    def __init__(self, monto):
        super().__init__(f"El monto ${monto} no es válido. Debe ser mayor a cero.")

# --- Clase que usa las excepciones personalizadas ---

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular  = titular
        self.saldo    = saldo_inicial
        self.bloqueada = False

    def retirar(self, monto):
        if self.bloqueada:
            raise CuentaBloqueadaError()
        if monto <= 0:
            raise MontoInvalidoError(monto)
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)
        self.saldo -= monto
        return self.saldo

    def bloquear(self):
        self.bloqueada = True

# --- Pruebas ---

cuenta = CuentaBancaria("Carlos Ruiz", saldo_inicial=500.0)
operaciones = [
    ("Retiro normal",        200.0),
    ("Retiro con saldo justo", 300.0),
    ("Monto inválido",       -50.0),
    ("Saldo insuficiente",   600.0),
]

for descripcion, monto in operaciones:
    print(f" {descripcion} (monto: ${monto}) ")
    try:
        nuevo_saldo = cuenta.retirar(monto)
        print(f"  Retiro exitoso. Saldo restante: ${nuevo_saldo:.2f}")
    except SaldoInsuficienteError as e:
        print(f"   {e}")
    except MontoInvalidoError as e:
        print(f"   {e}")
    except CuentaBloqueadaError as e:
        print(f"   {e}")
    print()

# Bloquear cuenta y probar
print(" Cuenta bloqueada ")
cuenta.bloquear()
try:
    cuenta.retirar(10)
except CuentaBloqueadaError as e:
    print(f"   {e}")