from bd import obtener_conexion


def insertar_cliente(nombres, contraseña, email):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cliente(nombres, contraseña, email) VALUES (%s, %s, %s)",
                       (nombres, contraseña, email))
    conexion.commit()
    conexion.close()


def obtener_cliente():
    conexion = obtener_conexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes


def eliminar_cliente(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_cliente_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM cliente WHERE id_cliente = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_cliente(nombres, contraseña, email, vigencia, id_cliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cliente SET nombres = %s, contraseña = %s, email = %s, vigencia = %s WHERE id_cliente = %s",
                       (nombres, contraseña, email, vigencia, id_cliente))
    conexion.commit()
    conexion.close()
