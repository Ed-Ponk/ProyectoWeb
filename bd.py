import pymysql

def obtener_conexion():
    return pymysql.connect(host='127.0.0.1',
                                port=8889,
                                user='root',
                                password='3024',
                                db='proyectoWeb')