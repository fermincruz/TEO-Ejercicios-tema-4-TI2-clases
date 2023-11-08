from collections import namedtuple
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
    pass

def libro_titulo_mas_corto(libros, autor = None):
    pass

def libros_mas_caros(libros, año=None):
    pass

def ordena_libros_por_año_y_autor(libros):
    pass

def crea_diccionario_iniciales(libros):
   pass

def crea_diccionario_mas_barato_por_mes(libros):
    pass
