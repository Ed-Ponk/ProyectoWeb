const openModalEditClienteButtons = document.querySelectorAll('.showModalEditCliente');

const closeModalEditButtons = document.querySelectorAll('.closeModalEdit');


if(openModalEditClienteButtons){
  for (let i = 0; i < openModalEditClienteButtons.length; i++) {
      const button = openModalEditClienteButtons[i];
      button.addEventListener('click', (e) => {
          e.preventDefault();
          const modalsEdit = document.querySelectorAll('.edit');
          modalsEdit[0].classList.add('edit--show');
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
      const enlacesEdicion = document.querySelectorAll("a.showModalEditCliente");
      let chkEstado;
      enlacesEdicion.forEach(function (enlace) {
          enlace.addEventListener("click", function (event) {
              event.preventDefault();
              const codigo = this.getAttribute("data-codigo");
              // Aquí puedes utilizar el valor de 'codigo' para realizar alguna acción en JavaScript
              const url = "http://127.0.0.1:8000/clientes/" + codigo; // Reemplaza la URL con la dirección y el puerto de tu API
  
              fetch(url)
                  .then(response => response.json())
                  .then(data => {
                      const id_cliente = data[0];
                      const nombres = data[1];
                      const apellido = data[2];
                      const dni = data[3];
                      const email = data[4];
                      const telefono = data[5];
                      const vigencia = data[6];
                      if(vigencia==1){
                        chkEstado = true;
                      }else{
                        chkEstado = false;
                      }

                      document.querySelector(".input-nombres").value = nombres;
                      document.querySelector(".input-apellido").value = apellido;
                      document.querySelector(".input-dni").value = dni;
                      document.querySelector(".input-email").value = email;
                      document.querySelector(".input-telefono").value = telefono;
                      document.querySelector(".chkVigencia").checked = chkEstado;
                      document.querySelector(".input-id").value = id_cliente;
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