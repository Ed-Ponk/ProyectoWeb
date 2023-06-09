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


if(modalAdd){
    openModalAdd.addEventListener('click', (e) => {
        e.preventDefault();
    
        modalAdd.classList.add('add--show');
    });
    
    
    closeModalAdd.addEventListener('click', (e) => {
        e.preventDefault();

        modalAdd.classList.remove('add--show');
    });    
}





