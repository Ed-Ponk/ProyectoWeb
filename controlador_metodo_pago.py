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
        cursor.execute("SELECT id_metodo_pago, nombre, CASE WHEN vigencia THEN 'Vigente' ELSE 'No Vigente' END as vigencia FROM metodo_pago order by id_metodo_pago")
        metodos_pago = cursor.fetchall()
    conexion.close()
    return metodos_pago

def obtener_metodo_pago_vigente():
    conexion = obtener_conexion()
    metodo_pagos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM metodo_pago where vigencia=true")
        metodo_pagos = cursor.fetchall()
    conexion.close()
    return metodo_pagos

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



