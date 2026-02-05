<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin</title>
    <link rel="stylesheet" href="css/estoque.css">
</head>

<body>
    <main class="estoque-wrapper">


        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Painel Administrativo</h1>
            </div>
        </div>


        <div class="dashboard">
            <div class="card">📦 Produtos<br><strong>12</strong></div>
            <div class="card">⚖️ Estoque Total<br><strong>325,40 kg</strong></div>
            <div class="card">💰 Valor Estimado<br><strong>R$ 8.450,00</strong></div>
        </div>


        <div class="acoes-admin">
            <div>
                <a href="estoque.php"><button class="btn-gerenciar-estoque">Gerenciar Estoque</button></a>
                <a href="vendas.php"><button class="btn-registrar-venda">Registrar Venda</button></a>
            </div>

            <button class="btn-sair" onclick="abrirModalSair()">Sair do Sistema</button>
        </div>

    </main>

    <!-- MODAL SAIR DO SISTEMA -->
    <div id="modalSair" class="modal">
        <div class="modal-content">
            <h3>Sair do Sistema</h3>
            <p>Tem certeza que deseja sair?</p>

            <div class="modal-actions">
                <button onclick="fecharModalSair()" class="btn-cancelar">Cancelar</button>
                <a href="index.html">
                    <button class="btn-excluir">Sair</button>
                </a>
            </div>
        </div>
    </div>

    <script src="js/script.js"></script>
    
</body>

</html>