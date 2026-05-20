Explicación del Proyecto: Análisis de una Videoteca con Python
Objetivo del proyecto
El propósito de este proyecto es trabajar con estructuras de datos en Python, específicamente listas de listas (matrices), para analizar información de películas o series.
En concreto, se busca:
Contar cuántos títulos cumplen dos condiciones:
1.	Tener una calificación mayor o igual a un valor dado
2.	Haber sido estrenados a partir de un año específico
Estructura de los datos
Se crea una matriz llamada Videoteca, donde cada fila representa una película o serie con la siguiente información:
Python
[Título, Año, Calificación, Género]
Mostrar más líneas
Ejemplo:
Python
["Matrix", 1999, 8.7, "Ciencia Ficción"]
Esto significa:
•	🎬 Título: Matrix
•	📅 Año: 1999
•	⭐ Calificación: 8.7
•	🎭 Género: Ciencia Ficción
En total, la matriz contiene 17 registros, lo que permite hacer un análisis básico.
Lógica del programa
El programa utiliza una función (módulo) llamada:
Python
contar_titulos(videoteca, umbral_calificacion, año_limite)
¿Qué hace esta función?
Recibe tres parámetros:
•	videoteca: la matriz con los datos
•	umbral_calificacion: el valor mínimo de calificación
•	año_limite: el año mínimo permitido
Proceso interno
1.	Se inicia un contador en 0:
Python
contador = 0
Mostrar más líneas
2.	Se recorre cada fila de la matriz:
Python
for fila in videoteca:
``
3.	Se extraen los datos de cada película:
Python
titulo, año, calificacion, genero = fila
``
4.	Se evalúan las condiciones:
Python
if calificacion >= umbral_calificacion and año >= año_limite:
5.	Si ambas se cumplen, se suma 1 al contador:
Python
contador += 1
6.	Finalmente, se retorna el total:
Python
return contador
Prueba del programa
Se definen los valores de prueba:
Python
umbral_calificacion = 7.4
año_limite = 1972
Mostrar más líneas
Luego, se llama a la función:
Python
resultado = contar_titulos(Videoteca, umbral_calificacion, año_limite)
Y se imprime el resultado:
Python
print(f"El número de títulos con calificación >= {umbral_calificacion} y año >= {año_limite} es: {resultado}")
Resultado obtenido
El resultado es:
El número de títulos con calificación >= 7.4 y año >= 1972 es: 17
¿Por qué?
•	Todas las películas tienen una calificación ≥ 7.4
•	Todas fueron estrenadas en 1972 o después
Por lo tanto, todas cumplen las condiciones.
Conceptos aplicados
Este proyecto permite practicar varios conceptos importantes:
•	Listas y listas anidadas (matrices)
•	Recorridos con for
•	Condicionales (if)
•	Funciones en Python
•	Contadores
•	Manipulación de datos
Conclusión
Este programa demuestra cómo analizar datos de manera sencilla usando Python.
A partir de una estructura básica, se puede filtrar información según criterios específicos, lo cual es una habilidad clave en programación y análisis de datos.

