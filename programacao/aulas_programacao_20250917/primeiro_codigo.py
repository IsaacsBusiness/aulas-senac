class Prato:

    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def exibirDetalhes(self):
        print(f"{self.nome} - R${self.preco:.2f} - {self.descricao:}")


p = Prato("\n Pizza", 25.5, "Pizza de carne com queijo\n")
p.exibirDetalhes()


class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Pedido:

    def __init__(self, cliente):
        self.cliente = cliente
        self.pratos = []

    def adicionarPrato(self, prato):
        self.pratos.append(prato)

    def calcularTotal(self):
        return sum([p.preco for p in self.pratos])


c = Cliente("João", "(31)99999-9999")
p1 = Prato("Lasanha", 30.0, "Lasanha de carne com queijo")
p2 = Prato("Suco", 8.0, "Suco de laranja natural")

pedido = Pedido(c)
pedido.adicionarPrato(p1)
pedido.adicionarPrato(p2)

print(f"Cliente: {c.nome} - Telefone: {c.telefone}")
print(f"Total do Pedido: R$ {pedido.calcularTotal():.2f}\n")


class Entregador:
    def __init__(self, nome, veiculo):
        self.nome = nome
        self.veiculo = veiculo

    def entregarPedido(self, pedido):
        print(
            f"Entregador {self.nome} entregou pedido de {pedido.cliente.nome} usando uma {self.veiculo} branca.\n"
        )


e = Entregador("Isaac", "moto")
e.entregarPedido(pedido)


class Carro:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        self.disponivel = False

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.modelo} - {self.placa} - {status}"


carro = Carro("Corolla", "ABC-1R34")
print(carro, f"\n")
