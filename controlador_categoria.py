from bd import obtener_conexion


def insertar_categoria(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO categoria(nombre) VALUES (%s)",
                       (nombre,))
    conexion.commit()
    conexion.close()


def obtener_categoria():
    conexion = obtener_conexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM categoria where vigencia=true")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias


def eliminar_categoria(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_categoria_por_id(id):
    conexion = obtener_conexion()
    categoria = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM categoria WHERE id_categoria = %s", (id,))
        categoria = cursor.fetchone()
    conexion.close()
    return categoria

def actualizar_categoria(nombre, vigencia, id_categoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE categoria SET nombre = %s, vigencia = %s WHERE id_categoria = %s",
                       (nombre, vigencia, id_categoria))
    conexion.commit()
    conexion.close()


#extra
def obtener_categoria_por_name(name):
    conexion = obtener_conexion()
    categoria = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM categoria WHERE nombre = %s", (name,))
        categoria = cursor.fetchone()
    conexion.close()
    return categoria
