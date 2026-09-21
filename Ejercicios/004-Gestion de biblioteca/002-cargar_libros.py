import json

NOMBRE_FICHERO = "biblioteca.dat"


def leer_fichero():
	################ Leemos el contenido del fichero ####################
	flujo = open(NOMBRE_FICHERO, "r")

	lineas = flujo.readlines()

	flujo.close()

	return lineas[0]


def deserializar_libros(linea):
	################ Convertimos el texto JSON otra vez en una lista ####################
	libros = json.loads(linea)

	return libros


def main():
	linea = leer_fichero()

	print("--- Contenido leído del fichero ---")
	print(linea)
	print("Tipo:", type(linea))

	libros = deserializar_libros(linea)

	print("\n--- Lista de libros reconstruida ---")
	print(libros)
	print("Tipo:", type(libros))


if __name__ == "__main__":
	main()

