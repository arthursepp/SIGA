var iconFolder = document.getElementById("iconFolder");

document.addEventListener('DOMContentLoaded', function () {
    const avisoClick = document.getElementById('avisoSide');
    const matriculaClick = document.getElementById('matriculaSide');
    const consultaClick = document.getElementById('consultaSide');
    const agendaClick = document.getElementById('agendaSide')
    const segurancaClick = document.getElementById('segurancaSide');
    const solicitacaoClick = document.getElementById('solicitacoesSide');
    const bibliotecaClick = document.getElementById('bibliotecaSide');
    const uploadClick = document.getElementById('uploadSide');
    const planoEnsinoSide = document.getElementById('planoEnsinoSide');
    const matrizClick = document.getElementById('matrizSide');

    const avisoDiv = document.getElementById('avisos');
    const matriculaDiv = document.getElementById('matricula');
    const consultaDiv = document.getElementById('consulta');
    const agendaDiv = document.getElementById('agenda');
    const segurancaDiv = document.getElementById('seguranca');
    const solicitacaoDiv = document.getElementById('solicitacao');
    const bibliotecaDiv = document.getElementById('biblioteca');
    const uploadDiv = document.getElementById('upload');
    const planoEnsinoDiv = document.getElementById('planoEnsino');
    const matrizDiv = document.getElementById('matrizIngles');    

    matriculaDiv.style.display = 'none';
    consultaDiv.style.display = 'none';
    agendaDiv.style.display = 'none';
    segurancaDiv.style.display = 'none';
    solicitacaoDiv.style.display = 'none';
    bibliotecaDiv.style.display = 'none';
    uploadDiv.style.display = 'none';
    planoEnsinoDiv.style.display = 'none';
    matrizDiv.style.display = 'none';

    avisoDiv.style.display = 'block';


    openSidebarMobile()
    closeSidebarMobile()
    closeSidebar()
    dropdownClick()
});

function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdown-content");

    if (dropdownContent.classList.contains("show")) {
        dropdownContent.classList.remove("show");
        iconFolder.classList.remove("fa-regular", "fa-folder-open");
        iconFolder.classList.add("fa-solid", "fa-folder");
    } else {
        dropdownContent.classList.add("show");
        iconFolder.classList.remove("fa-solid", "fa-folder");
        iconFolder.classList.add("fa-regular", "fa-folder-open");
    }
}

window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function openSidebarMobile() {
    const open = document.getElementById('openSidebar');
    const close = document.getElementById('close');

    const sidebar = document.getElementById('sidebarMobile');

    open.addEventListener('click', () => {

        if (sidebar.style.display === '' || sidebar.style.display === 'none') {
            sidebar.style.display = 'block';
            close.style.display = 'block';
            sidebar.style.backgroundColor = '#FFF';
        }
    })

}

function closeSidebarMobile() {
    const close = document.getElementById('close');

    const sidebar = document.getElementById('sidebarMobile');

    close.addEventListener('click', () => {
        if (sidebar.style.display === 'block') {
            sidebar.style.display = 'none';
        }
    })
}

function closeSidebar() {
    const sidebar = document.getElementById('sidebarMobile');
    sidebar.style.display = 'none';
    iconFolder.classList.remove("fa-regular", "fa-folder-open");
    iconFolder.classList.add("fa-solid", "fa-folder");
}

function dropdownClick() {

    const avisoClick = document.getElementById('avisoSide');
    const matriculaClick = document.getElementById('matriculaSide');
    const consultaClick = document.getElementById('consultaSide');
    const agendaClick = document.getElementById('agendaSide')
    const segurancaClick = document.getElementById('segurancaSide');
    const solicitacaoClick = document.getElementById('solicitacoesSide');
    const bibliotecaClick = document.getElementById('bibliotecaSide');
    const uploadClick = document.getElementById('uploadSide');
    const planoEnsinoSide = document.getElementById('planoEnsinoSide');
    const matrizClick = document.getElementById('matrizSide');

    const avisoDiv = document.getElementById('avisos');
    const matriculaDiv = document.getElementById('matricula');
    const consultaDiv = document.getElementById('consulta');
    const agendaDiv = document.getElementById('agenda');
    const segurancaDiv = document.getElementById('seguranca');
    const solicitacaoDiv = document.getElementById('solicitacao');
    const bibliotecaDiv = document.getElementById('biblioteca');
    const uploadDiv = document.getElementById('upload');
    const planoEnsinoDiv = document.getElementById('planoEnsino');
    const matrizDiv = document.getElementById('matrizIngles');


    avisoClick.addEventListener('click', () => {
        if (avisoDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            matriculaDiv.style.display = 'none'
            avisoDiv.style.display = 'block';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';


        }
    })

    matriculaClick.addEventListener('click', () => {
        if (matriculaDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'block';
            matriculaDiv.style.display = 'flex'
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';
        }
    })

    consultaClick.addEventListener('click', () => {
        if (consultaDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'block';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';
        }
    })

    agendaClick.addEventListener('click', () => {
        if (agendaDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'block';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';
        }
    })

    segurancaClick.addEventListener('click', () => {
        if (segurancaDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'block';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';
        }
    })

    solicitacaoClick.addEventListener('click', () => {
        if (solicitacaoDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'block';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';
        }
    })

    bibliotecaClick.addEventListener('click', () => {
        if (bibliotecaDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'flex';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';
        }
    })

    uploadClick.addEventListener('click', () => {
        if (uploadDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'block';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'none';
        }
    })

    planoEnsinoSide.addEventListener('click', () => {
        if (planoEnsinoDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'block';
            matrizDiv.style.display = 'none';
        }
    })

    matrizClick.addEventListener('click', () => {
        if (matrizDiv.style.display === 'block') {
            return
        } else {
            matriculaDiv.style.display = 'none';
            avisoDiv.style.display = 'none';
            consultaDiv.style.display = 'none';
            agendaDiv.style.display = 'none';
            segurancaDiv.style.display = 'none';
            solicitacaoDiv.style.display = 'none';
            bibliotecaDiv.style.display = 'none';
            uploadDiv.style.display = 'none';
            planoEnsinoDiv.style.display = 'none';
            matrizDiv.style.display = 'flex';
        }
    })
}

const dropdownElements = [
    document.getElementById('avisoSide'),
    document.getElementById('matriculaSide'),
    document.getElementById('consultaSide'),
    document.getElementById('agendaSide'),
    document.getElementById('segurancaSide'),
    document.getElementById('solicitacoesSide'),
    document.getElementById('bibliotecaSide'),
    document.getElementById('uploadSide'),
    document.getElementById('planoEnsinoSide'),
    document.getElementById('matrizSide')
];

dropdownElements.forEach(element => {
    element.addEventListener('click', () => {
        closeSidebar();
    });
});
