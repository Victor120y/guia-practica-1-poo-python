"""
Ejercicio 2: Encapsulación y Control de Acceso
-------------------------------------------------
Objetivo: Aplicar la encapsulación para proteger los datos y controlar el
acceso a los métodos de una clase.

La clase Empleado tiene dos atributos privados: nombre y edad. Se accede a
ellos mediante propiedades (property en Python), y la edad solo puede
modificarse con un valor válido (mayor que 0 y menor que 100).
"""


class Empleado:
    """Representa a un empleado con nombre y edad controlados por encapsulación."""

    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.edad = edad  # Usa el setter para validar desde la creación

    @property
    def nombre(self) -> str:
        """Getter para el nombre."""
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Setter para el nombre, valida que no esté vacío."""
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre

    @property
    def edad(self) -> int:
        """Getter para la edad."""
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        """Setter para la edad, valida que sea mayor que 0 y menor que 100."""
        if not (0 < nueva_edad < 100):
            raise ValueError("La edad debe ser mayor que 0 y menor que 100.")
        self.__edad = nueva_edad

    def __str__(self) -> str:
        return f"Empleado(nombre={self.__nombre}, edad={self.__edad})"


def main():
    print("=== Ejercicio 2: Encapsulación y Control de Acceso ===\n")
    empleado = Empleado("Ana López", 28)
    print(empleado)

    # Modificar mediante el setter (propiedad)
    empleado.edad = 30
    print(f"Edad actualizada: {empleado.edad}")

    empleado.nombre = "Ana María López"
    print(f"Nombre actualizado: {empleado.nombre}")

    # Ejemplo de validación fallida
    try:
        empleado.edad = 150
    except ValueError as e:
        print(f"\nError controlado: {e}")

    try:
        empleado.edad = -5
    except ValueError as e:
        print(f"Error controlado: {e}")


if __name__ == "__main__":
    main()
