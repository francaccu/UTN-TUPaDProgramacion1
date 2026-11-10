from conectar import conectar


def registrar_autor(nombre, nacionalidad):
    """Ejercicio 3: inserta un autor y devuelve su ID generado."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
            (nombre, nacionalidad),
        )
        id_autor = cursor.lastrowid
        conexion.commit()
        return id_autor
    finally:
        conexion.close()
