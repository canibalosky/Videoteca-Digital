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
# y devuelve el conteo de títulos que cumplen ambas condiciones, además de sus nombres.
def contar_titulos(videoteca, umbral_calificacion, año_limite):
    titulos_cumplen = []
    for fila in videoteca:
        titulo, año, calificacion, genero = fila
        if calificacion >= umbral_calificacion and año >= año_limite:
            titulos_cumplen.append(titulo)
    return len(titulos_cumplen), titulos_cumplen
#Mostrar la videoteca para verificar su contenido:
print("Videoteca Disponible: ")
print()
#con el ciclo for se muestra cada título, año, calificación y género de la videoteca:
for titulo, año, calificacion, genero in Videoteca:
    print(f"Título: {titulo}, Año: {año}, Calificación: {calificacion}, Género: {genero}")
#Entrada interactiva para el umbral de calificación y el año límite:
#try-except se usa para manejar posibles errores de entrada, como ingresar un 
#valor no numérico para la calificación o el año, lo que podría causar una excepción ValueError.
#Si el usuario ingresa un valor no válido, el programa muestra un mensaje y vuelve a pedir los datos.
while True:
    try:
        umbral_calificacion = float(input("\nDigite el número para la Calificación de la película o serie: "))
        print()
        año_limite = int(input("Digite el número para el Año de la película o serie: "))
        print()
        break
    except ValueError:
        print("Error: Por favor, ingrese un número válido para la calificación (decimal) y el año (sin puntos).")
        print("Intente de nuevo.\n")
        continue
#llamada a la función y muestra del resultado:
#cantidad almacena el número de títulos que cumplen ambas condiciones, mientras que titulos_cumplen es una lista 
#con los nombres de esos títulos.
#contar_titulos se llama con la videoteca, el umbral de calificación y el año límite para obtener el conteo 
#y los títulos que cumplen los criterios.
cantidad, titulos_cumplen = contar_titulos(Videoteca, umbral_calificacion, año_limite)
#Muestra del resultado:
print(f"El número de títulos con calificación >= {umbral_calificacion} y año >= {año_limite} es: {cantidad}")
print()
#if-else para mostrar los títulos que cumplen los criterios o un mensaje si no se encuentran títulos que cumplan ambos criterios:
#print(f"- {titulo}") se usa para mostrar cada título que cumple los criterios, con un guion al inicio para mejorar la legibilidad.
if cantidad > 0:
    print("Títulos que cumplen los criterios:")
    print()
    for titulo in titulos_cumplen:
        print(f"- {titulo}")
        print()
else:
    print()
    print("No se encontraron títulos que cumplan ambos criterios.")
    print()
