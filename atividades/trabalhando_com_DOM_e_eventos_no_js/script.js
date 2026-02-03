function trocaPaginas() {

    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("inpSenha").value;
    let mensagem = document.getElementById("pMensagem");

    //se a dropdownlist não estiver selecionada
    if (usuario === "0") {
        mensagem.innerHTML = "Selecione o tipo de usuário!";
    }

    // Vendedor
    else if (usuario === "1" && senha === "123") {
        alert("Você será direcionado para a página de conta bancária.");
        window.location.href = "vendas.html";
    }

    // Estoquista
    else if (usuario === "2" && senha === "456") {
        alert("Você será direcionado para a página de conta salário.");
        window.location.href = "estoque.html";
    }

    // Admin
    else if (usuario === "3" && senha === "789") {
        alert("Você será direcionado para a página de benefício aposentadoria.");
        window.location = "admin.html";
    }

    // Erro
    else {
        mensagem.hidden = false
        mensagem.innerHTML = "Usuário ou senha inválidos!";
    }
}
