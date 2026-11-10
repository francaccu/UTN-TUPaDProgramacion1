from autor import Autor
from conectar import conectar


def listar_autores():
    """Devuelve todos los autores registrados, ordenados por ID."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, nacionalidad FROM autores ORDER BY id"
        )
        filas = cursor.fetchall()
    finally:
        conexion.close()

    return [Autor(id_autor, nombre, nacionalidad) for id_autor, nombre, nacionalidad in filas]
