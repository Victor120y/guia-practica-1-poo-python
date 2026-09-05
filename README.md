# Actividad Evaluada 1: Guía de Trabajo
**Desarrollo y Reutilización de Software — CICLO II/2026**
**Universidad de El Salvador, Facultad Multidisciplinaria de Occidente**

Implementación en **Python** de los 5 ejercicios sobre Programación
Orientada a Objetos (POO): abstracción, encapsulación, herencia y
polimorfismo.

## Estructura del repositorio

```
Guia_Practica_1/
├── Ejercicio1_AbstraccionDatos/
│   └── cuenta_bancaria.py
├── Ejercicio2_Encapsulacion/
│   └── empleado.py
├── Ejercicio3_HerenciaSimple/
│   └── vehiculo_coche.py
├── Ejercicio4_Polimorfismo/
│   └── animales_polimorfismo.py
├── Ejercicio5_HerenciaMultinivel/
│   └── herencia_multinivel.py
└── README.md
```

## Requisitos

- Python 3.8 o superior instalado ([python.org/downloads](https://www.python.org/downloads/))

## Cómo ejecutar cada ejercicio

Desde la terminal, dentro de la carpeta de cada ejercicio. El comando varía
según el sistema operativo:

**Windows (usando el lanzador `py`):**
```bash
py cuenta_bancaria.py
py empleado.py
py vehiculo_coche.py
py animales_polimorfismo.py
py herencia_multinivel.py
```

**macOS / Linux:**
```bash
python3 cuenta_bancaria.py
python3 empleado.py
python3 vehiculo_coche.py
python3 animales_polimorfismo.py
python3 herencia_multinivel.py
```

> **Nota:** en Windows, si al instalar Python marcaste la opción "Add
> python.exe to PATH", también puede funcionar el comando `python` en vez de
> `py`. Verifica primero con `py --version` o `python --version` cuál
> reconoce tu terminal.

## Resumen de conceptos aplicados

| Ejercicio | Concepto principal | Clases |
|---|---|---|
| 1 | Abstracción de datos | `CuentaBancaria` |
| 2 | Encapsulación (properties) | `Empleado` |
| 3 | Herencia simple | `Vehiculo` → `Coche` |
| 4 | Polimorfismo | `Animal` → `Perro`, `Gato` |
| 5 | Herencia multinivel | `Animal` → `Mamifero` → `Perro` |

## Notas de implementación

- **Encapsulación en Python:** se usa el prefijo doble guion bajo (`__atributo`)
  para simular atributos privados, y `@property` / `@nombre.setter` para
  exponer getters y setters controlados, de forma equivalente a las
  propiedades de C#.
- Cada script incluye una función `main()` con ejemplos de uso y casos de
  validación (por ejemplo, montos negativos o edades fuera de rango).

## Autor(es)
- **Victor Andrés Hernández Avilés**
- **José Ricardo Navarro Delgado**

