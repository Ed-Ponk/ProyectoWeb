from bd import obtener_conexion


def insertar_cliente(nombres, apellido, dni, email, telefono):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cliente(nombres, apellido, dni, email, telefono) VALUES (%s, %s, %s, %s, %s)",
                       (nombres, apellido, dni, email, telefono))
    conexion.commit()
    conexion.close()


def obtener_cliente():
    conexion = obtener_conexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_cliente, nombres, apellido, dni, email, telefono, CASE WHEN vigencia THEN 'Vigente' ELSE 'No Vigente' END as vigencia FROM cliente ORDER by id_cliente")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes


def eliminar_cliente(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_cliente_por_id(id):
    conexion = obtener_conexion()
    cliente = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM cliente WHERE id_cliente = %s", (id,))
        cliente = cursor.fetchone()
    conexion.close()
    return cliente


def actualizar_cliente(nombres, apellido, dni, email, telefono, vigencia, id_cliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cliente SET nombres = %s, apellido = %s, dni= %s, email = %s, telefono = %s, vigencia = %s WHERE id_cliente = %s",
                       (nombres, apellido, dni, email, telefono, vigencia, id_cliente))
    conexion.commit()
    conexion.close()


def buscar_cliente_por_dni(dni):
    conexion = obtener_conexion()
    cliente = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select id_cliente, CONCAT(nombres,' ',apellido) as full_name from cliente where dni= %s and vigencia=true", (dni,))
        cliente = cursor.fetchone()
    conexion.close()
    return cliente