import requests


URL_BASE = "http://127.0.0.1:5000/api"


def mostrar_respuesta(nombre, respuesta):
    print(f"\n--- {nombre} ---")
    print("Codigo HTTP:", respuesta.status_code)
    print("Respuesta:", respuesta.json())


print("PRUEBA AUTOMATICA DE LA API")

respuesta = requests.get(f"{URL_BASE}/libros")
mostrar_respuesta("GET /api/libros", respuesta)

nuevo_autor = {
    "nombre": "Antoine de Saint-Exupery",
    "nacionalidad": "Francesa",
}
respuesta_autor = requests.post(f"{URL_BASE}/autores", json=nuevo_autor)
mostrar_respuesta("POST /api/autores", respuesta_autor)
respuesta_autor.raise_for_status()
id_autor = respuesta_autor.json()["id"]

nuevo_libro = {
    "titulo": "El principito",
    "anio": 1943,
    "autor_id": id_autor,
}
respuesta_libro = requests.post(f"{URL_BASE}/libros", json=nuevo_libro)
mostrar_respuesta("POST /api/libros", respuesta_libro)
respuesta_libro.raise_for_status()
id_libro = respuesta_libro.json()["id"]

nuevo_titulo = {"titulo": "El principito - Edicion actualizada"}
respuesta = requests.put(f"{URL_BASE}/libros/{id_libro}", json=nuevo_titulo)
mostrar_respuesta("PUT /api/libros/<id>", respuesta)

respuesta = requests.delete(f"{URL_BASE}/libros/{id_libro}")
mostrar_respuesta("DELETE /api/libros/<id>", respuesta)

respuesta = requests.get(f"{URL_BASE}/libros/{id_libro}")
mostrar_respuesta("VERIFICACION FINAL", respuesta)

if respuesta.status_code == 404:
    print("\nPrueba terminada correctamente: el libro fue eliminado.")
else:
    print("\nLa prueba termino, pero no se pudo confirmar la eliminacion.")
