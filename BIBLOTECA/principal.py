from actualizar_titulo_libro import actualizar_titulo_libro
from autor import Autor
from eliminar_libro import eliminar_libro
from inicializar_bd import inicializar_bd
from libro import Libro
from listar_autores import listar_autores
from listar_libros import listar_libros
from registrar_autor import registrar_autor
from registrar_libro import registrar_libro


def pedir_texto(mensaje):
    """Solicita un texto y no permite que quede vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El dato no puede estar vacío.")


def pedir_entero(mensaje):
    """Solicita un número entero hasta que el usuario ingrese uno válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")


def mostrar_autores():
    autores = listar_autores()
    if not autores:
        print("No hay autores registrados.")
        return []

    print("\nAutores registrados:")
    for autor in autores:
        print(f"ID: {autor.id_autor} | {autor}")
    return autores


def mostrar_libros():
    libros = listar_libros()
    if not libros:
        print("No hay libros registrados.")
        return []

    print("\nLibros registrados:")
    for libro in libros:
        print(libro)
    return libros


def cargar_autor():
    nombre = pedir_texto("Nombre del autor: ")
    nacionalidad = pedir_texto("Nacionalidad: ")
    id_autor = registrar_autor(nombre, nacionalidad)
    autor = Autor(id_autor, nombre, nacionalidad)
    print(f"Autor registrado correctamente: ID {autor.id_autor} - {autor}")


def cargar_libro():
    autores = mostrar_autores()
    if not autores:
        print("Primero debe registrar un autor.")
        return

    ids_validos = {autor.id_autor for autor in autores}
    titulo = pedir_texto("Título del libro: ")
    anio = pedir_entero("Año de publicación: ")
    autor_id = pedir_entero("ID del autor: ")
    while autor_id not in ids_validos:
        print("No existe un autor con ese ID.")
        autor_id = pedir_entero("ID del autor: ")

    id_libro = registrar_libro(titulo, anio, autor_id)
    autor = next(autor for autor in autores if autor.id_autor == autor_id)
    libro = Libro(id_libro, titulo, anio, autor)
    print(f"Libro registrado correctamente: {libro}")


def modificar_libro():
    if not mostrar_libros():
        return
    id_libro = pedir_entero("ID del libro que desea modificar: ")
    nuevo_titulo = pedir_texto("Nuevo título: ")
    if actualizar_titulo_libro(id_libro, nuevo_titulo):
        print("Título actualizado correctamente.")
    else:
        print("No existe un libro con ese ID.")


def borrar_libro():
    if not mostrar_libros():
        return
    id_libro = pedir_entero("ID del libro que desea eliminar: ")
    if eliminar_libro(id_libro):
        print("Libro eliminado correctamente.")
    else:
        print("No existe un libro con ese ID.")


def ejecutar_menu():
    inicializar_bd()
    while True:
        print("""
===== SISTEMA DE GESTIÓN DE BIBLIOTECA =====
1. Registrar autor
2. Registrar libro
3. Listar autores
4. Listar libros
5. Modificar título de un libro
6. Eliminar libro
0. Salir
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cargar_autor()
        elif opcion == "2":
            cargar_libro()
        elif opcion == "3":
            mostrar_autores()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            modificar_libro()
        elif opcion == "6":
            borrar_libro()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_menu()
