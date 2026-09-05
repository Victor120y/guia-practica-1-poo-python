"""
Ejercicio 1: Implementación de Abstracción de Datos
-----------------------------------------------------
Objetivo: Implementar un tipo de datos abstracto que oculta detalles de implementación.

La clase CuentaBancaria utiliza abstracción de datos para ocultar el detalle
de la implementación del saldo. El saldo solo puede ser accedido o modificado
a través de los métodos públicos: Depositar, Retirar y ObtenerSaldo.
"""


class CuentaBancaria:
    """Representa una cuenta bancaria simple con operaciones básicas."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        # Atributo "privado" (por convención, prefijo doble guion bajo)
        # Esto oculta el detalle de implementación del saldo.
        self.__saldo = saldo_inicial

    def depositar(self, monto: float) -> None:
        """Permite agregar dinero a la cuenta. Valida que el monto sea positivo."""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.__saldo += monto
        print(f"Depósito exitoso de ${monto:.2f}. Nuevo saldo: ${self.__saldo:.2f}")

    def retirar(self, monto: float) -> None:
        """Permite retirar dinero de la cuenta. Valida monto positivo y fondos suficientes."""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro.")
        self.__saldo -= monto
        print(f"Retiro exitoso de ${monto:.2f}. Nuevo saldo: ${self.__saldo:.2f}")

    def obtener_saldo(self) -> float:
        """Devuelve el saldo actual de la cuenta."""
        return self.__saldo


def main():
    print("=== Ejercicio 1: Abstracción de Datos ===\n")
    cuenta = CuentaBancaria("Victor Pérez", 100.0)
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo inicial: ${cuenta.obtener_saldo():.2f}\n")

    cuenta.depositar(50.0)
    cuenta.retirar(30.0)

    print(f"\nSaldo final: ${cuenta.obtener_saldo():.2f}")

    # Ejemplo de validaciones
    try:
        cuenta.retirar(1000.0)
    except ValueError as e:
        print(f"\nError controlado: {e}")

    try:
        cuenta.depositar(-10.0)
    except ValueError as e:
        print(f"Error controlado: {e}")


if __name__ == "__main__":
    main()
