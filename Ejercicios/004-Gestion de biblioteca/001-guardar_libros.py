import json

NOMBRE_FICHERO = "biblioteca.dat"


def crear_lista_libros():
	################ Creamos una lista de diccionarios con los libros ####################
	libros = [
		{
			"titulo": "El tanque volador",
			"autor": "Juan Perez",
			"anio": 1800,
			"paginas": 100
		},
		{
			"titulo": "El avion que no vuela",
			"autor": "Don pepito",
			"anio": 1801,
			"paginas": 101
		},
		{
			"titulo": "La naranja trabaja",
			"autor": "Daniel",
			"anio": 1900,
			"paginas": 102
		}
	]

	return libros


def serializar_libros(libros):
	################ Convertimos la lista de Python en texto JSON ####################
	cadena = json.dumps(libros)

	print("\n--- Lista convertida a JSON ---")
	print(cadena)
	print("Tipo:", type(cadena))

	return cadena


def guardar_en_fichero(cadena):
	################ Guardamos la cadena JSON en un fichero ####################
	flujo = open(NOMBRE_FICHERO, "w")

	flujo.write(cadena)

	flujo.close()

	print(f"\nSe ha guardado '{NOMBRE_FICHERO}' correctamente.")


def main():
	libros = crear_lista_libros()

	print("--- Lista de libros ---")
	print(libros)
	print("Tipo:", type(libros))

	cadena = serializar_libros(libros)

	guardar_en_fichero(cadena)


if __name__ == "__main__":
	main()


