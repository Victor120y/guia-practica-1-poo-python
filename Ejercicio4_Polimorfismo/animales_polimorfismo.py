""" Ejercicio 4: Polimorfismo

Objetivo: Implementar polimorfismo utilizando métodos sobrescritos.

La clase base Animal define Hacer_sonido(). Las clases Perro y Gato
sobrescriben ese método. Al recorrer una lista de tipo Animal, cada objeto
responde con su propio comportamiento (polimorfismo).
"""


class Animal:
    """Clase base que representa un animal genérico."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    def Hacer_sonido(self) -> str:
        return f"{self.nombre} hace un sonido genérico."


class Perro(Animal):
    """Clase derivada que sobrescribe Hacer_sonido()."""

    def Hacer_sonido(self) -> str:
        return f"{self.nombre} dice: ¡Guau guau!"


class Gato(Animal):
    """Clase derivada que sobrescribe Hacer_sonido()."""

    def Hacer_sonido(self) -> str:
        return f"{self.nombre} dice: ¡Miau!"


def main():
    print("=== Ejercicio 4: Polimorfismo ===\n")

    # Lista de referencias de tipo Animal (polimorfismo)
    animales: list[Animal] = [
        Perro("Firulais"),
        Gato("Michi"),
        Animal("Animal desconocido"),
    ]

    for animal in animales:
        # Aunque la referencia es de tipo Animal, se ejecuta el método
        # sobrescrito correspondiente a la clase real del objeto.
        print(animal.Hacer_sonido())


if __name__ == "__main__":
    main()
