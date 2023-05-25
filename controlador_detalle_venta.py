from bd import obtener_conexion


def insertar_detalle_venta(cantidad, precio_unitario, subtotal, venta_id, producto_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_venta(cantidad, precio_unitario, subtotal, venta_id, producto_id) VALUES (%s,%s,%s,%s,%s)",
                       (cantidad, precio_unitario, subtotal, venta_id, producto_id))
    conexion.commit()
    conexion.close()


def obtener_detalle_venta():
    conexion = obtener_conexion()
    detalle_ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM detalle_venta")
        detalle_ventas = cursor.fetchall()
    conexion.close()
    return detalle_ventas


def eliminar_detalle_venta(venta_id, producto_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle_venta WHERE venta_id = %s and producto_id = %s", (venta_id, producto_id))
    conexion.commit()
    conexion.close()


def obtener_detalle_venta_por_id(venta_id, producto_id):
    conexion = obtener_conexion()
    detalle_venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM detalle_venta WHERE venta_id = %s and producto_id = %s", (venta_id, producto_id))
        detalle_venta = cursor.fetchone()
    conexion.close()
    return detalle_venta

def actualizar_detalle_venta(cantidad, precio_unitario, subtotal, venta_id, producto_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_venta SET cantidad = %s, precio_unitario = %s, subtotal = %s WHERE venta_id = %s and producto_id = %s",
                       (cantidad, precio_unitario, subtotal, venta_id, producto_id))
    conexion.commit()
    conexion.close()


#extra

