# Ejercicios del tema 4: Funciones
---

Tenemos un fichero CSV con registros de libros en una librería (se muestra la primera línea del fichero):

```
978-3-16-148410-0, El Gran Gatsby, F. Scott Fitzgerald, 10/04/1925, 12.99, True
```

Las columnas son:

* ISBN (str): Identificador único de cada libro.
* Título (str): Título del libro.
* Autor (str): Nombre del autor del libro.
* Fecha de publicación (date): Fecha en la que fue publicado el libro.
* Precio (float): Precio de venta en euros.
* Disponible (bool): Indica si el libro está en stock.

Se dispone de la namedtuple ``Libro`` para representar esta información (puede ver la definición en el módulo ``libros.py``).

Implemente las siguientes funciones en ``libros.py``, haciendo uso de las funciones predefinidas ``max``, ``min`` y ``sorted`` cuando sea necesario. Puede probar cada función descomentando la llamada al método de test correspondiente en el módulo ``libros_test.py``:

* Función ``libro_mas_reciente``, que recibe una lista de libros y un autor y devuelve el libro con la fecha de publicación más reciente de dicho autor. Si no hay ningún libro del autor especificado, la función devuelve ``None``.

* Función ``libro_titulo_mas_corto``, que recibe una lista de libros y un autor (con valor por defecto ``None``), y devuelve el libro con el título más corto de entre los del autor. Si no hay ningún libro del autor especificado, la función devuelve ``None``. Si el valor del parámetro autor es ``None``, la función devuelve el libro con el título más corto de entre todos los libros de la lista.

* Función ``libros_mas_caros``, que recibe una lista de libros y un año y devuelve los 3 libros más caros de dicho año. Si hubiera menos de 3 libros del año especificado, la función devuelve los que hubiese. Si el valor del parámetro año es ``None``, la función devuelve los 3 libros más caros entre todos los libros de la lista.

* Función ``ordena_libros_por_año_y_autor``, que recibe una lista de libros y la devuelve ordenada por año, y a igualdad de año, por autor.

* Función ``crea_diccionario_iniciales``, que recibe una lista de libros y devuelve un diccionario en el que las claves son las iniciales de los autores y los valores son las listas de libros correspondientes de los autores coorrespondientes a cada inicial.

* Función ``crea_diccionario_mas_barato_por_mes``, que recibe una lista de libros y devuelve un diccionario en el que se asocia cada mes del año con el libro más barato de los publicados en dicho mes. Impleméntalo primero usando enteros para los meses, y luego sustituyendo los números por cadenas de texto con los nombres de los meses.


