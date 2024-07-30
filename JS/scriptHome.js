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

    dropdownClick()
    checkDivDisplay()

});


function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdown-content");
    if (dropdownContent.classList.contains("show")) {
        dropdownContent.classList.remove("show");
    } else {
        dropdownContent.classList.add("show");
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

function checkDivDisplay() {

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

    //------------------------------------------------------------------------

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

    if (avisoDiv.style.display === 'block') {
        avisoClick.style.backgroundColor = '#d0d0d0';
    } else if (matriculaDiv.style.display === 'block') {
        matriculaClick.style.backgroundColor = '#d0d0d0';
    } else if (consultaDiv.style.display === 'block') {
        consultaClick.style.backgroundColor = '#d0d0d0';
    } else if (agendaDiv.style.display === 'block') {
        agendaClick.style.backgroundColor = '#d0d0d0';
    } else if (segurancaDiv.style.display === 'block') {
        segurancaClick.style.backgroundColor = '#d0d0d0';
    } else if (solicitacaoDiv.style.display === 'block') {
        solicitacaoClick.style.backgroundColor = '#d0d0d0';
    } else if (solicitacaoDiv.style.display === 'block') {
        solicitacaoClick.style.backgroundColor = '#d0d0d0';
    } else if (bibliotecaDiv.style.display === 'block') {
        bibliotecaClick.style.backgroundColor = '#d0d0d0';
    } else if (uploadDiv.style.display === 'block') {
        uploadClick.style.backgroundColor = '#d0d0d0';
    } else if (planoEnsinoDiv.style.display === 'block') {
        planoEnsinoSide.style.backgroundColor = '#d0d0d0';
    } else if (matrizDiv.style.display === 'block') {
        matrizClick.style.backgroundColor = '#d0d0d0';
    }
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
            consultaDiv.style.display = 'flex';
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
