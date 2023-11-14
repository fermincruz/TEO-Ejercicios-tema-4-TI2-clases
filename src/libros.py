from collections import namedtuple, defaultdict
import csv
from datetime import datetime

Libro = namedtuple("Libro", "isbn,titulo,autor,fecha_publicacion,precio,disponible")

def lee_libros(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector:
            fecha_publicacion = datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
            precio = float(precio)
            disponible = disponible == "Sí"
            res.append(
                Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)
            )
        return res


# TODO: Implemente las funciones solicitadas en el enunciado
def libro_mas_reciente(libros, autor):
    filtrado = [libro for libro in libros if libro.autor == autor]
    '''
    O también:
    filtrado = []
    for libro in libros:
        if libro.autor == autor:
        filtrado.append(libro)
    '''
    if len(filtrado) == 0:
        return None
    
    return max(filtrado, key = lambda libro:libro.fecha_publicacion)

def libro_titulo_mas_corto(libros, autor = None):
    filtrado = [libro for libro in libros if autor == None or libro.autor == autor]
    if len(filtrado) == 0:
        return None
    
    return min(filtrado, key = lambda libro:len(libro.titulo))

def libros_mas_caros(libros, año=None):
    filtrado = [libro for libro in libros if año == None or libro.fecha_publicacion.year == año]
    filtrado.sort(key=lambda libro:libro.precio, reverse=True)
    return filtrado[:3]

def ordena_libros_por_año_y_autor(libros):
    # La función lambda devuelve para cada libro una tupla formada por año y autor
    # Así, al comparar estas tuplas la función sorted, primero ordenará por año,
    # pero a igualdad de año, ordenará por autor.
    return sorted(libros, key=lambda libro:(libro.fecha_publicacion.year, libro.autor))

def crea_diccionario_iniciales(libros):
    res = defaultdict(list)    # o también:   res = dict()
    for libro in libros:
        clave = libro.autor[0]
        res[clave].append(libro)  #Se supone que el valor asociado a la clave es una lista
    return res

def crea_diccionario_mas_barato_por_mes(libros):
    pass
