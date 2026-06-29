"""Práctica de katas de Python.

Este archivo agrupa ejercicios de funciones, map, filter, reduce,
excepciones, clases y condicionales.

Los ejercicios interactivos no se ejecutan automáticamente para evitar
bloqueos al importar o ejecutar pruebas.
"""

import math
import unicodedata
from difflib import get_close_matches
from functools import reduce


# 1. Devuelve la frecuencia de cada letra ignorando espacios y tildes.
def quitar_tildes(texto):
    """Devuelve un texto sin tildes."""
    texto_normalizado = unicodedata.normalize("NFD", texto)
    return "".join(
        caracter
        for caracter in texto_normalizado
        if unicodedata.category(caracter) != "Mn"
    )


def frecuencia_letras(texto):
    """Devuelve un diccionario con la frecuencia de cada letra del texto."""
    texto = quitar_tildes(texto.lower())
    return {
        letra: texto.count(letra)
        for letra in sorted(set(texto))
        if letra.isalpha()
    }


# 2. Devuelve una lista con el doble de cada valor usando map().
def doblar_valores(lista):
    """Devuelve una lista con cada valor multiplicado por 2."""
    return list(map(lambda x: x * 2, lista))


# 3. Devuelve palabras que contienen la palabra o fragmento objetivo.
def filtrar_palabras(palabras, fragmento):
    """Filtra las palabras que contienen el fragmento indicado."""
    return list(filter(lambda palabra: fragmento in palabra, palabras))


# 4. Calcula elemento_a - elemento_b usando map().
def diferencia(lista_a, lista_b):
    """Devuelve la diferencia entre elementos correspondientes de dos listas."""
    return list(map(lambda a, b: a - b, lista_a, lista_b))


# 5. Calcula la media y devuelve estado 'aprobado' o 'suspenso'.
def estado_calificacion(notas):
    """Devuelve 'aprobado' si la media es mayor o igual que 5; si no, 'suspenso'."""
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")

    media = sum(notas) / len(notas)
    return "aprobado" if media >= 5 else "suspenso"


# 6. Calcula el factorial de forma recursiva.
def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if not isinstance(n, int):
        raise TypeError("El número debe ser entero.")
    if n < 0:
        raise ValueError("El número no puede ser negativo.")

    return 1 if n == 0 else n * factorial(n - 1)


# 7. Convierte una lista de tuplas en una lista de strings usando map().
def tuplas_strings(tuplas):
    """Convierte cada tupla en un string, separando sus elementos con espacios."""
    return list(map(lambda tupla: " ".join(map(str, tupla)), tuplas))


# 8. Intenta dividir dos valores recibidos como texto y devuelve un mensaje.
def dividir_texto(texto_a, texto_b):
    """Convierte dos textos a número y devuelve su división o un mensaje de error."""
    try:
        a = float(texto_a)
        b = float(texto_b)
        return a / b
    except ValueError:
        return "Error: uno de los valores no es un número."
    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero."


# 9. Excluye mascotas prohibidas usando filter().
def excluir_mascotas(mascotas):
    """Devuelve una lista sin las mascotas prohibidas."""
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


# 10. Calcula el promedio; si la lista está vacía lanza ListaVaciaError.
class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""



def promedio_con_error(numeros):
    """Calcula el promedio de una lista o lanza ListaVaciaError si está vacía."""
    if not numeros:
        raise ListaVaciaError("La lista está vacía")
    return sum(numeros) / len(numeros)


# 11. Convierte y valida una edad entre 0 y 120.
def validar_edad(edad):
    """Valida que la edad sea un entero entre 0 y 120, ambos incluidos."""
    if not isinstance(edad, int):
        raise ValueError("La edad debe ser un número entero.")
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120.")
    return f"Edad válida: {edad} años"


# 12. Devuelve la longitud de cada palabra usando map().
def longitud_palabras(palabras):
    """Devuelve la longitud de cada palabra."""
    return list(map(len, palabras))


# 13. Devuelve tuplas (mayúscula, minúscula) sin letras repetidas usando map().
def mayus_minus_tuplas(palabras):
    """Devuelve una lista de tuplas con cada palabra en mayúsculas y minúsculas."""
    return list(map(lambda palabra: (palabra.upper(), palabra.lower()), set(palabras)))


