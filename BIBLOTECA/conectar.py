import sqlite3
from pathlib import Path


# El archivo se guarda junto al código, aunque se ejecute desde otra carpeta.
RUTA_BD = Path(__file__).resolve().parent / "biblioteca.db"


def conectar():
    """Abre la base y activa la comprobación de claves foráneas."""
    conexion = sqlite3.connect(RUTA_BD)
    try:
        # SQLite requiere activar esta comprobación en cada conexión.
        conexion.execute("PRAGMA foreign_keys = ON")
        return conexion
    except sqlite3.Error:
        conexion.close()
        raise
