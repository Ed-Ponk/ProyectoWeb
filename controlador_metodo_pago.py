from bd import obtener_conexion


def insertar_metodo_pago(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO metodo_pago(nombre) VALUES (%s)",
                       (nombre,))
    conexion.commit()
    conexion.close()


def obtener_metodo_pago():
    conexion = obtener_conexion()
    metodos_pago = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM metodo_pago where vigencia=true")
        metodos_pago = cursor.fetchall()
    conexion.close()
    return metodos_pago


def eliminar_metodo_pago(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM metodo_pago WHERE id_metodo_pago = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_metodo_pago_por_id(id):
    conexion = obtener_conexion()
    metodo_pago = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM metodo_pago WHERE id_metodo_pago = %s", (id,))
        metodo_pago = cursor.fetchone()
    conexion.close()
    return metodo_pago

def actualizar_metodo_pago(nombre, vigencia, id_metodo_pago):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE metodo_pago SET nombre = %s, vigencia = %s WHERE id_metodo_pago = %s",
                       (nombre, vigencia, id_metodo_pago))
    conexion.commit()
    conexion.close()


#extra
def obtener_metodo_pago_por_name(name):
    conexion = obtener_conexion()
    metodo_pago = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM metodo_pago WHERE nombre = %s", (name,))
        metodo_pago = cursor.fetchone()
    conexion.close()
    return metodo_pago