# 14. Filtra palabras que empiezan por una letra concreta usando filter().
def filtrar_por_letra(palabras, letra):
    """Filtra palabras que empiezan por la letra indicada."""
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))


# 15. Aplica la lambda sumar_3 a una lista.
def suma_3(lista):
    """Devuelve una lista sumando 3 a cada elemento."""
    return list(map(lambda x: x + 3, lista))


# 16. Filtra palabras con longitud mayor que n usando filter().
def filtrar_longitud(palabras, n):
    """Filtra palabras cuya longitud es mayor que n."""
    return list(filter(lambda palabra: len(palabra) > n, palabras))


# 17. Convierte una lista de dígitos en un número usando reduce().
def digitos_a_numero(digitos):
    """Convierte una lista de dígitos en un único número."""
    if not digitos:
        raise ValueError("La lista de dígitos no puede estar vacía.")
    return reduce(lambda x, y: x * 10 + y, digitos)


# 18. Filtra estudiantes con calificación >= 90 usando filter().
def filtrar_estudiantes(estudiantes):
    """Filtra estudiantes con nota mayor o igual que 90."""
    return list(filter(lambda estudiante: estudiante[1] >= 90, estudiantes))


# 19. Crea una función lambda que filtre los números impares.
def impares(lista):
    """Devuelve los números impares de una lista."""
    return list(filter(lambda x: x % 2 != 0, lista))


# 20. Devuelve solo valores int usando filter(). Excluye bool por claridad.
def filtrar_enteros(lista):
    """Filtra valores enteros, excluyendo booleanos."""
    return list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), lista))


# 21. Crea una función que calcule el cubo.
def cubo(numero):
    """Devuelve el cubo de un número."""
    return numero ** 3


# 22. Obtén el producto total de los valores de una lista usando reduce().
def producto_total(lista):
    """Devuelve el producto acumulado de una lista de números."""
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return reduce(lambda x, y: x * y, lista)


# 23. Concatena una lista de palabras usando reduce().
def concatenar(palabras):
    """Concatena una lista de palabras separándolas por espacios."""
    if not palabras:
        return ""
    return reduce(lambda x, y: x + " " + y, palabras)


# 24. Calcula la diferencia total en los valores de una lista usando reduce().
def diferencia_total(lista):
    """Resta todos los elementos de una lista de izquierda a derecha."""
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return reduce(lambda x, y: x - y, lista)


# 25. Crea una función que cuente el número de caracteres en una cadena de texto.
def contar_caracteres(cadena):
    """Cuenta los caracteres de una cadena."""
    return len(cadena)


# 26. Crea una función lambda que calcule el resto de una división.
resto_division = lambda a, b: a % b


# 27. Crea una función que calcule el promedio de una lista de números.
def promedio_simple(lista):
    """Calcula el promedio de una lista de números."""
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return sum(lista) / len(lista)


# 28. Busca y devuelve el primer elemento duplicado en una lista.
def duplicado(lista):
    """Devuelve el primer elemento duplicado o None si no hay duplicados."""
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# 29. Enmascara todos los caracteres excepto los últimos cuatro.
def enmascarar_variable(variable):
    """Convierte una variable a texto y oculta sus caracteres excepto los cuatro últimos."""
    variable_str = str(variable)
    longitud = len(variable_str)

    if longitud <= 4:
        return variable_str

    return "#" * (longitud - 4) + variable_str[-4:]


# 30. Determina si dos palabras son anagramas.
def anagramas(palabra1, palabra2):
    """Devuelve True si dos palabras son anagramas."""
    palabra1 = quitar_tildes(palabra1.lower().replace(" ", ""))
    palabra2 = quitar_tildes(palabra2.lower().replace(" ", ""))
    return sorted(palabra1) == sorted(palabra2)


