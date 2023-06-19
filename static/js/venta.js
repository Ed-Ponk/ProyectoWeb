
const tipoVentaSelect = document.getElementById('tipo_venta');
const tipoVentaInput = document.querySelector('.tipo_venta_save');
const metodoPagoSelect = document.getElementById('metodo_pago');
const metodoPagoInput = document.querySelector('.metodo_pago_save');

const categoriaSelect = document.querySelector('.category-select');
const marcaSelect = document.querySelector('.brand-select');
const productoSelect = document.querySelector('.product-select');

// Capturar el evento de cambio en el select
tipoVentaSelect.addEventListener('change', function () {
  // Obtener el valor seleccionado
  const selectedValue = this.value;

  // Asignar el valor al campo input
  tipoVentaInput.value = selectedValue;
});

metodoPagoSelect.addEventListener('change', function () {
  // Obtener el valor seleccionado
  const selectedValue = this.value;

  // Asignar el valor al campo input
  metodoPagoInput.value = selectedValue;
});

categoriaSelect.addEventListener('change', function () {
  filtroProducto();
});

marcaSelect.addEventListener('change', function () {
  filtroProducto();
});

function filtroProducto() {

  let categoria = document.querySelector(".category-select");
  let marca = document.querySelector(".brand-select");

  let codigo_categoria = categoria.value;
  let codigo_marca = marca.value;

  if (codigo_categoria != 'default' && codigo_marca != 'default') {
    const url = 'http://127.0.0.1:8000/productos_filtrados_categoria_marca/' + codigo_categoria + '/' + codigo_marca;

    fetch(url)
      .then(response => response.json())
      .then(data => {

        let select_producto = document.querySelector(".product-select");
        select_producto.innerHTML = "";
        let option_default = document.createElement("option");

        option_default.text = "--Seleccione Producto--";
        option_default.value = "default";
        select_producto.appendChild(option_default);
        data.forEach(item => {
          const id_producto = item[0];
          const nombre = item[1];

          let option = document.createElement("option");
          option.text = nombre;
          option.value = id_producto;
          select_producto.appendChild(option);
        });
      })
      .catch(error => {
        console.error("Error en la solicitud:", error);
      });
  } else {
    if (codigo_categoria != 'default') {
      const url = 'http://127.0.0.1:8000/productos_filtrados_categoria/' + codigo_categoria;

      fetch(url)
        .then(response => response.json())
        .then(data => {

          let select_producto = document.querySelector(".product-select");
          select_producto.innerHTML = "";
          let option_default = document.createElement("option");

          option_default.text = "--Seleccione Producto--";
          option_default.value = "default";
          select_producto.appendChild(option_default);
          data.forEach(item => {
            const id_producto = item[0];
            const nombre = item[1];

            let option = document.createElement("option");
            option.text = nombre;
            option.value = id_producto;
            select_producto.appendChild(option);
          });
        })
        .catch(error => {
          console.error("Error en la solicitud:", error);
        });
    } else {
      if (codigo_marca != 'default') {
        const url = 'http://127.0.0.1:8000/productos_filtrados_marca/' + codigo_marca;

        fetch(url)
          .then(response => response.json())
          .then(data => {

            let select_producto = document.querySelector(".product-select");
            select_producto.innerHTML = "";
            let option_default = document.createElement("option");

            option_default.text = "--Seleccione Producto--";
            option_default.value = "default";
            select_producto.appendChild(option_default);
            data.forEach(item => {
              const id_producto = item[0];
              const nombre = item[1];

              let option = document.createElement("option");
              option.text = nombre;
              option.value = id_producto;
              select_producto.appendChild(option);
            });
          })
          .catch(error => {
            console.error("Error en la solicitud:", error);
          });
      }
    }
  }
}


