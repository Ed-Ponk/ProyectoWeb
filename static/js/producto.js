
const openModalEditProductoButtons = document.querySelectorAll('.showModalEditProducto');

const closeModalEditButtons = document.querySelectorAll('.closeModalEdit');

if(openModalEditProductoButtons){
  for (let i = 0; i < openModalEditProductoButtons.length; i++) {
      const button = openModalEditProductoButtons[i];
      button.addEventListener('click', (e) => {
          e.preventDefault();
          const modalsEdit = document.querySelectorAll('.edit');
          modalsEdit[0].classList.add('edit--show');
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
      const enlacesEdicion = document.querySelectorAll("a.showModalEditProducto");
      let chkEstado;
      enlacesEdicion.forEach(function (enlace) {
          enlace.addEventListener("click", function (event) {
              event.preventDefault();
              const codigo = this.getAttribute("data-codigo");
              // Aquí puedes utilizar el valor de 'codigo' para realizar alguna acción en JavaScript
              const url = "http://127.0.0.1:8000/productos/" + codigo; // Reemplaza la URL con la dirección y el puerto de tu API
  
              fetch(url)
                  .then(response => response.json())
                  .then(data => {
                      const id_producto = data[0];
                      const nombre = data[1];
                      const descripcion = data[2];
                      const precio = data[3];
                      const stock = data[4];
                      const modelo = data[5];
                      const marca = data[6];
                      const categoria = data[7];
                      const vigencia = data[8];

                      if(vigencia==1){
                        chkEstado = true;
                      }else{
                        chkEstado = false;
                      }

                      document.querySelector(".input-nombre").value = nombre;
                      document.querySelector(".input-descripcion").value = descripcion;
                      document.querySelector(".input-precio").value = precio;
                      document.querySelector(".input-stock").value = stock;
                      document.querySelector(".input-modelo").value = modelo;
                      document.querySelector(".select-marca").value = marca;
                      document.querySelector(".select-categoria").value = categoria;
                      document.querySelector(".chkVigencia").checked = chkEstado;
                      document.querySelector(".input-id").value = id_producto;
                  })
                  .catch(error => {
                      console.error("Error en la solicitud:", error);
                  });
          });
      });
  });
}

if(closeModalEditButtons){
  for (let i = 0; i < closeModalEditButtons.length; i++) {
      const button = closeModalEditButtons[i];
      button.addEventListener('click', (e) => {
          e.preventDefault();
          const modalsEdit = document.querySelectorAll('.edit');
  
          modalsEdit[0].classList.remove('edit--show');
      });
  }
}