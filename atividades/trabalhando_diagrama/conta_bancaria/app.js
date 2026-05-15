class Cliente {
    constructor(nome, cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }

    apresentar() {
        console.log(`Cliente: ${this.nome}`);
        console.log(`CPF: ${this.cpf}`);
    }
}

function main() {
    var cliente1 = new Cliente(
        "Jacó",
        "254520561"
    );
    cliente1.apresentar()
}
main()