function obtenerStockPrecio() {
  let producto = document.querySelector(".product-select");

  let codigo_producto = producto.value;

  if (codigo_producto != 'default') {
    const url = 'http://127.0.0.1:8000/productos_stock_precio/' + codigo_producto;

    fetch(url)
      .then(response => response.json())
      .then(data => {

        let stock = document.querySelector(".stock-input");
        let price = document.querySelector(".price-input");

        data.forEach(item => {
          stock.value = item[0];
          price.value = item[1];
        });
      })
      .catch(error => {
        console.error("Error en la solicitud:", error);
      });
  }
}

const buscar = document.getElementById('btn-search');

buscar.addEventListener('click', function () {
  // Código que se ejecuta al hacer clic en el botón
  let dniInput = document.querySelector(".input-dni");
  let dni = dniInput.value;

  const dniPattern = /^\d{8}$/; // Expresión regular para un DNI de 8 dígitos
  if (!dniPattern.test(dni)) {
    alert("Ingrese un DNI válido de 8 dígitos");
    return; // Detener la ejecución si el DNI no tiene el formato correcto
  }

  const url = 'http://127.0.0.1:8000/buscar_cliente/' + encodeURIComponent(dni);
  let name = document.querySelector(".input-info");
  let name_save = document.querySelector(".cliente_save");

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(response.status + ' ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      if (data.hasOwnProperty('mensaje') && data.mensaje === 'Cliente no encontrado') {
        throw new Error('Cliente no encontrado');
      }
      name.value = data[1];
      name_save.value = data[0];
    })
    .catch(error => {
      if (error.message.includes('404') || error.message.includes('Cliente no encontrado')) {
        alert('Cliente no encontrado');
        name.value = '';
      } else {
        console.error("Error en la solicitud:", error);
        alert("Ocurrió un error en la solicitud");
      }
    });
});

const agregarProducto = document.getElementById('add-product');
const productos = {}; // Objeto para realizar el seguimiento de los productos y cantidades

agregarProducto.addEventListener('click', function () {
  const product = document.querySelector('.product-select');
  const brand = document.querySelector('.brand-select');
  const stock = document.querySelector('.stock-input');
  const price = document.querySelector('.price-input');
  const quantity = document.querySelector('.quantity-input');

  const productId = product.value;

  // Verificar si el producto ya existe en la tabla

  if (productos.hasOwnProperty(productId)) {
    // Incrementar la cantidad del producto existente
    const existingRow = productos[productId].row;
    const existingQuantity = parseInt(existingRow.querySelector('.quantity-cell').textContent);
    const existingTotal = parseFloat(existingRow.querySelector('.total-cell').textContent);
    const newQuantity = existingQuantity + parseInt(quantity.value);
    const newTotal = existingTotal + (parseFloat(price.value) * parseInt(quantity.value));

    // Actualizar la cantidad y el importe en la fila existente
    existingRow.querySelector('.quantity-cell').textContent = newQuantity;
    existingRow.querySelector('.total-cell').textContent = newTotal.toFixed(2);
    calcularTotal();
  } else {
    // Crear nueva fila de tabla
    const newRow = document.createElement('tr');

    // Agregar celdas a la fila
    const productIdCell = document.createElement('td');
    productIdCell.textContent = productId;

    const productNameCell = document.createElement('td');
    productNameCell.textContent = product.options[product.selectedIndex].text;

    const brandCell = document.createElement('td');
    brandCell.textContent = brand.options[brand.selectedIndex].text; // Agregar la marca seleccionada


    const quantityCell = document.createElement('td');
    quantityCell.textContent = quantity.value;
    quantityCell.classList.add('quantity-cell'); // Agregar una clase para facilitar su selección

    const priceCell = document.createElement('td');
    priceCell.textContent = price.value;

    const totalCell = document.createElement('td');
    totalCell.textContent = (parseFloat(price.value) * parseInt(quantity.value)).toFixed(2);
    totalCell.classList.add('total-cell'); // Agregar una clase para facilitar su selección

    // Agregar las celdas a la fila
    newRow.appendChild(productIdCell);
    newRow.appendChild(productNameCell);
    newRow.appendChild(brandCell);
    newRow.appendChild(quantityCell);
    newRow.appendChild(priceCell);
    newRow.appendChild(totalCell);

    // Crear las celdas para los botones "Eliminar" y "Editar"
    const deleteCell = document.createElement('td');
    const editCell = document.createElement('td');

    // Crear los botones "Eliminar" y "Editar"
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Eliminar';
    deleteButton.classList.add('button');
    deleteButton.classList.add('is-danger');

    deleteButton.addEventListener('click', function () {
      // Obtener el producto ID
      const productId = this.parentNode.parentNode.querySelector('td:first-child').textContent;
      // Eliminar la fila de la tabla
      this.parentNode.parentNode.remove();
      // Eliminar el producto del objeto productos
      delete productos[productId];
    });

    const editButton = document.createElement('button');
    editButton.textContent = 'Editar';
    editButton.classList.add('button');
    editButton.classList.add('is-info');

    // Agregar los botones a las celdas correspondientes
    deleteCell.appendChild(deleteButton);
    editCell.appendChild(editButton);

    // Agregar las celdas de los botones a la fila
    newRow.appendChild(deleteCell);
    newRow.appendChild(editCell);

    // Agregar la nueva fila al tbody de la tabla
    const tableBody = document.querySelector('.table tbody');
    tableBody.appendChild(newRow);

    // Agregar el producto y la fila correspondiente al objeto productos
    productos[productId] = {
      row: newRow
    };

    deleteButton.addEventListener('click', function () {
      // Obtener la fila a eliminar
      const rowToDelete = this.parentNode.parentNode;
      // Eliminar la fila de la tabla
      rowToDelete.remove();
      calcularTotal();
    });


    editButton.addEventListener('click', function () {
      // Obtener la fila a editar
      const rowToEdit = this.parentNode.parentNode;
      // Realizar acciones de edición, por ejemplo, obtener los datos de la fila y mostrarlos en un formulario de edición
      // ...
    });

    calcularTotal();
  }
});

