from bd import obtener_conexion


def insertar_venta(fecha, total, cliente_id, metodo_pago_id, usuario_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO venta(fecha, total, cliente_id, metodo_pago_id, usuario_id) VALUES (%s, %s, %s, %s, %s)",
                       (fecha, total, cliente_id, metodo_pago_id, usuario_id))
    conexion.commit()
    conexion.close()


def obtener_venta():
    conexion = obtener_conexion()
    ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM venta")
        ventas = cursor.fetchall()
    conexion.close()
    return ventas


def eliminar_venta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM venta WHERE id_venta = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_venta_por_id(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM venta WHERE id_venta = %s", (id,))
        venta = cursor.fetchone()
    conexion.close()
    return venta

def actualizar_venta(fecha, total, cliente_id, metodo_pago_id, usuario_id, id_venta):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE venta SET fecha = %s, total = %s, cliente_id = %s, metodo_pago_id = %s, usuario_id = %s WHERE id_venta = %s",
                       (fecha, total, cliente_id, metodo_pago_id, usuario_id, id_venta))
    conexion.commit()
    conexion.close()


#extra
