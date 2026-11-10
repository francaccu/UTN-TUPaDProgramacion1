"""
Trabajo práctico: Sistema de Gestión de Biblioteca (POO + SQLite).

Las clases y funciones están definidas en archivos independientes.
Este archivo las importa y ejecuta la prueba integral del ejercicio 4.

Base teórica: Guia_acceso_datos_Python.pdf:
  - Secciones 1 y 2, página 1: sqlite3, conexión, cursor y tablas.
  - Sección 3, páginas 2 y 3: INSERT, SELECT, UPDATE y DELETE.
  - Sección 4, página 3: manejo y cierre de conexiones.
El modelado POO, la clave foránea y el JOIN completan las consignas
del archivo tp_grupal_accesodatos.pdf, ejercicios 1 a 4.
"""

from actualizar_titulo_libro import actualizar_titulo_libro
from autor import Autor
from eliminar_libro import eliminar_libro
from inicializar_bd import inicializar_bd
from libro import Libro
from listar_libros import listar_libros
from registrar_autor import registrar_autor
from registrar_libro import registrar_libro


if __name__ == "__main__":
    # Paso 1: crear el esquema sin borrar datos existentes.
    inicializar_bd()
    print("1. Base de datos inicializada.")

    # Paso 2: registrar dos autores y tres libros.
    autor_1 = Autor(
        registrar_autor("Jorge Luis Borges", "Argentina"),
        "Jorge Luis Borges",
        "Argentina",
    )
    autor_2 = Autor(
        registrar_autor("Julio Cortázar", "Argentina"),
        "Julio Cortázar",
        "Argentina",
    )
    libro_1 = Libro(
        registrar_libro("Ficciones", 1944, autor_1.id_autor),
        "Ficciones", 1944, autor_1,
    )
    libro_2 = Libro(
        registrar_libro("El Aleph", 1949, autor_1.id_autor),
        "El Aleph", 1949, autor_1,
    )
    libro_3 = Libro(
        registrar_libro("Rayuela", 1963, autor_2.id_autor),
        "Rayuela", 1963, autor_2,
    )
    print("\n2. Se registraron estos autores y tres libros:")
    print(autor_1)
    print(autor_2)

    # Paso 3: leer la base con JOIN y mostrar título, año y autor.
    print("\n3. Listado completo:")
    for libro in listar_libros():
        print(libro)

    # Paso 4: actualizar y volver a consultar para verificar persistencia.
    nuevo_titulo = "Ficciones (título actualizado)"
    if not actualizar_titulo_libro(libro_1.id_libro, nuevo_titulo):
        raise RuntimeError("No se encontró el libro que se debía actualizar.")

    libros_actualizados = listar_libros()
    cambio_verificado = False
    print("\n4. Listado después de actualizar el título:")
    for libro in libros_actualizados:
        print(libro)
        if libro.id_libro == libro_1.id_libro and libro.titulo == nuevo_titulo:
            cambio_verificado = True
    if not cambio_verificado:
        raise RuntimeError("La consulta no devolvió el título actualizado.")
    print("Verificación: el nuevo título quedó guardado en la base.")

    # Paso 5: eliminar el tercer libro y comprobar el listado resultante.
    if not eliminar_libro(libro_3.id_libro):
        raise RuntimeError("No se encontró el libro que se debía eliminar.")

    print("\n5. Listado después de eliminar Rayuela:")
    libros_restantes = listar_libros()
    for libro in libros_restantes:
        print(libro)
        if libro.id_libro == libro_3.id_libro:
            raise RuntimeError("El libro eliminado todavía aparece en la base.")
    print("Verificación: el libro eliminado ya no aparece en la base.")
    print("\nPrueba integral completada correctamente.")
