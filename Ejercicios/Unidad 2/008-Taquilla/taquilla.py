import mysql.connector


# PASO 2 - Conéctate desde Python

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="taquilla"
)
conexion.autocommit = True
cursor = conexion.cursor()


# PASO 3 - Muestra los datos

def ver_estado():
    cursor.execute("SELECT * FROM clientes")
    print("CLIENTES:", cursor.fetchall())
    cursor.execute("SELECT * FROM entradas")
    print("ENTRADAS:", cursor.fetchall())
    print()

ver_estado()


# PASO 4 - Mira el problema (ya ejecutado una vez, por eso está comentado)

# try:
#     cursor.execute("UPDATE clientes SET saldo = saldo - 20 WHERE id = 1")
#     cursor.execute("INSERT INTO entrada (cliente_id, evento) VALUES (1, 'Concierto')")
# except Exception as error:
#     print("Error:", error)
#
# ver_estado()

# cursor.execute("UPDATE clientes SET saldo = saldo + 20 WHERE id = 1")


# PASO 5 - Crea la compra con transacción

def comprar(cliente_id, evento, precio):
    try:
        conexion.start_transaction()

        cursor.execute("UPDATE clientes SET saldo = saldo - %s WHERE id = %s",
                       (precio, cliente_id))

        cursor.execute("SELECT saldo FROM clientes WHERE id = %s", (cliente_id,))
        saldo = cursor.fetchone()[0]
        if saldo < 0:
            raise Exception("saldo insuficiente")

        cursor.execute("INSERT INTO entradas (cliente_id, evento) VALUES (%s, %s)",
                       (cliente_id, evento))

        conexion.commit()
        print("Compra realizada")

    except Exception as error:
        conexion.rollback()
        print("Compra cancelada:", error)


# PASO 6 - Prueba la función

comprar(1, "Concierto", 20)
ver_estado()

comprar(2, "Festival", 40)
ver_estado()


# PASO 7 - Cierra la conexión

cursor.close()
conexion.close()
