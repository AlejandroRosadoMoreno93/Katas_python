# Práctica de Katas en Python

Este repositorio contiene una práctica de Python formada por una serie de ejercicios o *katas* orientados a reforzar conceptos básicos e intermedios del lenguaje.

El archivo principal de la práctica es:

```
proyecto_katas.py
```

## Objetivo de la práctica

El objetivo principal ha sido resolver distintos ejercicios de programación en Python aplicando:

- Funciones propias.
- Funciones `lambda`.
- Uso de `map()`, `filter()` y `reduce()`.
- Condicionales `if`, `elif` y `else`.
- Manejo de errores con `try`, `except` y excepciones personalizadas.
- Trabajo con listas, tuplas, cadenas de texto y diccionarios.
- Programación orientada a objetos mediante clases.
- Entrada de datos por teclado con `input()`.

## Estructura general del archivo

La práctica está organizada mediante ejercicios numerados. Cada ejercicio incluye una función, clase o bloque de código que resuelve un problema concreto.

Al inicio del archivo se importan los módulos necesarios:

```python
import unicodedata
from functools import reduce
from difflib import get_close_matches
```

Estos módulos se utilizan para:

- Normalizar texto y eliminar tildes.
- Aplicar operaciones acumulativas con `reduce()`.
- Buscar coincidencias aproximadas entre nombres.

## Pasos seguidos en la práctica

### 1. Tratamiento de texto

Se comenzó trabajando con cadenas de texto. Para ello se crearon funciones como:

- `quitar_tildes(texto)`: elimina tildes de un texto.
- `frecuencia_letras(texto)`: cuenta la frecuencia de cada letra ignorando espacios y signos.
- `contar_caracteres(cadena)`: devuelve el número de caracteres de una cadena.
- `anagramas(palabra1, palabra2)`: comprueba si dos palabras son anagramas.
- `enmascarar_variable(variable)`: convierte una variable en texto y oculta todos los caracteres excepto los últimos cuatro.

Estas funciones permiten practicar el uso de strings, métodos de texto, diccionarios y conversión de tipos.

### 2. Uso de `map()`

Después se resolvieron ejercicios usando `map()` para transformar elementos de listas.

Ejemplos incluidos:

- `doblar_valores(lista)`: devuelve el doble de cada valor.
- `diferencia(lista_a, lista_b)`: calcula la diferencia entre elementos de dos listas.
- `tuplas_strings(tuplas)`: convierte una lista de tuplas en una lista de strings.
- `longitud_palabras(palabras)`: devuelve la longitud de cada palabra.
- `suma_3(lista)`: suma 3 a cada número de una lista.
- `sumar_listas(lista1, lista2)`: suma los elementos correspondientes de dos listas.

### 3. Uso de `filter()`

También se practicó el filtrado de datos con `filter()` y funciones `lambda`.

Ejercicios destacados:

- `filtrar_palabras(palabras, fragmento)`: filtra palabras que contienen un fragmento concreto.
- `excluir_mascotas(mascotas)`: elimina de una lista ciertas mascotas prohibidas.
- `filtrar_por_letra(palabras, letra)`: filtra palabras que empiezan por una letra.
- `filtrar_longitud(palabras, n)`: filtra palabras con longitud mayor que un número dado.
- `filtrar_estudiantes(estudiantes)`: devuelve estudiantes con calificación igual o superior a 90.
- `impares(lista)`: devuelve solo los números impares.
- `filtrar_enteros(lista)`: devuelve solo valores enteros, excluyendo booleanos.

### 4. Uso de `reduce()`

Se aplicó `reduce()` para acumular valores de una lista y obtener un único resultado.

Funciones realizadas:

- `digitos_a_numero(digitos)`: convierte una lista de dígitos en un número.
- `producto_total(lista)`: calcula el producto total de una lista.
- `concatenar(palabras)`: concatena una lista de palabras.
- `diferencia_total(lista)`: calcula la diferencia acumulada de una lista.

### 5. Funciones matemáticas y validaciones

Se crearon varias funciones para practicar operaciones matemáticas y comprobaciones:

- `calificacion(notas)`: calcula la media de varias notas y devuelve si está aprobado o suspenso.
- `factorial(n)`: calcula el factorial de forma recursiva.
- `cubo(numero)`: devuelve el cubo de un número.
- `promedio(lista)`: calcula el promedio de una lista de números.
- `validar_edad(edad)`: comprueba que una edad sea un número entero válido entre 0 y 120.
- `area(figura, datos)`: calcula el área de un rectángulo, círculo o triángulo.

### 6. Manejo de errores

