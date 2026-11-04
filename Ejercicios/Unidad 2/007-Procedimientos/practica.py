import mysql.connector


# PASO 4 - Conectar Python y llamar a listar_libros

conexion = mysql.connector.connect(
    host="localhost",
    user="app_biblioteca",
    password="Biblio_2026",
    database="biblioteca"
)

cursor = conexion.cursor()

print("=== Listado de libros ===")

cursor.callproc("listar_libros", ())

for resultado in cursor.stored_results():
    for id_libro, titulo, autor, ejemplares in resultado.fetchall():
        print(f"{id_libro} - {titulo} ({autor}) - {ejemplares} ejemplares")


# PASO 5 - Procedimiento con parámetro de entrada

print()
print("=== Libros de Federico García Lorca ===")

cursor.callproc("buscar_por_autor", ("Federico García Lorca",))

for resultado in cursor.stored_results():
    for titulo, ejemplares in resultado.fetchall():
        print(f"{titulo} - {ejemplares} ejemplares")


# PASO 6 - Procedimiento con parámetro de salida

print()
print("=== Total de libros ===")

resultado = cursor.callproc("contar_libros", (0,))

print(f"Hay {resultado[0]} libros en la biblioteca")


# PASO 8 - Prestar un libro desde Python

print()
print("=== Préstamo del libro 1 ===")

try:
    cursor.callproc("prestar_libro", (1,))
    conexion.commit()
    print("Préstamo registrado")
except mysql.connector.Error as e:
    conexion.rollback()
    print("Error:", e.msg)


print()
print("=== Préstamo del libro 4 ===")

try:
    cursor.callproc("prestar_libro", (4,))
    conexion.commit()
    print("Préstamo registrado")
except mysql.connector.Error as e:
    conexion.rollback()
    print("Error:", e.msg)


# PASO 9 - Comprobar los permisos

print()
print("=== Prueba de permisos ===")

try:
    cursor.execute("SELECT * FROM libros")
    print(cursor.fetchall())
except mysql.connector.Error as e:
    print("Acceso denegado:", e.msg)


cursor.close()
conexion.close()
