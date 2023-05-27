from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador_cliente, controlador_categoria, controlador_detalle_venta, controlador_marca, controlador_metodo_pago, controlador_producto, controlador_venta

app = Flask(__name__)


"""

@app.route("/agregar_cliente")
def formulario_agregar_cliente():
    return render_template("agregar_cliente.html")


@app.route("/guardar_cliente", methods=["POST"])
def guardar_disco():
    nombres = request.form["nombres"]
    contraseña = request.form["contraseña"]
    email = request.form["email"]
    controlador_cliente.insertar_cliente(nombres, contraseña, email)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/clientes")
"""


@app.route("/")
@app.route("/clientes")
def clientes():
    clientes = controlador_cliente.obtener_cliente()
    return render_template("clientes.html", clientes=clientes)


"""
@app.route("/eliminar_disco", methods=["POST"])
def eliminar_disco():
    controlador_cliente.eliminar_disco(request.form["id"])
    return redirect("/discos")


@app.route("/formulario_editar_disco/<int:id>")
def editar_disco(id):
    # Obtener el disco por ID
    disco = controlador_cliente.obtener_disco_por_id(id)
    return render_template("editar_disco.html", disco=disco)


@app.route("/actualizar_disco", methods=["POST"])
def actualizar_disco():
    id = request.form["id"]
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    precio = request.form["precio"]
    genero = request.form["genero"]
    controlador_cliente.actualizar_disco(codigo, nombre, artista, precio, genero, id)
    return redirect("/discos")

"""


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
