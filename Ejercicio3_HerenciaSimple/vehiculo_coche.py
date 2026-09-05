"""
Ejercicio 3: Herencia Simple
-------------------------------
Objetivo: Implementar herencia simple para extender las funcionalidades de
una clase base.

La clase Coche hereda de Vehiculo y añade su propio método Conducir(),
además de poder usar los métodos heredados Arrancar() y Detener().
"""


class Vehiculo:
    """Clase base que representa un vehículo genérico."""

    def __init__(self, marca: str):
        self.marca = marca

    def arrancar(self) -> None:
        print(f"{self.marca}: el vehículo ha arrancado.")

    def detener(self) -> None:
        print(f"{self.marca}: el vehículo se ha detenido.")


class Coche(Vehiculo):
    """Clase derivada que extiende Vehiculo añadiendo la capacidad de conducir."""

    def __init__(self, marca: str, modelo: str):
        super().__init__(marca)
        self.modelo = modelo

    def conducir(self) -> None:
        print(f"{self.marca} {self.modelo}: conduciendo por la carretera.")


def main():
    print("=== Ejercicio 3: Herencia Simple ===\n")
    mi_coche = Coche("Toyota", "Corolla")

    # Métodos heredados de Vehiculo
    mi_coche.arrancar()
    # Método propio de Coche
    mi_coche.conducir()
    # Método heredado de Vehiculo
    mi_coche.detener()


if __name__ == "__main__":
    main()
