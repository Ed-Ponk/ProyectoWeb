from bd import obtener_conexion


def insertar_producto(nombre, descripcion, precio, stock, modelo, marca_id, categoria_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO producto(nombre, descripcion, precio, stock, modelo, marca_id, categoria_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (nombre, descripcion, precio, stock, modelo, marca_id, categoria_id))
    conexion.commit()
    conexion.close()


def obtener_producto():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM producto where vigencia=true")
        productos = cursor.fetchall()
    conexion.close()
    return productos


def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM producto WHERE id_producto = %s", (id,))
        producto = cursor.fetchone()
    conexion.close()
    return producto

def actualizar_categoria(nombre, descripcion, precio, stock, modelo, marca_id, categoria_id, id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE categoria SET nombre = %s, descripcion = %s, precio= %s, stock= %s, modelo=%s, marca_id= %s, categoria= %s, vigencia = %s WHERE id_producto = %s",
                       (nombre, descripcion, precio, stock, modelo, marca_id, categoria_id, id_producto))
    conexion.commit()
    conexion.close()


#extra
"""
def obtener_categoria_por_name(name):
    conexion = obtener_conexion()
    categoria = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM categoria WHERE nombre = %s", (name,))
        categoria = cursor.fetchone()
    conexion.close()
    return categoria
"""




