from flask import Flask, render_template, request, redirect, flash, jsonify, Response
import controlador_cliente, controlador_categoria, controlador_detalle_venta, controlador_marca, controlador_metodo_pago, controlador_producto, controlador_venta, controlador_tipo_venta
import json
from datetime import datetime

app = Flask(__name__)


@app.template_filter('strftime')
def format_datetime(value, format='%Y-%m-%d'):
    return value.strftime(format)

@app.route("/buscar_cliente/<string:dni>", methods=["GET"])
def buscar_cliente(dni):
    cliente = controlador_cliente.buscar_cliente_por_dni(dni)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}) , 404 


@app.route("/productos_stock_precio/<int:id>", methods=["GET"])
def obtener_stock_precio(id):
    datos_producto = controlador_producto.obtener_stock_precio(id)
    if datos_producto:
        return jsonify(datos_producto)
    else:
        return jsonify({"mensaje": "Stock y cantidad del producto no encontrado"}), 404  

@app.route("/productos_filtrados_categoria_marca/<int:id_categoria>/<int:id_marca>", methods=["GET"])
def filtrar_producto_categoria_marca(id_categoria,id_marca):
    producto_filtrado = controlador_producto.obtener_producto_por_categoria_marca(id_categoria, id_marca)
    if producto_filtrado:
        return jsonify(producto_filtrado)
    else:
        return jsonify({"mensaje": "Producto por categoria y por marca no encontrado"}), 404  
        

@app.route("/productos_filtrados_categoria/<int:id>", methods=["GET"])
def filtrar_producto_categoria(id):
    producto_filtrado = controlador_producto.obtener_producto_por_categoria(id)
    if producto_filtrado:
        return jsonify(producto_filtrado)
    else:
        return jsonify({"mensaje": "Producto por categoria no encontrado"}), 404  

@app.route("/productos_filtrados_marca/<int:id>", methods=["GET"])
def filtrar_producto_marca(id):
    producto_filtrado = controlador_producto.obtener_producto_por_marca(id)
    if producto_filtrado:
        return jsonify(producto_filtrado)
    else:
        return jsonify({"mensaje": "Producto por marca no encontrado"}), 404  

@app.route("/tipos_venta/<int:id>", methods=["GET"])
def obtener_tipo_venta(id):
    tipo_venta = controlador_tipo_venta.obtener_tipo_venta_por_id(id)
    if tipo_venta:
        return jsonify(tipo_venta)
    else:
        return jsonify({"mensaje": "Tipo venta no encontrado"}), 404   

@app.route("/metodo_pagos/<int:id>", methods=["GET"])
def obtener_metodo_pago(id):
    metodo_pago = controlador_metodo_pago.obtener_metodo_pago_por_id(id)
    if metodo_pago:
        return jsonify(metodo_pago)
    else:
        return jsonify({"mensaje": "Metodo pago no encontrado"}), 404    

