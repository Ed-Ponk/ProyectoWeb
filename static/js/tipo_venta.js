const openModalEditTipoVentaButtons = document.querySelectorAll('.showModalEditTipoVenta');
const closeModalEditButtons = document.querySelectorAll('.closeModalEdit');

if(openModalEditTipoVentaButtons){
  for (let i = 0; i < openModalEditTipoVentaButtons.length; i++) {
      const button = openModalEditTipoVentaButtons[i];
      button.addEventListener('click', (e) => {
          e.preventDefault();
          const modalsEdit = document.querySelectorAll('.edit');
          modalsEdit[0].classList.add('edit--show');
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
      const enlacesEdicion = document.querySelectorAll("a.showModalEditTipoVenta");
      let chkEstado;
      enlacesEdicion.forEach(function (enlace) {
          enlace.addEventListener("click", function (event) {
              event.preventDefault();
              const codigo = this.getAttribute("data-codigo");
              // Aquí puedes utilizar el valor de 'codigo' para realizar alguna acción en JavaScript
              const url = "http://127.0.0.1:8000/tipos_venta/" + codigo; // Reemplaza la URL con la dirección y el puerto de tu API
  
              fetch(url)
                  .then(response => response.json())
                  .then(data => {
                      const id_tipo_venta = data[0];
                      const nombre = data[1];
                      const vigencia = data[2];
                      if(vigencia==1){
                        chkEstado = true;
                      }else{
                        chkEstado = false;
                      }
                      document.querySelector(".input-nombre").value = nombre;
                      document.querySelector(".chkVigencia").checked = chkEstado;
                      document.querySelector(".input-id").value = id_tipo_venta;
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