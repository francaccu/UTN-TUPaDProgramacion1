class Libro:
    """Ejercicio 1: un libro se asocia con un objeto Autor existente."""

    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        # Agregación: recibimos un Autor; no lo creamos dentro del Libro.
        self.autor = autor

    def __str__(self):
        return (
            f"ID: {self.id_libro} | Título: {self.titulo} | "
            f"Año: {self.anio_publicacion} | Autor: {self.autor}"
        )
