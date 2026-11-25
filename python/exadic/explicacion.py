
# ==================================================
#                 DICCIONARIOS EN PYTHON
# ==================================================


# 1. CREAR UN DICCIONARIO
# Un diccionario almacena datos mediante claves y valores.
# Se utilizan llaves {}.

estudiante = {
    "nombre": "Breyner",
    "edad": 17,
    "nota": 4.5
}

print("Diccionario creado:")
print(estudiante)


# 2. CREAR UN DICCIONARIO VACIO
# Podemos crear un diccionario sin datos para llenarlo despues.

estudiante = {}

print("Diccionario vacio:")
print(estudiante)


# 3. AGREGAR INFORMACION A UN DICCIONARIO
# Para agregar datos utilizamos una clave entre corchetes.
# Si la clave no existe, se agrega.
# Si ya existe, se modifica su valor.

estudiante = {}

estudiante["nombre"] = "Breyner"
estudiante["edad"] = 17
estudiante["nota"] = 4.5

print("Diccionario con datos:")
print(estudiante)


# 4. LLENAR UN DICCIONARIO CON INPUT
# Podemos solicitar los datos al usuario y guardarlos.

estudiante = {}

estudiante["nombre"] = input("Ingrese el nombre: ")
estudiante["edad"] = int(input("Ingrese la edad: "))
estudiante["nota"] = float(input("Ingrese la nota: "))

print("Datos del estudiante:")
print(estudiante)


# 5. CONSULTAR INFORMACION
# Para consultar un valor utilizamos su clave.

print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Nota:", estudiante["nota"])


# 6. MODIFICAR INFORMACION
# Para modificar un dato solamente asignamos un nuevo valor
# a una clave que ya existe.

estudiante["edad"] = 18

print("Edad modificada:")
print(estudiante)


# 7. ELIMINAR INFORMACION
# pop() elimina un elemento indicando su clave.

estudiante.pop("nota")

print("Diccionario despues de eliminar la nota:")
print(estudiante)


# 8. IMPRIMIR UN DICCIONARIO
# print() permite mostrar todo el diccionario.

estudiante = {
    "nombre": "Breyner",
    "edad": 17,
    "nota": 4.5
}

print(estudiante)


# 9. RECORRER UN DICCIONARIO CON FOR
# Cuando recorremos un diccionario directamente,
# la variable recibe sus claves.

for x in estudiante:
    print(x)


# 10. IMPRIMIR LOS VALORES DEL DICCIONARIO
# Utilizamos la clave para obtener su valor.

for x in estudiante:
    print(estudiante[x])


# 11. IMPRIMIR CLAVES Y VALORES
# Podemos mostrar la clave y su valor al mismo tiempo.

for x in estudiante:
    print(x, ":", estudiante[x])


# 12. LLENAR UN DICCIONARIO CON UN FOR
# En este ejemplo registramos 3 estudiantes.
# Utilizamos x como clave para identificar cada estudiante.
# Cada estudiante tiene su propio diccionario.

estudiantes = {}

for x in range(3):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))

    estudiantes[x] = {
        "nombre": nombre,
        "edad": edad
    }

print("Todos los estudiantes:")
print(estudiantes)


# 13. RECORRER UN DICCIONARIO CON OTROS DICCIONARIOS
# Podemos acceder a los datos internos utilizando sus claves.

for x in estudiantes:
    print("Nombre:", estudiantes[x]["nombre"])
    print("Edad:", estudiantes[x]["edad"])


# 14. GUARDAR LISTAS DENTRO DE UN DICCIONARIO
# Un diccionario puede almacenar listas como valores.
# En este ejemplo cada estudiante tiene una lista de notas.

estudiantes = {
    0: {
        "nombre": "Ana",
        "notas": [4.0, 3.5, 5.0]
    },
    1: {
        "nombre": "Luis",
        "notas": [3.0, 4.5, 4.0]
    }
}

print("Diccionario con listas:")
print(estudiantes)


# 15. RECORRER LAS LISTAS DENTRO DEL DICCIONARIO
# Utilizamos un for para recorrer los estudiantes
# y otro for para recorrer las notas de cada estudiante.

for x in estudiantes:
    print("Estudiante:", estudiantes[x]["nombre"])

    for nota in estudiantes[x]["notas"]:
        print("Nota:", nota)


# 16. CONTAR LOS ELEMENTOS DE UN DICCIONARIO
# len() permite conocer cuantas claves tiene el diccionario.

print("Cantidad de estudiantes:", len(estudiantes))


# 17. EJEMPLO COMPLETO: REGISTRO DE PRODUCTOS
# Creamos un diccionario vacio.
# Registramos 5 productos con sus respectivos precios.
# Guardamos cada producto dentro de otro diccionario.
# Finalmente recorremos e imprimimos toda la informacion.

productos = {}

for x in range(5):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))

    productos[x] = {
        "nombre": nombre,
        "precio": precio
    }

print("REGISTRO DE PRODUCTOS")

for x in productos:
    print("Producto:", productos[x]["nombre"])
    print("Precio:", productos[x]["precio"])


# ==================================================
#             FIN DE LA GUIA DE DICCIONARIOS
# ==================================================
