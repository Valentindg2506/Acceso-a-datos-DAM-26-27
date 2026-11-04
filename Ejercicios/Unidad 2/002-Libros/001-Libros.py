import mysql.connector


libros = [
    {
        "titulo": "Don Quijote",
        "paginas": 863,
        "generos": ["novela", "aventuras", "humor"]
    },
    {
        "titulo": "Platero y yo",
        "paginas": 144,
        "generos": ["poesía", "infantil"]
    },
    {
        "titulo": "Marianela",
        "paginas": 256,
        "generos": ["novela"]
    }
]


# PASO 2 - Averiguar el tipo de cada dato

print("--- TIPOS DE DATOS ---")

muestra = libros[0]

for clave in muestra.keys():
    print(clave, type(muestra[clave]))


# PASO 3 - Conectarse a la base de datos

conn = mysql.connector.connect(
    host="localhost",
    user="desfase",
    password="desfase",
    database="desfase"
)

cursor = conn.cursor()


# PASO 4 - Borrar las tablas si ya existen

cursor.execute("DROP TABLE IF EXISTS libros_generos")
cursor.execute("DROP TABLE IF EXISTS libros")


# PASO 5 - Crear la tabla libros

cursor.execute("""
    CREATE TABLE libros (
        Identificador INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255),
        paginas INT
    )
""")


# PASO 6 - Crear la tabla de géneros

cursor.execute("""
    CREATE TABLE libros_generos (
        Identificador INT AUTO_INCREMENT PRIMARY KEY,
        libros_id INT,
        valor VARCHAR(255),

        FOREIGN KEY (libros_id)
        REFERENCES libros(Identificador)
    )
""")


# PASO 7 - Guardar los libros y sus géneros

for libro in libros:

    cursor.execute(
        "INSERT INTO libros (titulo, paginas) VALUES (%s, %s)",
        (
            libro["titulo"],
            libro["paginas"]
        )
    )

    id_libro = cursor.lastrowid

    for genero in libro["generos"]:

        cursor.execute(
            "INSERT INTO libros_generos (libros_id, valor) VALUES (%s, %s)",
            (
                id_libro,
                genero
            )
        )


conn.commit()


# PASO 8 - Recuperar los datos

recuperados = []

cursor.execute(
    "SELECT Identificador, titulo, paginas FROM libros"
)

filas_libros = cursor.fetchall()


for fila in filas_libros:

    id_libro = fila[0]
    titulo = fila[1]
    paginas = fila[2]

    cursor.execute(
        "SELECT valor FROM libros_generos WHERE libros_id = %s",
        (id_libro,)
    )

    filas_generos = cursor.fetchall()

    generos = []

    for fila_genero in filas_generos:
        generos.append(fila_genero[0])

    libro = {
        "titulo": titulo,
        "paginas": paginas,
        "generos": generos
    }

    recuperados.append(libro)


print("\n--- LIBROS RECUPERADOS ---")

print(recuperados)

print("\n¿Los datos recuperados son iguales a los originales?")

print(recuperados == libros)


cursor.close()
conn.close()