@app.route("/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    producto = controlador_producto.obtener_producto_por_id(id)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

@app.route("/clientes/<int:id>", methods=["GET"])
def obtener_cliente(id):
    cliente = controlador_cliente.obtener_cliente_por_id(id)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

@app.route("/categorias/<int:id>", methods=["GET"])
def obtener_categoria(id):
    categoria = controlador_categoria.obtener_categoria_por_id(id)
    if categoria:
        return jsonify(categoria)
    else:
        return jsonify({"mensaje": "Categoria no encontrado"}), 404

@app.route("/marcas/<int:id>", methods=["GET"])
def obtener_marca(id):
    marca = controlador_marca.obtener_marca_por_id(id)
    if marca:
        return jsonify(marca)
    else:
        return jsonify({"mensaje": "Marca no encontrado"}), 404

@app.route("/")
@app.route("/clientes")
def clientes():
    clientes = controlador_cliente.obtener_cliente()
    return render_template("clientes.html", clientes=clientes)


@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    nombres = request.form["nombres"]
    apellido = request.form["apellido"]
    dni = request.form["dni"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    controlador_cliente.insertar_cliente(nombres, apellido, dni, email, telefono)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/clientes")

@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    controlador_cliente.eliminar_cliente(request.form["id"])
    return redirect("/clientes")


@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    id = request.form["id"]
    nombres = request.form["nombres"]
    apellido = request.form["apellido"]
    dni = request.form["dni"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    if "vigencia" in request.form:
        vigencia=1
    else:
        vigencia=0 

    controlador_cliente.actualizar_cliente(nombres, apellido, dni, email, telefono, vigencia, id)
    return redirect("/clientes")


#PRODUCTO

@app.route("/productos")
def productos():
    productos = controlador_producto.obtener_producto()
    marcas = controlador_marca.obtener_marca_vigente()
    categorias = controlador_categoria.obtener_categoria_vigente()
    return render_template("productos.html", productos=productos, marcas=marcas, categorias=categorias)


@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    modelo = request.form["modelo"]
    marca_id = request.form.get("marca")
    categoria_id = request.form.get("categoria")
    controlador_producto.insertar_producto(nombre, descripcion, precio, stock, modelo, marca_id, categoria_id)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/productos")

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_producto.eliminar_producto(request.form["id"])
    return redirect("/productos")


@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    modelo = request.form["modelo"]
    marca_id = request.form["marca"]
    categoria_id = request.form["categoria"]

    if "vigencia" in request.form:
        vigencia=1
    else:
        vigencia=0  

    controlador_producto.actualizar_producto(nombre, descripcion, precio, stock, modelo, marca_id, categoria_id, vigencia, id)
    return redirect("/productos")

#MARCA

@app.route("/marcas")
def marcas():
    marcas = controlador_marca.obtener_marca()
    return render_template("marcas.html", marcas=marcas)


@app.route("/guardar_marca", methods=["POST"])
def guardar_marca():
    nombre = request.form["nombre"]
    controlador_marca.insertar_marca(nombre)
    return redirect("/marcas")

@app.route("/eliminar_marca", methods=["POST"])
def eliminar_marca():
    controlador_marca.eliminar_marca(request.form["id"])
    return redirect("/marcas")


@app.route("/actualizar_marca", methods=["POST"])
def actualizar_marca():
    id = request.form["id"]
    nombre = request.form["nombre"]

    if "vigencia" in request.form:
        vigencia=1
    else:
        vigencia=0       
    controlador_marca.actualizar_marca(nombre, vigencia, id)
    return redirect("/marcas")


#CATEGORIA

@app.route("/categorias")
def categorias():
    categorias = controlador_categoria.obtener_categoria()
    return render_template("categorias.html", categorias=categorias)


@app.route("/guardar_categoria", methods=["POST"])
def guardar_categoria():
    nombre = request.form["nombre"]
    controlador_categoria.insertar_categoria(nombre)
    return redirect("/categorias")

@app.route("/eliminar_categoria", methods=["POST"])
def eliminar_categoria():
    controlador_categoria.eliminar_categoria(request.form["id"])
    return redirect("/categorias")


@app.route("/actualizar_categoria", methods=["POST"])
def actualizar_categoria():
    id = request.form["id"]
    nombre = request.form["nombre"]
    if "vigencia" in request.form:
        vigencia=1
    else:
        vigencia=0   
    controlador_categoria.actualizar_categoria(nombre, vigencia, id)
    return redirect("/categorias")

#METODO_PAGO
@app.route("/metodo_pagos")
def metodo_pagos():
    metodo_pagos = controlador_metodo_pago.obtener_metodo_pago()
    return render_template("metodo_pagos.html", metodo_pagos=metodo_pagos)


@app.route("/guardar_metodo_pago", methods=["POST"])
def guardar_metodo_pago():
    nombre = request.form["nombre"]

    controlador_metodo_pago.insertar_metodo_pago(nombre)
    return redirect("/metodo_pagos")


@app.route("/eliminar_metodo_pago", methods=["POST"])
def eliminar_metodo_pago():
    controlador_metodo_pago.eliminar_metodo_pago(request.form["id"])
    return redirect("/metodo_pagos")


@app.route("/actualizar_metodo_pago", methods=["POST"])
def actualizar_metodo_pago():
    id = request.form["id"]
    nombre = request.form["nombre"]
    if "vigencia" in request.form:
        vigencia=1
    else:
        vigencia=0

    controlador_metodo_pago.actualizar_metodo_pago(nombre, vigencia, id)
    return redirect("/metodo_pagos")

#TIPO VENTA
@app.route("/tipos_venta")
def tipos_venta():
    tipos_venta = controlador_tipo_venta.obtener_tipos_venta()
    return render_template("tipos_venta.html", tipos_venta=tipos_venta)


@app.route("/guardar_tipo_venta", methods=["POST"])
def guardar_tipo_venta():
    nombre = request.form["nombre"]

    controlador_tipo_venta.insertar_tipo_venta(nombre)
    return redirect("/tipos_venta")


@app.route("/eliminar_tipo_venta", methods=["POST"])
def eliminar_tipo_venta():
    controlador_tipo_venta.eliminar_tipo_venta(request.form["id"])
    return redirect("/tipos_venta")


@app.route("/actualizar_tipo_venta", methods=["POST"])
def actualizar_tipo_venta():
    id = request.form["id"]
    nombre = request.form["nombre"]
    if "vigencia" in request.form:
        vigencia = 1
    else:
        vigencia = 0

    controlador_tipo_venta.actualizar_tipo_venta(nombre, vigencia, id)
    return redirect("/tipos_venta")


#VENTA
@app.route("/ventas")
def ventas():
    ventas = controlador_venta.obtener_venta_filtro()
    return render_template("ventas.html", ventas=ventas)


@app.route("/agregar_venta")
def formulario_agregar_venta():
    tipos_venta = controlador_tipo_venta.obtener_tipos_venta_vigentes()
    metodo_pagos = controlador_metodo_pago.obtener_metodo_pago_vigente()
    categorias = controlador_categoria.obtener_categoria_vigente()
    marcas = controlador_marca.obtener_marca_vigente()
    fecha_actual = datetime.now()
    usuario = controlador_venta.obtener_usuario()
    return render_template("agregar_venta.html", categorias=categorias, tipos_venta=tipos_venta, metodo_pagos= metodo_pagos, marcas=marcas, fecha_actual=fecha_actual, usuario=usuario)


@app.route("/guardar_venta", methods=["POST"])
def guardar_venta():
    cliente = request.form["cliente"]
    metodo_pago = request.form["metodo_pago"]
    tipo_venta = request.form["tipo_venta"]
    empleado = request.form["empleado"]
    fecha = request.form["fecha"]
    total = request.form["total"]
    controlador_venta.insertar_venta(fecha, total, cliente, metodo_pago, empleado, tipo_venta)

    response = Response(status=204)
    return response


@app.route("/guardar_detalle_venta", methods=["POST"])
def guardar_detalle_venta():
    venta_id = controlador_venta.obtener_id_ultimo()

    detalle_venta = json.loads(request.data) 

    for grupo_producto in detalle_venta:
        cantidad = grupo_producto["cantidad"]
        precio_unitario = grupo_producto["precio"]
        subtotal = grupo_producto["importe"]
        producto_id = grupo_producto["idProducto"]

        controlador_detalle_venta.insertar_detalle_venta(cantidad, precio_unitario, subtotal, venta_id, producto_id)

    return jsonify({"message": "Detalle de venta guardado correctamente"})

@app.route("/eliminar_venta", methods=["POST"])
def eliminar_venta():
    controlador_venta.eliminar_venta(request.form["id"])
    return redirect("/ventas")


@app.route("/formulario_editar_venta/<int:id>")
def editar_venta(id):
    # Obtener la venta por ID
    venta = controlador_venta.obtener_venta_por_id(id)
    return render_template("editar_venta.html", venta=venta)


@app.route("/actualizar_venta", methods=["POST"])
def actualizar_venta():
    id = request.form["id"]
    cliente = request.form["cliente"]
    metodo_pago = request.form["metodo_pago"]
    empleado = request.form["empleado"]
    fecha = request.form["fecha"]
    total = request.form["total"]
    controlador_venta.actualizar_ventaa(cliente, metodo_pago, empleado, fecha, total, id)
    return redirect("/ventas")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
