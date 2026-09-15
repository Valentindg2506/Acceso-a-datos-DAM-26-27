NOMBRE_FICHERO_TEMPERATURAS = "temperaturas.txt"
NOMBRE_FICHERO_CONTADOR = "contador.bin"


def escribir_temperaturas():
	################ ESCRIBIMOS LOS DATOS ####################
	print("\n--- 1. Flujo de salida: escribiendo las temperaturas ---")

	flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "w")

	flujo.write("18.5\n")
	flujo.write("21.0\n")
	flujo.write("19.2\n")

	flujo.close()

	print(f"Se ha escrito '{NOMBRE_FICHERO_TEMPERATURAS}' correctamente.")


def leer_temperaturas():
	################ LEEMOS LOS DATOS ####################
	"""Flujo de ENTRADA: el programa lee todo el fichero."""
	print("\n--- 2. Flujo de entrada: leyendo todo el fichero ---")

	flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")

	contenido = flujo.read()

	flujo.close()

	print(contenido)


def saltar_primera_temperatura():
	################ SALTAMOS LA PRIMERA LINEA Y LEEMOS EL RESTO ####################
	"""El puntero controla en qué posición del fichero estamos."""
	print("--- 3. Moviendo el puntero con seek() ---")

	flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")

	flujo.readline()             # LEEMOS LA PRIMER TEMPERATURA
	posicion = flujo.tell()      # GUARDAMOS LA POSICION DEL PUNTERO

	flujo.seek(0)                # VOLVEMOS AL PRINCIPIO
	flujo.seek(posicion)         # VOLVEMOS A LA POSICION GUARDADA

	resto = flujo.read()         # LEEMOS LAS DOS TEMPERATURAS QUE QUEDARON

	flujo.close()

	print("Nos saltamos la primera temperatura y leemos el resto:")
	print(resto)


def comprobar_fichero_configuracion():
	################ MANEJAMOS LAS EXCEPCIONES ####################
	"""Manejo de excepciones: qué pasa si el fichero no existe."""
	print("--- 4. Manejo de excepciones ---")

	try:
		flujo = open("configuracion.txt", "r")
		flujo.close()

	except FileNotFoundError:
		print("Error controlado: el fichero no existe, pero el programa no se cae.")


def guardar_numero_registros():
	################ GUARDAMOS EL REGISTRO EN BINARIO ####################
	"""Fichero binario: guardamos el número de temperaturas."""
	print("\n--- 5. Trabajando con un fichero binario ---")

	datos = bytes([3])  # HAY 3 TEMPERATURAS GUARDADAS

	flujo_salida = open(NOMBRE_FICHERO_CONTADOR, "wb")
	flujo_salida.write(datos)
	flujo_salida.close()

	flujo_entrada = open(NOMBRE_FICHERO_CONTADOR, "rb")
	leido = flujo_entrada.read()
	flujo_entrada.close()

	print(f"Byte escrito: {list(datos)}")
	print(f"Byte leído:   {list(leido)}")
	print(f"Número de registros: {leido[0]}")


def main():
	escribir_temperaturas()
	leer_temperaturas()
	saltar_primera_temperatura()
	comprobar_fichero_configuracion()
	guardar_numero_registros()


if __name__ == "__main__":
	main()


