from bd import obtener_conexion

def insertar_tipo_venta(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tipo_venta(nombre) VALUES (%s)",
                       (nombre,))
    conexion.commit()
    conexion.close()


def obtener_tipos_venta():
    conexion = obtener_conexion()
    tipos_venta = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo_venta, nombre, CASE WHEN vigencia THEN 'Vigente' ELSE 'No Vigente' END as vigencia FROM tipo_venta ORDER BY id_tipo_venta")
        tipos_venta = cursor.fetchall()
    conexion.close()
    return tipos_venta


def obtener_tipos_venta_vigentes():
    conexion = obtener_conexion()
    tipos_venta = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM tipo_venta WHERE vigencia = true")
        tipos_venta = cursor.fetchall()
    conexion.close()
    return tipos_venta


def eliminar_tipo_venta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM tipo_venta WHERE id_tipo_venta = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_tipo_venta_por_id(id):
    conexion = obtener_conexion()
    tipo_venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM tipo_venta WHERE id_tipo_venta = %s", (id,))
        tipo_venta = cursor.fetchone()
    conexion.close()
    return tipo_venta


def actualizar_tipo_venta(nombre, vigencia, id_tipo_venta):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tipo_venta SET nombre = %s, vigencia = %s WHERE id_tipo_venta = %s",
                       (nombre, vigencia, id_tipo_venta))
    conexion.commit()
    conexion.close()