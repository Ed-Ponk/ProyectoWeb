from bd import obtener_conexion


def insertar_marca(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO marca(nombre) VALUES (%s)",
                       (nombre,))
    conexion.commit()
    conexion.close()


def obtener_marca():
    conexion = obtener_conexion()
    marcas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM marca where vigencia=true")
        marcas = cursor.fetchall()
    conexion.close()
    return marcas


def eliminar_marca(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM marca WHERE id_marca = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_marca_por_id(id):
    conexion = obtener_conexion()
    marca = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM marca WHERE id_marca = %s", (id,))
        marca = cursor.fetchone()
    conexion.close()
    return marca

def actualizar_marca(nombre, vigencia, id_marca):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE marca SET nombre = %s, vigencia = %s WHERE id_marca = %s",
                       (nombre, vigencia, id_marca))
    conexion.commit()
    conexion.close()


#extra
def obtener_marca_por_name(name):
    conexion = obtener_conexion()
    marca = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM marca WHERE nombre = %s", (name,))
        marca = cursor.fetchone()
    conexion.close()
    return marca
