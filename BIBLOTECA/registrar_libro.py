from conectar import conectar


def registrar_libro(titulo, anio, autor_id):
    """Ejercicio 3: inserta un libro de un autor existente y retorna su ID."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
            (titulo, anio, autor_id),
        )
        id_libro = cursor.lastrowid
        conexion.commit()
        return id_libro
    finally:
        conexion.close()
