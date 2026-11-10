from conectar import conectar


def actualizar_titulo_libro(id_libro, nuevo_titulo):
    """Ejercicio 3: actualiza el título; devuelve False si el ID no existe."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE libros SET titulo = ? WHERE id = ?",
            (nuevo_titulo, id_libro),
        )
        actualizado = cursor.rowcount > 0
        conexion.commit()
        return actualizado
    finally:
        conexion.close()
