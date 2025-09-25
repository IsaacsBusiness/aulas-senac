class Pessoa:
    def __init__(self, nome, idade, nacionalidade="Brasileiro(a)"):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

    def apresentar(self):
        print(
            f"\nOlá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.nacionalidade}.\n"
        )


# # Exemplo de uso
if __name__ == "__main__":
    pessoa1 = Pessoa("Ana", 30)
    pessoa2 = Pessoa("João", 25, "Português")

    pessoa1.apresentar()
    pessoa2.apresentar()

    # # Solicitando dados do usuário
    nome = input("Digite seu nome:")
    idade = int(input("Digite a sua idade: "))
    nacionalidade = input("Digite sua nacionalidade: ")

    # # Criando objeto com os dados fornecidos
    pessoa3 = Pessoa(nome, idade, nacionalidade)

    # # Apresentando a pessoa
    pessoa3.apresentar()
