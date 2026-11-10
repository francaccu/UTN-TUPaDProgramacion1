from conectar import conectar


def eliminar_libro(id_libro):
    """Ejercicio 3: elimina el libro; devuelve False si el ID no existe."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
        eliminado = cursor.rowcount > 0
        conexion.commit()
        return eliminado
    finally:
        conexion.close()
