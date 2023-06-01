let listElements = document.querySelectorAll('.list__button--click');

listElements.forEach(listElement => {
    listElement.addEventListener('click', () => {

        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;
        if (menu.clientHeight == "0") {
            height = menu.scrollHeight;
        }

        menu.style.height = `${height}px`;

    })
});


const modalAdd = document.getElementById("agregar");
const openModalAdd = document.getElementById('showModalAdd');
const closeModalAdd = document.getElementById('closeModalAdd');

const openModalEditClienteButtons = document.querySelectorAll('.showModalEditCliente');
const openModalEditCategoriaButtons = document.querySelectorAll('.showModalEditCategoria');
const openModalEditMarcaButtons = document.querySelectorAll('.showModalEditMarca');
const closeModalEditButtons = document.querySelectorAll('.closeModalEdit');


openModalAdd.addEventListener('click', (e) => {
    e.preventDefault();

    modalAdd.classList.add('add--show');
});


closeModalAdd.addEventListener('click', (e) => {
    e.preventDefault();
    modalAdd.classList.remove('add--show');
});



for (let i = 0; i < openModalEditClienteButtons.length; i++) {
    const button = openModalEditClienteButtons[i];
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const modalsEdit = document.querySelectorAll('.edit');
        modalsEdit[0].classList.add('edit--show');
    });
}

for (let i = 0; i < openModalEditCategoriaButtons.length; i++) {
    const button = openModalEditCategoriaButtons[i];
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const modalsEdit = document.querySelectorAll('.edit');
        modalsEdit[0].classList.add('edit--show');
    });
}

for (let i = 0; i < openModalEditMarcaButtons.length; i++) {
    const button = openModalEditMarcaButtons[i];
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const modalsEdit = document.querySelectorAll('.edit');
        modalsEdit[0].classList.add('edit--show');
    });
}

for (let i = 0; i < closeModalEditButtons.length; i++) {
    const button = closeModalEditButtons[i];
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const modalsEdit = document.querySelectorAll('.edit');

        modalsEdit[0].classList.remove('edit--show');
    });
}

/*Tablas a editar*/
document.addEventListener("DOMContentLoaded", function () {
    const enlacesEdicion = document.querySelectorAll("a.showModalEditCliente");

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

                    document.querySelector(".input-nombres").value = nombres;
                    document.querySelector(".input-apellido").value = apellido;
                    document.querySelector(".input-dni").value = dni;
                    document.querySelector(".input-email").value = email;
                    document.querySelector(".input-telefono").value = telefono;
                    document.querySelector(".input-vigencia").value = vigencia;
                    document.querySelector(".input-id").value = id_cliente;
                })
                .catch(error => {
                    console.error("Error en la solicitud:", error);
                });
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const enlacesEdicion = document.querySelectorAll("a.showModalEditCategoria");

    enlacesEdicion.forEach(function (enlace) {
        enlace.addEventListener("click", function (event) {
            event.preventDefault();
            const codigo = this.getAttribute("data-codigo");
            // Aquí puedes utilizar el valor de 'codigo' para realizar alguna acción en JavaScript
            const url = "http://127.0.0.1:8000/categorias/" + codigo; // Reemplaza la URL con la dirección y el puerto de tu API

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const id_categoria = data[0];
                    const nombre = data[1];
                    const vigencia = data[2];

                    document.querySelector(".input-nombre").value = nombre;
                    document.querySelector(".input-vigencia").value = vigencia;
                    document.querySelector(".input-id").value = id_categoria;
                })
                .catch(error => {
                    console.error("Error en la solicitud:", error);
                });
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const enlacesEdicion = document.querySelectorAll("a.showModalEditMarca");

    enlacesEdicion.forEach(function (enlace) {
        enlace.addEventListener("click", function (event) {
            event.preventDefault();
            const codigo = this.getAttribute("data-codigo");
            // Aquí puedes utilizar el valor de 'codigo' para realizar alguna acción en JavaScript
            const url = "http://127.0.0.1:8000/marcas/" + codigo; // Reemplaza la URL con la dirección y el puerto de tu API

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const id_marca = data[0];
                    const nombre = data[1];
                    const vigencia = data[2];

                    document.querySelector(".input-nombre").value = nombre;
                    document.querySelector(".input-vigencia").value = vigencia;
                    document.querySelector(".input-id").value = id_marca;
                })
                .catch(error => {
                    console.error("Error en la solicitud:", error);
                });
        });
    });
});