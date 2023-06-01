from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador_cliente, controlador_categoria, controlador_detalle_venta, controlador_marca, controlador_metodo_pago, controlador_producto, controlador_venta

app = Flask(__name__)

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


@app.route("/formulario_editar_cliente/<int:id>")
def editar_cliente(id):
    # Obtener el disco por ID
    cliente = controlador_cliente.obtener_cliente_por_id(id)
    return render_template("editar_cliente.html", cliente=cliente)


@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    id = request.form["id"]
    nombres = request.form["nombres"]
    apellido = request.form["apellido"]
    dni = request.form["dni"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    vigencia = request.form["vigencia"]
    controlador_cliente.actualizar_cliente(nombres, apellido, dni, email, telefono, vigencia, id)
    return redirect("/clientes")


#PRODUCTO

@app.route("/productos")
def productos():
    productos = controlador_producto.obtener_producto()
    return render_template("productos.html", productos=productos)


@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    modelo = request.form["modelo"]
    marca_id = request.form["marca_id"]
    categoria_id = request.form["categoria_id"]
    controlador_producto.insertar_producto(nombre, descripcion, precio, stock, modelo, marca_id, categoria_id)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/productos")

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_producto.eliminar_producto(request.form["id"])
    return redirect("/productos")


@app.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    # Obtener el disco por ID
    producto = controlador_producto.obtener_producto_por_id(id)
    return render_template("editar_producto.html", producto=producto)


@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    modelo = request.form["modelo"]
    marca_id = request.form["marca_id"]
    categoria_id = request.form["categoria_id"]
    vigencia = request.form["vigencia"]
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


@app.route("/formulario_editar_marca/<int:id>")
def editar_marca(id):
    marca = controlador_marca.obtener_marca_por_id(id)
    return render_template("editar_marca.html", marca=marca)


@app.route("/actualizar_marca", methods=["POST"])
def actualizar_marca():
    id = request.form["id"]
    nombre = request.form["nombre"]
    vigencia = request.form["vigencia"]
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


@app.route("/formulario_editar_categoria/<int:id>")
def editar_categoria(id):
    categoria = controlador_categoria.obtener_categoria_por_id(id)
    return render_template("editar_categoria.html", categoria=categoria)


@app.route("/actualizar_categoria", methods=["POST"])
def actualizar_categoria():
    id = request.form["id"]
    nombre = request.form["nombre"]
    vigencia = request.form["vigencia"]
    controlador_categoria.actualizar_categoria(nombre, vigencia, id)
    return redirect("/categorias")

#VENTA
@app.route("/ventas")
def ventas():
    ventas = controlador_venta.obtener_venta()
    return render_template("ventas.html", ventas=ventas)


@app.route("/agregar_venta")
def formulario_agregar_venta():
    return render_template("agregar_venta.html")


@app.route("/guardar_venta", methods=["POST"])
def guardar_venta():
    cliente = request.form["cliente"]
    metodo_pago = request.form["metodo_pago"]
    empleado = request.form["empleado"]
    fecha = request.form["fecha"]
    total = request.form["total"]
    controlador_venta.insertar_venta(cliente, metodo_pago, empleado, fecha, total)
    return redirect("/ventas")


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
