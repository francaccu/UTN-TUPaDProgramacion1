from autor import Autor
from conectar import conectar
from libro import Libro


def listar_libros():
    """Ejercicio 3: consulta con JOIN y devuelve objetos Libro con su Autor."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT libros.id, libros.titulo, libros.anio,
                   autores.id, autores.nombre, autores.nacionalidad
            FROM libros
            INNER JOIN autores ON libros.autor_id = autores.id
            ORDER BY libros.id
        """)
        filas = cursor.fetchall()
    finally:
        conexion.close()

    libros = []
    autores = {}
    for id_libro, titulo, anio, id_autor, nombre, nacionalidad in filas:
        # Los libros del mismo autor comparten el mismo objeto Autor.
        if id_autor not in autores:
            autores[id_autor] = Autor(id_autor, nombre, nacionalidad)
        libros.append(Libro(id_libro, titulo, anio, autores[id_autor]))
    return libros
