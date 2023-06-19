from bd import obtener_conexion


def insertar_venta(fecha, total, cliente_id, metodo_pago_id, usuario_id, tipo_venta):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO venta(fecha, total, cliente_id, metodo_pago_id, usuario_id, tipo_venta_id) VALUES (%s, %s, %s, %s, %s, %s)",
                       (fecha, total, cliente_id, metodo_pago_id, usuario_id, tipo_venta))
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

def obtener_venta_filtro():
    conexion = obtener_conexion()
    ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_venta, concat(cl.nombres,' ',cl.apellido) as cliente, mp.nombre as metodo_pago, tp.nombre as tipo_venta, concat(us.nombres,' ', us.apellido) as empleado, fecha ,total FROM venta ve inner join cliente cl on ve.cliente_id=cl.id_cliente inner join metodo_pago mp on ve.metodo_pago_id=mp.id_metodo_pago inner join tipo_venta tp on ve.tipo_venta_id=tp.id_tipo_venta inner join usuario us on ve.usuario_id=us.id_usuario order by id_venta")
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

def obtener_usuario():
    conexion = obtener_conexion()
    usuario = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_usuario, concat(nombres,' ',apellido) as full_name FROM usuario where tipo='v' and vigencia=true")
        usuario = cursor.fetchall()
    conexion.close()
    return usuario


def obtener_id_ultimo():
    conexion = obtener_conexion()

    with conexion.cursor() as cursor:
        cursor.execute("select max(id_venta) as id_venta from venta")
        resultado = cursor.fetchone()
    conexion.close()
    return resultado[0]