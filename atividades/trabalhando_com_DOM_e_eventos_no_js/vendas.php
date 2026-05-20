<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vendas</title>
    <link rel="stylesheet" href="css/estoque.css">
</head>

<body>
    <main class="estoque-wrapper">


        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Registro de Vendas</h1>
            </div>

            <div>
                <a href="estoque.php"><button class="btn-novo-produto">Estoque</button></a>
                <button class="btn-sair" onclick="abrirModalSair()">Sair do Sistema</button>
            </div>
        </div>


        <div class="estoque-filtro">
            <input type="text" placeholder="Buscar produto...">
        </div>


        <div class="tabela-container">
            <table>
                <thead>
                    <tr>
                        <th>Produto</th>
                        <th>Preço/kg</th>
                        <th>Estoque</th>
                        <th>Venda (kg)</th>
                        <th>Ação</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Farinha de Trigo</td>
                        <td>R$ 23,52</td>
                        <td>54,00 kg</td>
                        <td><input type="number" step="0.01"></td>
                        <td><button class="btn-vender">Vender</button></td>
                    </tr>
                </tbody>
            </table>
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