# mis_notas.py
# Mi cuaderno de notas: repaso de todo lo visto con ficheros.

import csv
import json
import os


NOMBRE_NOTAS = "notas.csv"
NOMBRE_JSON = "notas.json"
NOMBRE_BINARIO = "total.bin"


def crear_fichero_notas():
    lineas = [
        "Ana,8\n",
        "Luis,6\n",
        "Marta,9\n"
    ]

    fichero = open(NOMBRE_NOTAS, "w")

    fichero.writelines(lineas)

    fichero.close()

    print("Fichero", NOMBRE_NOTAS, "creado con 3 alumnos.")


class Cuaderno:

    def __init__(self, archivo):
        self.archivo = archivo


    def anadir(self, nombre, nota):
        fichero = open(self.archivo, "a")

        fichero.write(nombre + "," + str(nota) + "\n")

        fichero.close()

        print("Añadido:", nombre, "con un", nota)


def leer_todo():
    fichero = open(NOMBRE_NOTAS, "r")

    contenido = fichero.read()

    fichero.close()

    print(contenido)


def leer_linea_a_linea():
    fichero = open(NOMBRE_NOTAS, "r")

    linea = fichero.readline()

    while linea != "":
        partes = linea.strip().split(",")

        print("Alumno:", partes[0], "- Nota:", partes[1])

        linea = fichero.readline()

    fichero.close()


def probar_seek_tell():
    fichero = open(NOMBRE_NOTAS, "r")

    primera = fichero.readline()

    posicion = fichero.tell()

    print("He leído:", primera.strip(), "- puntero en:", posicion)

    fichero.seek(0)

    print("Vuelvo al principio y leo otra vez:", fichero.readline().strip())

    fichero.seek(posicion)

    print("Salto a", posicion, "y leo:", fichero.readline().strip())

    fichero.close()


def cargar_con_csv():
    alumnos = []

    fichero = open(NOMBRE_NOTAS, "r")

    lector = csv.reader(fichero)

    for fila in lector:
        alumno = {
            "nombre": fila[0],
            "nota": int(fila[1])
        }

        alumnos.append(alumno)

    fichero.close()

    return alumnos


def guardar_json(alumnos):
    texto = json.dumps(alumnos)

    print("Tipo de alumnos:", type(alumnos))
    print("Tipo de texto:", type(texto))

    fichero = open(NOMBRE_JSON, "w")

    fichero.write(texto)

    fichero.close()

    print("Guardado en", NOMBRE_JSON)


def cargar_json():
    fichero = open(NOMBRE_JSON, "r")

    linea = fichero.readlines()[0]

    fichero.close()

    print("Tipo de lo leído:", type(linea))

    alumnos = json.loads(linea)

    print("Tipo tras json.loads:", type(alumnos))

    return alumnos


def leer_fichero_seguro(nombre):
    fichero = None

    try:
        fichero = open(nombre, "r")

        print("Contenido de", nombre + ":")

        print(fichero.read())

    except FileNotFoundError:
        print("Error: el fichero", nombre, "no existe.")

    except PermissionError:
        print("Error: no tienes permiso para leer", nombre)

    except IOError:
        print("Error: hubo un problema al leer", nombre)

    finally:
        if fichero is not None:
            fichero.close()

        print("Fin de la lectura de", nombre)


def guardar_total_binario(total):
    fichero = open(NOMBRE_BINARIO, "wb")

    fichero.write(bytes([total]))

    fichero.close()

    fichero = open(NOMBRE_BINARIO, "rb")

    datos = fichero.read()

    fichero.close()

    print("Número guardado en binario:", datos[0])


def listar_ficheros():
    for nombre in os.listdir("."):

        if nombre.startswith("notas") or nombre.endswith(".bin"):
            print("-", nombre)


def main():
    print("=== MI CUADERNO DE NOTAS ===")


    print("\n--- PASO 1: crear el fichero ---")
    crear_fichero_notas()


    print("\n--- PASO 2: añadir alumnos con la clase Cuaderno ---")

    cuaderno = Cuaderno(NOMBRE_NOTAS)

    cuaderno.anadir("Pablo", 7)
    cuaderno.anadir("Lucia", 10)


    print("\n--- PASO 3: leer todo de golpe ---")
    leer_todo()


    print("--- PASO 4: leer línea a línea ---")
    leer_linea_a_linea()


    print("\n--- PASO 5: seek y tell ---")
    probar_seek_tell()


    print("\n--- PASO 6: leer con csv ---")

    alumnos = cargar_con_csv()

    print(alumnos)


    print("\n--- PASO 7: guardar en JSON ---")
    guardar_json(alumnos)


    print("\n--- PASO 8: cargar el JSON ---")

    recuperados = cargar_json()

    for alumno in recuperados:
        print(alumno["nombre"], "tiene un", alumno["nota"])


    print("\n--- PASO 9: excepciones ---")

    leer_fichero_seguro(NOMBRE_NOTAS)
    leer_fichero_seguro("no_existe.txt")


    print("\n--- PASO 10: binario ---")

    guardar_total_binario(len(recuperados))


    print("\n--- PASO 11: ficheros creados ---")

    listar_ficheros()


if __name__ == "__main__":
	main()

