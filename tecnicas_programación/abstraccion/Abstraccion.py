# Ejemplo de Abstracción
# La abstracción nos permite ocultar la complejidad interna y exponer solo lo necesario.

class CuentaBancaria:
    def __init__(self):
        # El atributo _saldo está protegido (convención de un guion bajo),
        # el usuario no debería modificarlo directamente.
        self._saldo = 0

    def depositar(self, cantidad):
        """Método público para ingresar dinero."""
        # Buena práctica: Validar que los datos sean correctos antes de procesar
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso: +{cantidad}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        """Método público para sacar dinero."""
        # Aquí ocultamos la lógica de verificación de fondos al usuario
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro exitoso: -{cantidad}")
        else:
            print("Operación rechazada: Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual disponible: {self._saldo}")

# --- Ejecución del código ---
print("--- Inicio del ejemplo de Abstracción ---")
cuenta = CuentaBancaria()

# El usuario interactúa con la interfaz simple (métodos) sin preocuparse por la lógica interna
cuenta.depositar(100)
cuenta.retirar(30)
cuenta.retirar(200) # Intento de sobregiro para probar la lógica
cuenta.mostrar_saldo()
