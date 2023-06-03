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
        cursor.execute("SELECT pr.id_producto, pr.nombre, pr.descripcion, pr.precio, pr.stock, pr.modelo, ma.nombre, ca.nombre, CASE WHEN pr.vigencia THEN 'Vigente' ELSE 'No Vigente' END as vigencia FROM producto pr inner join marca ma on pr.marca_id=ma.id_marca inner join categoria ca on pr.categoria_id=ca.id_categoria ORDER by pr.id_producto")
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

def actualizar_producto(nombre, descripcion, precio, stock, modelo, marca_id, categoria_id, vigencia, id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, descripcion = %s, precio= %s, stock= %s, modelo=%s, marca_id= %s, categoria_id= %s, vigencia = %s WHERE id_producto = %s",
                       (nombre, descripcion, precio, stock, modelo, marca_id, categoria_id, vigencia, id_producto))
    conexion.commit()
    conexion.close()



#extra
def obtener_producto_por_categoria(id):
    conexion = obtener_conexion()
    productos_filtrados=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_producto, nombre FROM  producto where categoria_id = %s", (id,))
        productos_filtrados = cursor.fetchall()
    conexion.close()
    return productos_filtrados

def obtener_producto_por_marca(id):
    conexion = obtener_conexion()
    productos_filtrados=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_producto, nombre FROM  producto where marca_id = %s", (id,))
        productos_filtrados = cursor.fetchall()
    conexion.close()
    return productos_filtrados

def obtener_producto_por_categoria_marca(id_categoria, id_marca):
    conexion = obtener_conexion()
    productos_filtrados=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_producto, nombre FROM  producto where categoria_id = %s and marca_id = %s", (id_categoria, id_marca))
        productos_filtrados = cursor.fetchall()
    conexion.close()
    return productos_filtrados

def obtener_stock_precio(id):
    conexion = obtener_conexion()
    dato_producto=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT stock, precio FROM  producto where id_producto = %s", (id, ))
        dato_producto = cursor.fetchall()
    conexion.close()
    return dato_producto
