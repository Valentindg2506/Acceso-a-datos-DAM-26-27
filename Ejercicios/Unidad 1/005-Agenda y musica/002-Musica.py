import os


def mostrar(carpeta, espacios):

    for nombre in sorted(os.listdir(carpeta)):

        print(espacios + nombre)

        ruta = os.path.join(carpeta, nombre)

        if os.path.isdir(ruta):
            mostrar(ruta, espacios + "    ")


# PROGRAMA PRINCIPAL

print("--- MI MUSICA ---")

os.makedirs("mi_musica/rock/clasicos", exist_ok=True)
os.makedirs("mi_musica/pop", exist_ok=True)

archivo = open("mi_musica/lista.txt", "w")
archivo.close()

archivo = open("mi_musica/rock/clasicos/queen.mp3", "w")
archivo.close()

archivo = open("mi_musica/pop/abba.mp3", "w")
archivo.close()

mostrar("mi_musica", "")