# 31. Solicita una lista de nombres y busca uno en ella.
def buscar_nombre():
    """Pide nombres al usuario y busca uno, mostrando sugerencias si no coincide."""
    nombres = input("Ingrese una lista de nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombre_a_buscar = input("Ingrese un nombre para buscar: ").strip()

    if nombre_a_buscar in nombres:
        print(f"{nombre_a_buscar} fue encontrado en la lista.")
        return

    sugerencias = get_close_matches(nombre_a_buscar, nombres, n=1, cutoff=0.4)
    if sugerencias:
        print(f"{nombre_a_buscar} no fue encontrado. ¿Quizás querías buscar '{sugerencias[0]}'?")
    else:
        print(f"{nombre_a_buscar} no fue encontrado en la lista.")


# 32. Busca un empleado por nombre completo.
def buscar_empleado(nombre_completo, empleados):
    """Busca un empleado y devuelve su puesto si existe."""
    for empleado in empleados:
        if empleado["nombre_completo"].lower() == nombre_completo.lower():
            return f"{nombre_completo} trabaja como {empleado['puesto']}."
    return f"{nombre_completo} no trabaja aquí."


# 33. Suma elementos correspondientes de dos listas.
def sumar_listas(lista1, lista2):
    """Suma los elementos correspondientes de dos listas."""
    return list(map(lambda x, y: x + y, lista1, lista2))


# 34. Crea la clase Arbol.
class Arbol:
    """Representa un árbol genérico con tronco y ramas."""

    def __init__(self, tronco, ramas=None):
        self.tronco = tronco
        self.ramas = ramas if ramas is not None else []

    def crecer_tronco(self):
        """Hace crecer el tronco una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Añade una nueva rama de longitud 1."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Hace crecer todas las ramas una unidad."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama situada en la posición indicada."""
        if not 0 <= posicion < len(self.ramas):
            raise IndexError("Esa posición no existe.")
        return self.ramas.pop(posicion)

    def info_arbol(self):
        """Devuelve información del árbol."""
        return f"Tronco: {self.tronco}, Ramas: {self.ramas}"


# 36. Crea la clase UsuarioBanco.
class UsuarioBanco:
    """Representa un usuario bancario con saldo y cuenta corriente."""

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Retira dinero del saldo del usuario."""
        self._validar_cantidad_positiva(cantidad)
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")

        self.saldo -= cantidad
        return f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}."

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero desde otro usuario hacia este usuario."""
        self._validar_cantidad_positiva(cantidad)
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")

        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        return (
            f"{otro_usuario.nombre} ha transferido {cantidad} a {self.nombre}. "
            f"Saldo actual de {self.nombre}: {self.saldo}."
        )

    def agregar_dinero(self, cantidad):
        """Añade dinero al saldo del usuario."""
        self._validar_cantidad_positiva(cantidad)
        self.saldo += cantidad
        return f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}."

    @staticmethod
    def _validar_cantidad_positiva(cantidad):
        """Valida que una cantidad sea mayor que cero."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")


# 37. Procesa un texto según la opción especificada.
def contar_palabras(texto):
    """Cuenta las palabras de un texto."""
    return len(texto.split())


def reemplazar_palabras(texto, palabra_antigua, palabra_nueva):
    """Reemplaza una palabra por otra dentro de un texto."""
    return texto.replace(palabra_antigua, palabra_nueva)


def eliminar_palabra(texto, palabra_a_eliminar):
    """Elimina una palabra de un texto."""
    texto = texto.replace(palabra_a_eliminar, "")
    return " ".join(texto.split())


def procesar_texto(texto, opcion, *args):
    """Procesa un texto usando la operación indicada."""
    if opcion == "contar_palabras":
        return contar_palabras(texto)
    if opcion == "reemplazar_palabras":
        return reemplazar_palabras(texto, *args)
    if opcion == "eliminar_palabra":
        return eliminar_palabra(texto, *args)
    raise ValueError("Opción no válida")


# 38. Indica si es de noche, de día o tarde según la hora.
def momento(hora):
    """Devuelve el momento del día según una hora entre 0 y 23."""
    if 6 <= hora < 12:
        return "Es de día."
    if 12 <= hora < 18:
        return "Es de tarde."
    if 18 <= hora < 24 or 0 <= hora < 6:
        return "Es de noche."
    return "Hora no válida. Por favor, ingrese una hora entre 0 y 23."


# 39. Determina la calificación en texto según una nota numérica.
def calificacion_texto(nota):
    """Convierte una nota numérica en una calificación textual."""
    if 0 <= nota <= 69:
        return "Insuficiente"
    if 70 <= nota <= 79:
        return "Bien"
    if 80 <= nota <= 89:
        return "Muy bien"
    if 90 <= nota <= 100:
        return "Excelente"
    return "Nota no válida. Por favor, ingrese una nota entre 0 y 100."


# 40. Calcula el área de una figura.
def area(figura, datos):
    """Calcula el área de un rectángulo, círculo o triángulo."""
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    if figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    if figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    raise ValueError("Figura no válida. Use 'rectangulo', 'circulo' o 'triangulo'.")


# 41. Calcula el precio final de una compra aplicando un cupón opcional.
def calcular_precio_final(precio_original, tiene_cupon, descuento=0):
    """Calcula el precio final después de aplicar un cupón válido."""
    if precio_original < 0:
        raise ValueError("El precio original no puede ser negativo.")

    tiene_cupon = tiene_cupon.lower().strip()
    if tiene_cupon in ("sí", "si"):
        if descuento <= 0:
            return precio_original
        return max(precio_original - descuento, 0)

    if tiene_cupon == "no":
        return precio_original

    return precio_original


def ejecutar_ejercicio_41():
    """Ejecuta el programa interactivo del ejercicio 41."""
    precio_original = float(input("Introduce el precio original del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? sí/no: ").lower()
    descuento = 0

    if tiene_cupon in ("sí", "si"):
        descuento = float(input("Introduce el valor del cupón de descuento: "))

    precio_final = calcular_precio_final(precio_original, tiene_cupon, descuento)
    print(f"El precio final de la compra es: {precio_final} €")

"Comprobación de los ejercicios con assert y ejemplos de uso. No se ejecutan los ejercicios interactivos automáticamente."
def ejecutar_pruebas():
    """Ejecuta pruebas básicas con assert."""
    assert frecuencia_letras("Hola") == {"a": 1, "h": 1, "l": 1, "o": 1}
    assert doblar_valores([1, 2, 3]) == [2, 4, 6]
    assert filtrar_palabras(["hola", "adiós", "casa"], "o") == ["hola"]
    assert diferencia([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert estado_calificacion([6, 7, 8]) == "aprobado"
    assert factorial(5) == 120
    assert tuplas_strings([(1, "a"), (True, None)]) == ["1 a", "True None"]
    assert dividir_texto("10", "2") == 5
    assert dividir_texto("10", "0") == "Error: no se puede dividir entre cero."
    assert excluir_mascotas(["Perro", "Cocodrilo"]) == ["Perro"]
    assert promedio_con_error([1, 2, 3, 4, 5]) == 3
    assert validar_edad(25) == "Edad válida: 25 años"
    assert longitud_palabras(["hola", "adiós"]) == [4, 5]
    assert filtrar_por_letra(["hola", "adiós"], "h") == ["hola"]
    assert suma_3([1, 2, 3]) == [4, 5, 6]
    assert filtrar_longitud(["hola", "adiós", "sol"], 4) == ["adiós"]
    assert digitos_a_numero([1, 2, 3, 4, 5]) == 12345
    assert filtrar_estudiantes([("Juan", 85), ("Ana", 95)]) == [("Ana", 95)]
    assert impares([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert filtrar_enteros([1, 2.5, True, 3, False]) == [1, 3]
    assert cubo(3) == 27
    assert producto_total([1, 2, 3, 4]) == 24
    assert concatenar(["Hola", "mundo"]) == "Hola mundo"
    assert diferencia_total([10, 2, 3]) == 5
    assert contar_caracteres("Hola") == 4
    assert resto_division(10, 3) == 1
    assert promedio_simple([1, 2, 3, 4, 5]) == 3
    assert duplicado([1, 2, 3, 2]) == 2
    assert enmascarar_variable("1234567890") == "######7890"
    assert anagramas("amor", "Roma") is True
    assert buscar_empleado(
        "Juan Pérez",
        [{"nombre_completo": "Juan Pérez", "puesto": "Gerente"}],
    ) == "Juan Pérez trabaja como Gerente."
    assert sumar_listas([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

    arbol = Arbol(1)
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    assert arbol.info_arbol() == "Tronco: 2, Ramas: [2, 1]"

    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    alicia.transferir_dinero(bob, 60)
    alicia.retirar_dinero(50)
    assert alicia.saldo == 110
    assert bob.saldo == 10

    texto = "Python es fácil y Python es útil"
    assert procesar_texto(texto, "contar_palabras") == 7
    assert procesar_texto(texto, "reemplazar_palabras", "Python", "Java") == "Java es fácil y Java es útil"
    assert procesar_texto(texto, "eliminar_palabra", "fácil") == "Python es y Python es útil"
    assert momento(10) == "Es de día."
    assert calificacion_texto(85) == "Muy bien"
    assert area("rectangulo", (5, 10)) == 50
    assert calcular_precio_final(100, "sí", 15) == 85


def mostrar_ejemplos():
    """Muestra ejemplos de uso sin ejecutar ejercicios interactivos."""
    print(frecuencia_letras("Hola, ¿cómo estás?"))
    print(doblar_valores([1, 2, 3, 4, 5]))
    print(filtrar_palabras(["hola", "adiós", "cómo", "estás"], "o"))
    print(diferencia([1, 2, 3], [4, 5, 6]))
    print(estado_calificacion([6, 7, 8, 9, 10]))
    print(factorial(5))
    print(tuplas_strings([(40.4168, -3.7038), ("hola", "mundo"), ("Madrid", 2026)]))
    print(dividir_texto("10", "2"))
    print(excluir_mascotas(["Perro", "Gato", "Conejo", "Loro", "Cocodrilo"]))
    print(promedio_con_error([1, 2, 3, 4, 5]))
    print(validar_edad(25))
    print(longitud_palabras(["hola", "adiós", "cómo", "estás"]))
    print(mayus_minus_tuplas(["hola", "adiós", "cómo", "estás", "hola"]))
    print(filtrar_por_letra(["hola", "adiós", "cómo", "estás"], "h"))
    print(suma_3([1, 2, 3, 4, 5]))
    print(filtrar_longitud(["hola", "adiós", "cómo", "estás"], 4))
    print(digitos_a_numero([1, 2, 3, 4, 5]))
    print(filtrar_estudiantes([("Juan", 85), ("María", 92), ("Pedro", 78), ("Ana", 95)]))
    print(impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(filtrar_enteros([1, 2.5, "hola", True, 3, False, 4.0, 5]))
    print(cubo(3))
    print(producto_total([1, 2, 3, 4, 5]))
    print(concatenar(["Hola", "mundo", "¿", "cómo", "estás", "?"]))
    print(diferencia_total([10, 2, 3, 4]))
    print(contar_caracteres("Hola, ¿cómo estás?"))
    print(resto_division(10, 3))
    print(promedio_simple([1, 2, 3, 4, 5]))
    print(duplicado([1, 2, 3, 4, 5, 3, 6]))
    print(enmascarar_variable("1234567890"))
    print(anagramas("amor", "Roma"))
    print(buscar_empleado("Juan Pérez", [{"nombre_completo": "Juan Pérez", "puesto": "Gerente"}]))
    print(sumar_listas([1, 2, 3], [4, 5, 6]))

    arbol = Arbol(1)
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print(arbol.info_arbol())

    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    print(bob.agregar_dinero(20))
    print(alicia.transferir_dinero(bob, 60))
    print(alicia.retirar_dinero(50))
    print(f"Saldo final de Alicia: {alicia.saldo}")
    print(f"Saldo final de Bob: {bob.saldo}")

    texto = "Python es fácil y Python es útil"
    print(procesar_texto(texto, "contar_palabras"))
    print(procesar_texto(texto, "reemplazar_palabras", "Python", "Java"))
    print(procesar_texto(texto, "eliminar_palabra", "fácil"))
    print(momento(10))
    print(calificacion_texto(85))
    print(area("rectangulo", (5, 10)))
    print(calcular_precio_final(100, "sí", 15))


if __name__ == "__main__":
    ejecutar_pruebas()
    mostrar_ejemplos()

    # Ejercicios interactivos, quitar el comentario para ejecutar:
    # buscar_nombre()
    # ejecutar_ejercicio_41()