Se practicó el control de errores mediante excepciones.

Ejemplos trabajados:

- `dividir_texto(texto_a, texto_b)`: intenta convertir dos textos a número y dividirlos, controlando errores de conversión y división entre cero.
- `ListaVaciaError`: excepción personalizada para detectar listas vacías.
- Uso de `try` y `except` en operaciones bancarias para evitar que el programa muestre errores en rojo al usuario.

### 7. Búsqueda de datos

Se implementaron ejercicios relacionados con la búsqueda de información en listas o estructuras de datos.

Funciones incluidas:

- `duplicado(lista)`: busca el primer elemento duplicado de una lista.
- `buscar_nombre()`: solicita una lista de nombres y busca uno concreto. Si no aparece, puede sugerir una coincidencia aproximada.
- `buscar_empleado(nombre_completo, empleados)`: busca un empleado por nombre completo y devuelve su puesto.

### 8. Programación orientada a objetos

Se añadieron clases para practicar atributos, métodos y manipulación de objetos.

#### Clase `Arbol`

La clase `Arbol` representa un árbol genérico con un tronco y una lista de ramas.

Métodos implementados:

- `crecer_tronco()`
- `nueva_rama()`
- `crecer_ramas()`
- `quitar_rama(posicion)`
- `info_arbol()`

Pasos realizados con esta clase:

1. Crear un árbol.
2. Hacer crecer el tronco una unidad.
3. Añadir una nueva rama.
4. Hacer crecer todas las ramas.
5. Añadir dos nuevas ramas.
6. Retirar la rama situada en la posición 2.
7. Mostrar la información final del árbol.

#### Clase `UsuarioBanco`

La clase `UsuarioBanco` representa a un usuario de banco con nombre, saldo y cuenta corriente.

Métodos implementados:

- `retirar_dinero(cantidad)`
- `transferir_dinero(otro_usuario, cantidad)`
- `agregar_dinero(cantidad)`

Pasos realizados con esta clase:

1. Crear dos usuarios: Alicia y Bob.
2. Agregar dinero al saldo de Bob.
3. Transferir dinero desde Bob a Alicia.
4. Retirar dinero de Alicia.
5. Mostrar los saldos finales.

### 9. Procesamiento de texto mediante opciones

Se creó una función principal llamada `procesar_texto()` que ejecuta distintas operaciones según la opción indicada.

Funciones auxiliares:

- `contar_palabras(texto)`
- `reemplazar_palabras(texto, palabra_antigua, palabra_nueva)`
- `eliminar_palabra(texto, palabra_a_eliminar)`

La función `procesar_texto()` permite elegir entre esas opciones usando condicionales.

### 10. Condicionales y programas interactivos

En la parte final de la práctica se trabajaron ejercicios con condicionales.

Ejercicios incluidos:

- `momento(hora)`: indica si es de día, tarde o noche según la hora.
- `calificacion(nota)`: convierte una nota numérica en una calificación textual.
- Programa de descuento: solicita un precio original, pregunta si existe un cupón y calcula el precio final.

## Importante sobre la ejecución
Además, algunos ejercicios solicitan datos al usuario mediante `input()`, por ejemplo:

- El ejercicio de búsqueda de nombres.
- El ejercicio del cálculo del precio final con cupón de descuento.

Para ello, se han bloqueado con el objetivo de que el usuario final, al eliminar # pueda ejecutarlo

## Ejemplo de entrada para el ejercicio del cupón

```
Introduce el precio original del artículo: 100
¿Tienes un cupón de descuento? sí/no: sí
Introduce el valor del cupón de descuento: 15
```

Salida esperada:

```
El precio final de la compra es: 85.0 €
```

## Conceptos practicados

Con esta práctica se han reforzado los siguientes conceptos:

- Definición y llamada de funciones.
- Parámetros y valores de retorno.
- Funciones anónimas `lambda`.
- Transformación de datos con `map()`.
- Filtrado de datos con `filter()`.
- Acumulación de resultados con `reduce()`.
- Condicionales.
- Bucles.
- Listas, tuplas, diccionarios y conjuntos.
- Manejo de errores.
- Excepciones personalizadas.
- Clases, atributos y métodos.
- Entrada y salida de datos.

## Posibles mejoras

Como mejoras futuras, se podrían aplicar los siguientes cambios:

- Separar los ejercicios en varios archivos para organizar mejor el proyecto.
- Corregir la numeración, ya que en el archivo aparece el ejercicio 34 y después el 36.

## ALEJANDRO ROSADO

Práctica realizada como parte del aprendizaje de Python.