function calcularTotal() {
  let total = 0;

  // Recorrer cada fila de la tabla y sumar los importes
  const rows = document.querySelectorAll('.table tbody tr');
  rows.forEach(function (row) {
    const importe = parseFloat(row.querySelector('.total-cell').textContent);
    total += importe;
  });

  // Mostrar el total en la celda correspondiente
  const totalCell = document.getElementById('total-cell');
  const totalSave = document.querySelector('.total_save');
  totalCell.textContent = total.toFixed(2);
  totalSave.value = total.toFixed(2);
}

const form = document.querySelector('.form__save');
const guardarTodo = document.querySelector('.guardar-todo');

form.addEventListener('submit', function (event) {
  event.preventDefault();

  form.submit();

  setTimeout(function() {
    guardar_detalle_venta();
    window.location.href = 'http://127.0.0.1:8000/ventas';
  }, 300);
});

function guardar_detalle_venta() {
  const tableBody = document.getElementById('table-body');
  const rows = tableBody.querySelectorAll('tr');
  const detalleVenta = [];

  rows.forEach(row => {
    const idProducto = row.querySelector('td:nth-child(1)').textContent;
    const producto = row.querySelector('td:nth-child(2)').textContent;
    const marca = row.querySelector('td:nth-child(3)').textContent;
    const cantidad = row.querySelector('td:nth-child(4)').textContent;
    const precio = row.querySelector('td:nth-child(5)').textContent;
    const importe = row.querySelector('td:nth-child(6)').textContent;

    // Crea un objeto con los datos de cada fila
    const grupoProducto = {
      idProducto: idProducto,
      producto: producto,
      marca: marca,
      cantidad: cantidad,
      precio: precio,
      importe: importe
    };

    // Agrega el objeto al array
    detalleVenta.push(grupoProducto);
  });

  // Convierte el array a JSON
  const detalleVentaJSON = JSON.stringify(detalleVenta);

  fetch('http://127.0.0.1:8000/guardar_detalle_venta', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: detalleVentaJSON
  })
    .then(response => response.json())
    .then(responseData => {
      console.log(responseData);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}