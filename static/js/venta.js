
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


function obtenerStockPrecio(){
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
