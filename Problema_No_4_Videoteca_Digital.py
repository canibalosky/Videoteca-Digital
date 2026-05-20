#----------------------------------------------
#Nombre del estudiante: Wilson Hernández
#Grupo: 213022_900
#Programa: Ingeniería de Telecomunicaciones
#----------------------------------------------
#Se debe trabajar con una matriz con información de peliculas o series.
#Cada fila contiene [Título, Año, Calificación, Género]
#Se requiere contar los títulos que cumplan dos condiciones:
#1. Calificación >= umbral dado.
#2. Año >= año límite.
#Diseño de la matriz, donde se crea una lista de listas con al menos 7 registros:
#Matriz.
Videoteca = [
    ["El Padrino", 1972, 9.2, "Drama"],
    ["El Señor de los Anillos", 2001, 8.8, "Fantasía"],
    ["Matrix", 1999, 8.7, "Ciencia Ficción"],
    ["Parasite", 2019, 8.6, "Drama"],
    ["Inception", 2010, 8.8, "Ciencia Ficción"],
    ["The Dark Knight", 2008, 9.0, "Acción"],
    ["Pulp Fiction", 1994, 8.9, "Crimen"],
    ["Roma", 2018, 7.7, "Drama"],
    ["Amores Perros", 2000, 8.1, "Drama"],
    ["El Secreto de Sus Ojos", 2009, 8.2, "Drama"],
    ["Y tu mamá también", 2001, 7.6, "Drama"],
    ["Ciudad de Dios", 2002, 8.6, "Crimen"],
    ["El Laberinto del Fauno", 2006, 8.2, "Fantasía"],
    ["La Casa de Papel", 2017, 8.3, "Crimen"],
    ["Narcos", 2015, 8.8, "Crimen"],
    ["Élite", 2018, 7.4, "Drama"],
    ["Relatos Salvajes", 2014, 7.6, "Comedia Negra"]
]
#Definición de la función (módulo) para contar títulos que cumplen las condiciones:
#Se crea una función que recibe la matriz, el umbral de calificación y el año límite como parámetros, 
# y devuelve el conteo de títulos que cumplen ambas condiciones.
def contar_titulos(videoteca, umbral_calificacion, año_limite):
    contador = 0
    for fila in videoteca:
        titulo, año, calificacion, genero = fila
        if calificacion >= umbral_calificacion and año >= año_limite:
            contador += 1
    return contador
#Definición de los valores de prueba:
umbral_calificacion = 7.4
año_limite = 1972
#llamada a la función y muestra del resultado:
resultado = contar_titulos(Videoteca, umbral_calificacion, año_limite)
#Muestra del resultado:
print(f"El número de títulos con calificación >= {umbral_calificacion} y año >= {año_limite} es: {resultado}")
