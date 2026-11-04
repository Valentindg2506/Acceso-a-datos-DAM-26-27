class Agenda:

    def __init__(self, archivo):
        self.archivo = archivo


    def guardar(self, nombre, telefono):
        archivo = open(self.archivo, "a")

        archivo.write(nombre + "," + telefono + "\n")

        archivo.close()


    def leer(self):
        archivo = open(self.archivo, "r")

        for linea in archivo:
            datos = linea.strip().split(",")

            print("Nombre: " + datos[0] + " - Telefono: " + datos[1])

        archivo.close()


# PROGRAMA PRINCIPAL

print("--- MI AGENDA ---")

agenda = Agenda("agenda.csv")

agenda.guardar("Marta", "611222333")
agenda.guardar("Pablo", "622333444")
agenda.guardar("Lucia", "633444555")

agenda.leer()

