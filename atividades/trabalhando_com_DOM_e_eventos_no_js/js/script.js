let timeoutMensagem; // controle global

// Função para mostrar mensagens temporárias
function mostrarMensagem(texto) {
    const mensagem = document.getElementById("pMensagem");

    mensagem.innerHTML = texto;
    mensagem.hidden = false;

    // limpa timeout anterior (se existir)
    clearTimeout(timeoutMensagem);

    // some após 3 segundos
    timeoutMensagem = setTimeout(() => {
        mensagem.hidden = true;
    }, 3000);
}

// Função para troca de páginas com base no usuário e senha
function trocaPaginas() {
    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("inpSenha").value;

    // Dropdown não selecionada
    if (usuario === "0") {
        mostrarMensagem("Selecione o tipo de usuário!");
    }

    // Vendedor
    else if (usuario === "1" && senha === "123") {
        window.location.href = "vendas.php";
    }

    // Estoquista
    else if (usuario === "2" && senha === "456") {
        window.location.href = "estoque.php";
    }

    // Admin
    else if (usuario === "3" && senha === "789") {
        window.location.href = "admin.php";
    }

    // erro geral
    else {
        mostrarMensagem("Usuário ou senha inválidos!");
    }
}

// Função para abrir o modal de exclusão
function abrirModal(id) {
    document.getElementById('modalExcluir').style.display = 'flex';
    document.getElementById('linkExcluir').href =
        'php-action/delete.php?id=' + id;
}

function fecharModal() {
    document.getElementById('modalExcluir').style.display = 'none';
}

function confirmarExclusao(id) {
    document.getElementById('linkExcluir').href =
        'php-action/delete.php?id=' + id;

    document.getElementById('modalExcluir').style.display = 'flex';
}

function fecharExcluir() {
    document.getElementById('modalExcluir').style.display = 'none';
}

// Desaparecer mensagem automaticamente
setTimeout(() => {
    const msg = document.querySelector('.msg');
    if (msg) {
        msg.style.opacity = '0';
        setTimeout(() => msg.remove(), 500);
    }
}, 5000); // desaparece após 5 segundos

// Funções para o modal de sair
function abrirModalSair() {
    document.getElementById('modalSair').style.display = 'flex';
}

function fecharModalSair() {
    document.getElementById('modalSair').style.display = 'none';
}
