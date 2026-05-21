Explicación del Proyecto: Análisis de una Videoteca con Python

Objetivo del proyecto

El propósito de este proyecto es trabajar con estructuras de datos en Python, específicamente listas de listas (matrices), para analizar información de películas o series.
En concreto, se busca:
Contar cuántos títulos cumplen dos condiciones:
  A.	Tener una calificación mayor o igual a un valor dado
  B.	Haber sido estrenados a partir de un año específico

1. Estructura de la Videoteca
Se construye una matriz llamada Videoteca, donde cada fila representa un título con la siguiente información:
  •	Título
  •	Año de lanzamiento
  •	Calificación
  •	Género

["Matrix", 1999, 8.7, "Ciencia Ficción"]

Esta estructura permite organizar múltiples datos de forma eficiente y facilita su recorrido mediante ciclos.

2. Función Principal: contar_titulos
Se define una función que permite realizar el análisis de la videoteca:
def contar_titulos(videoteca, umbral_calificacion, año_limite):

Parámetros:
  •	videoteca: la matriz con la información de películas y series.
  •	umbral_calificacion: valor mínimo de calificación requerido.
  •	año_limite: año mínimo de lanzamiento.

Proceso:
  •	Se recorre cada fila de la matriz usando un ciclo for.
  •	Se extraen los datos de cada registro.
  •	Se evalúan dos condiciones: 
    1.	Que la calificación sea mayor o igual al umbral.
    2.	Que el año sea mayor o igual al límite establecido.
Si ambas condiciones se cumplen, el título se agrega a una lista.

Resultado:
La función retorna:
  •	La cantidad de títulos que cumplen las condiciones.
  •	Una lista con los nombres de esos títulos.

3. Visualización de la Videoteca
Antes del análisis, el programa imprime todos los registros usando un ciclo for, lo que permite verificar el contenido de la matriz.

for titulo, año, calificacion, genero in Videoteca:

Esto facilita la comprensión de los datos disponibles al usuario.

4. Entrada de Datos
El programa solicita al usuario ingresar:
  •	Un valor para calificación mínima (float)
  •	Un valor para año mínimo (int)
Se utiliza un bloque try-except para evitar errores si el usuario introduce datos incorrectos:

try:
    ...
except ValueError:

Esto mejora la robustez del programa al manejar entradas inválidas.

5. Procesamiento y Resultados
Una vez obtenidos los datos, se llama a la función:
cantidad, titulos_cumplen = contar_titulos(...)
Luego se muestra:
  •	El número total de títulos que cumplen los criterios.
  •	La lista de títulos (si existen).
Si no hay coincidencias, se muestra un mensaje indicando que no se encontraron resultados.

6. Uso de Condicionales
Se utiliza una estructura if-else para decidir qué mostrar:
  •	Si hay resultados → se listan los títulos.
  •	Si no hay resultados → se muestra un mensaje informativo.

7. Importancia del Proyecto
Este ejercicio permite aplicar conceptos clave de programación en Python:
  •	Manejo de listas y matrices
  •	Uso de funciones
  •	Estructuras de control (for, if)
  •	Validación de datos con try-except
  •	Interacción con el usuario (input)

8. Conclusión
El programa desarrollado permite filtrar y analizar una colección de películas y series de manera eficiente, basándose en criterios definidos por el usuario. Es un ejemplo práctico de cómo estructurar datos y aplicar lógica de programación para obtener información relevante.

