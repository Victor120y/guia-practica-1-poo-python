"""
Ejercicio 5: Herencia Multinivel y Sobrescritura de Métodos

Objetivo: Demostrar herencia multinivel y sobrescritura de métodos.

Jerarquía: Animal (base) -> Mamifero (intermedia) -> Perro (derivada).
Perro hereda de Mamifero (que a su vez hereda de Animal) y sobrescribe
el método hacer_sonido().
"""


class Animal:
    """Clase base."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    def hacer_sonido(self) -> str:
        return f"{self.nombre} hace un sonido genérico."


class Mamifero(Animal):
    """Clase intermedia que hereda de Animal y añade el método alimentar()."""

    def alimentar(self) -> str:
        return f"{self.nombre} está amamantando a sus crías."


class Perro(Mamifero):
    """Clase derivada que hereda de Mamifero (y transitivamente de Animal)."""

    def hacer_sonido(self) -> str:
        return f"{self.nombre} dice: ¡Guau guau!"


def main():
    print("* Ejercicio 5: Herencia Multinivel y Sobrescritura de Métodos * \n")

    firulais = Perro("Firu")

    # Método sobrescrito (definido en Perro)
    print(firulais.hacer_sonido())

    # Método heredado de Mamifero
    print(firulais.alimentar())

    # Verificación de la jerarquía de herencia
    print(f"\n¿Firu es instancia de Animal? {isinstance(firulais, Animal)}")
    print(f"¿Firu es instancia de Mamifero? {isinstance(firulais, Mamifero)}")
    print(f"¿Firu es instancia de Perro? {isinstance(firulais, Perro)}")


if __name__ == "__main__":
    main()
