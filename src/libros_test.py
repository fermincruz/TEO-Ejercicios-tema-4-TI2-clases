import libros

def test_lee_libros():
    print("Test de lee_libros")
    datos = libros.lee_libros("data/libreria.csv")
    print(f"Se han leído {len(datos)} libros.")
    print("="*20)
    print()
    return datos

def test_libro_mas_reciente(datos):
    print("Test de libro_mas_reciente")
    print("\nLibro más reciente de Gabriel García Márquez:", libros.libro_mas_reciente(datos, "Gabriel García Márquez"))
    print("="*20)
    print()

def test_libro_titulo_mas_corto(datos):
    print("Test de libro_titulo_mas_corto")
    print("El libro con el título más corto de todos es:", libros.libro_titulo_mas_corto(datos))
    print("El libro con el título más corto de todos es de Gabriel García Márquez:", libros.libro_titulo_mas_corto(datos, "Gabriel García Márquez"))
    print("="*20)
    print()

def test_libros_mas_caros(datos):
    print("Test de libros_mas_caros")
    print("Los libros más caros de todos son:")
    for libro in libros.libros_mas_caros(datos):
        print("\t", libro)
    print("\nLos libros más caros del año 1985 son:")
    for libro in libros.libros_mas_caros(datos, 1985):
        print("\t", libro)
    print("="*20)
    print()

def test_ordena_libros_por_año_y_autor(datos):
    print("Test de test_ordena_libros_por_año_y_autor")
    print("Los libros ordenados por año, y a igualdad de año, por autor:")
    for libro in libros.ordena_libros_por_año_y_autor(datos):
        print("\t", libro)
    print("="*20)
    print()

def test_crea_diccionario_iniciales(datos):
    print("Test de crea_diccionario_iniciales")
    diccionario = libros.crea_diccionario_iniciales(datos)
    for autor, libros_autor in sorted(diccionario.items()):
        print("Letra:", autor)
        for libro in libros_autor:
            print("\t", libro)
        print()
    print("="*20)
    print()

def test_crea_diccionario_mas_barato_por_mes(datos):
    print("Test de crea_diccionario_mas_barato_por_mes(libros)")
    diccionario = libros.crea_diccionario_mas_barato_por_mes(datos)
    for mes, libro in sorted(diccionario.items()):
        print(f"{mes}: {libro}")
    print("="*20)
    print()

def mostrar_diccionario_listas_comprimido(diccionario):
    print(f"{'clave':<{30}} valor")
    print(f"{'(mes)':<{30}} (List[Libro])")
    print("="*100)
    for clave, valor in diccionario.items():
        print(f"{clave:<{30}} {str_lista_comprimida(valor)}")
        print("-"*100)

def str_lista_comprimida(lista):
    res = "["
    for elemento in lista:
        res += f"Libro(titulo='{elemento.titulo}', fecha_publicacion={elemento.fecha_publicacion}, precio={elemento.precio},...),\n"+" "*31
    return res[:-33] + "]"

def test_agrupa_libros_por_mes(datos):
    print("Test de agrupa_libros_por_mes")
    mostrar_diccionario_listas_comprimido(libros.agrupa_libros_por_mes(datos))

if __name__ == "__main__":
    datos = test_lee_libros()
    #test_libro_mas_reciente(datos)
    #test_libro_titulo_mas_corto(datos)
    #test_libros_mas_caros(datos)
    #test_ordena_libros_por_año_y_autor(datos)
    #test_crea_diccionario_iniciales(datos)
    #test_agrupa_libros_por_mes(datos)
    #test_crea_diccionario_mas_barato_por_mes(datos)