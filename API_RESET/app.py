import os
import sqlite3

from flask import Flask, jsonify, request


app = Flask(__name__)

CARPETA_DEL_PROGRAMA = os.path.dirname(os.path.abspath(__file__))
BASE_DE_DATOS = os.path.join(CARPETA_DEL_PROGRAMA, "biblioteca.db")


class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def a_diccionario(self):
        return {
            "id": self.id_autor,
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad,
        }


class Libro:
    def __init__(self, id_libro, titulo, anio, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio = anio
        self.autor = autor

    def a_diccionario(self):
        return {
            "id": self.id_libro,
            "titulo": self.titulo,
            "anio": self.anio,
            "autor": self.autor.a_diccionario(),
        }


def obtener_conexion():
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def inicializar_base_de_datos():
    conexion = obtener_conexion()

    conexion.execute(
        """
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT NOT NULL
        )
        """
    )

    conexion.execute(
        """
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio INTEGER NOT NULL,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
        """
    )

    conexion.commit()
    conexion.close()


def obtener_autores_db():
    conexion = obtener_conexion()
    filas = conexion.execute("SELECT * FROM autores ORDER BY id").fetchall()
    conexion.close()

    autores = []
    for fila in filas:
        autor = Autor(fila["id"], fila["nombre"], fila["nacionalidad"])
        autores.append(autor.a_diccionario())
    return autores


def obtener_autor_db(id_autor):
    conexion = obtener_conexion()
    fila = conexion.execute(
        "SELECT * FROM autores WHERE id = ?", (id_autor,)
    ).fetchone()
    conexion.close()

    if fila is None:
        return None

    autor = Autor(fila["id"], fila["nombre"], fila["nacionalidad"])
    return autor.a_diccionario()


def insertar_autor_db(nombre, nacionalidad):
    conexion = obtener_conexion()
    cursor = conexion.execute(
        "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
        (nombre, nacionalidad),
    )
    id_autor = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return id_autor


def crear_libro_desde_fila(fila):
    autor = Autor(
        fila["autor_id"],
        fila["autor_nombre"],
        fila["autor_nacionalidad"],
    )
    return Libro(fila["id"], fila["titulo"], fila["anio"], autor)


def obtener_libros_db():
    conexion = obtener_conexion()
    filas = conexion.execute(
        """
        SELECT libros.id, libros.titulo, libros.anio,
               autores.id AS autor_id,
               autores.nombre AS autor_nombre,
               autores.nacionalidad AS autor_nacionalidad
        FROM libros
        INNER JOIN autores ON libros.autor_id = autores.id
        ORDER BY libros.id
        """
    ).fetchall()
    conexion.close()

    libros = []
    for fila in filas:
        libros.append(crear_libro_desde_fila(fila).a_diccionario())
    return libros


def obtener_libro_db(id_libro):
    conexion = obtener_conexion()
    fila = conexion.execute(
        """
        SELECT libros.id, libros.titulo, libros.anio,
               autores.id AS autor_id,
               autores.nombre AS autor_nombre,
               autores.nacionalidad AS autor_nacionalidad
        FROM libros
        INNER JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
        """,
        (id_libro,),
    ).fetchone()
    conexion.close()

    if fila is None:
        return None

    return crear_libro_desde_fila(fila).a_diccionario()


def insertar_libro_db(titulo, anio, autor_id):
    conexion = obtener_conexion()
    cursor = conexion.execute(
        "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
        (titulo, anio, autor_id),
    )
    id_libro = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return id_libro


def actualizar_libro_db(id_libro, titulo, anio, autor_id):
    conexion = obtener_conexion()
    cursor = conexion.execute(
        """
        UPDATE libros
        SET titulo = ?, anio = ?, autor_id = ?
        WHERE id = ?
        """,
        (titulo, anio, autor_id, id_libro),
    )
    conexion.commit()
    filas_modificadas = cursor.rowcount
    conexion.close()
    return filas_modificadas


def eliminar_libro_db(id_libro):
    conexion = obtener_conexion()
    cursor = conexion.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    filas_eliminadas = cursor.rowcount
    conexion.close()
    return filas_eliminadas


@app.get("/api/autores")
def listar_autores():
    return jsonify(obtener_autores_db()), 200


@app.get("/api/autores/<int:id_autor>")
def buscar_autor(id_autor):
    autor = obtener_autor_db(id_autor)

    if autor is None:
        return jsonify({"error": "Autor no encontrado"}), 404

    return jsonify(autor), 200


@app.post("/api/autores")
def crear_autor():
    datos = request.get_json(silent=True)

    if datos is None or "nombre" not in datos or "nacionalidad" not in datos:
        return jsonify({"error": "Faltan nombre o nacionalidad"}), 400

    if not isinstance(datos["nombre"], str) or not isinstance(
        datos["nacionalidad"], str
    ):
        return jsonify({"error": "Nombre y nacionalidad deben ser textos"}), 400

    if datos["nombre"].strip() == "" or datos["nacionalidad"].strip() == "":
        return jsonify({"error": "Los campos no pueden estar vacios"}), 400

    id_autor = insertar_autor_db(
        datos["nombre"].strip(), datos["nacionalidad"].strip()
    )
    return jsonify(obtener_autor_db(id_autor)), 201


@app.get("/api/libros")
def listar_libros():
    return jsonify(obtener_libros_db()), 200


@app.get("/api/libros/<int:id_libro>")
def buscar_libro(id_libro):
    libro = obtener_libro_db(id_libro)

    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    return jsonify(libro), 200


@app.post("/api/libros")
def crear_libro():
    datos = request.get_json(silent=True)
    campos_obligatorios = ["titulo", "anio", "autor_id"]

    if datos is None or not all(campo in datos for campo in campos_obligatorios):
        return jsonify({"error": "Faltan titulo, anio o autor_id"}), 400

    if not isinstance(datos["titulo"], str) or datos["titulo"].strip() == "":
        return jsonify({"error": "El titulo debe ser un texto no vacio"}), 400

    if not isinstance(datos["anio"], int) or not isinstance(datos["autor_id"], int):
        return jsonify({"error": "Anio y autor_id deben ser numeros enteros"}), 400

    if obtener_autor_db(datos["autor_id"]) is None:
        return jsonify({"error": "Autor no encontrado"}), 404

    id_libro = insertar_libro_db(
        datos["titulo"].strip(), datos["anio"], datos["autor_id"]
    )
    return jsonify(obtener_libro_db(id_libro)), 201


@app.put("/api/libros/<int:id_libro>")
def actualizar_libro(id_libro):
    libro_actual = obtener_libro_db(id_libro)

    if libro_actual is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    datos = request.get_json(silent=True)
    if datos is None:
        return jsonify({"error": "Se debe enviar un cuerpo JSON"}), 400

    campos_validos = {"titulo", "anio", "autor_id"}
    if not any(campo in datos for campo in campos_validos):
        return jsonify({"error": "No se envio ningun campo para modificar"}), 400

    titulo = datos.get("titulo", libro_actual["titulo"])
    anio = datos.get("anio", libro_actual["anio"])
    autor_id = datos.get("autor_id", libro_actual["autor"]["id"])

    if not isinstance(titulo, str) or titulo.strip() == "":
        return jsonify({"error": "El titulo debe ser un texto no vacio"}), 400

    if not isinstance(anio, int) or not isinstance(autor_id, int):
        return jsonify({"error": "Anio y autor_id deben ser numeros enteros"}), 400

    if obtener_autor_db(autor_id) is None:
        return jsonify({"error": "Autor no encontrado"}), 404

    actualizar_libro_db(id_libro, titulo.strip(), anio, autor_id)
    return jsonify(obtener_libro_db(id_libro)), 200


@app.delete("/api/libros/<int:id_libro>")
def eliminar_libro(id_libro):
    if obtener_libro_db(id_libro) is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    eliminar_libro_db(id_libro)
    return jsonify({"mensaje": "Libro eliminado correctamente", "id": id_libro}), 200


inicializar_base_de_datos()


if __name__ == "__main__":
    print("API disponible en http://127.0.0.1:5000")
    app.run(debug=True)
