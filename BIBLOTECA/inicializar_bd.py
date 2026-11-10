from conectar import conectar


def inicializar_bd():
    """Ejercicio 2: crea biblioteca.db y sus tablas si no existen."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                nacionalidad TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                anio INTEGER,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES autores(id)
            )
        """)
        conexion.commit()
    finally:
        conexion.close()


if __name__ == "__main__":
    inicializar_bd()
    print("Base de datos biblioteca.db inicializada.")
