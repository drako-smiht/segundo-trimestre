# ============================================================
# EJEMPLOS DE PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ============================================================

# 1. CLASE Y OBJETO
# Una clase es el molde o plano; un objeto es una instancia creada
# a partir de ese molde.

class Persona:
    # __init__ es el constructor: se ejecuta al crear un objeto.
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.edad = edad      # Atributo público

    # Un método representa una acción que puede realizar el objeto.
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"


persona1 = Persona("Ana", 16)
persona2 = Persona("Carlos", 17)
    
print(persona1.presentarse())
print(persona2.presentarse())


# 2. ENCAPSULAMIENTO
# Se usa para proteger los datos y controlar cómo se leen o modifican.
# Un solo guion bajo indica que un atributo es privado por convención.

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
        else:
            print("La cantidad debe ser mayor que cero")

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida")

    def consultar_saldo(self):
        return self._saldo


cuenta = CuentaBancaria("Lucía", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print("Saldo:", cuenta.consultar_saldo())


# 3. HERENCIA
# Una clase hija hereda atributos y métodos de una clase padre.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "Este animal hace un sonido"


class Perro(Animal):
    # Sobrescribir hablar reemplaza el método heredado.
    def hablar(self):
        return f"{self.nombre} dice: Guau"


class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau"


animales = [Perro("Max"), Gato("Misu")]

for animal in animales:
    print(animal.hablar())


# 4. POLIMORFISMO
# Diferentes objetos pueden responder al mismo método de formas distintas.
# Aquí se usa polimorfismo con el método hablar().

for animal in animales:
    print(animal.hablar())


# 5. ABSTRACCIÓN
# Una clase abstracta define un modelo general. Sus clases hijas deben
# implementar los métodos necesarios.

from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2


rectangulo = Rectangulo(4, 3)
circulo = Circulo(5)

print("Área del rectángulo:", rectangulo.calcular_area())
print("Área del círculo:", circulo.calcular_area())


# 6. GETTERS Y SETTERS CON @property
# Permiten consultar o modificar un dato protegido con validaciones.

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self._nota = 0
        self.nota = nota  # Se llama al setter

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 5:
            self._nota = valor
        else:
            print("La nota debe estar entre 0 y 5")


estudiante = Estudiante("María", 4.5)
print(estudiante.nombre, "- Nota:", estudiante.nota)

estudiante.nota = 8  # Valor inválido: no cambia la nota
print("Nota después del intento:", estudiante.nota)
