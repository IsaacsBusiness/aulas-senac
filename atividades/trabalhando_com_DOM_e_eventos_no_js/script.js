let timeoutMensagem; // controle global

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

function trocaPaginas() {
    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("inpSenha").value;

    // dropdown não selecionada
    if (usuario === "0") {
        mostrarMensagem("Selecione o tipo de usuário!");
    }

    // Vendedor
    else if (usuario === "1" && senha === "123") {
        window.location.href = "vendas.html";
    }

    // Estoquista
    else if (usuario === "2" && senha === "456") {
        window.location.href = "estoque.html";
    }

    // Admin
    else if (usuario === "3" && senha === "789") {
        window.location.href = "admin.html";
    }

    // erro geral
    else {
        mostrarMensagem("Usuário ou senha inválidos!");
    }
}
