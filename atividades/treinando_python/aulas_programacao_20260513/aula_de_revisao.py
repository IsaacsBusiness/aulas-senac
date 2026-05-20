class Pessoa:
    def __init__(self, nomePessoa, alturaPessoa, pesoPessoa):
        self.nomePessoa = nomePessoa
        self.alturaPessoa = alturaPessoa
        self.pesoPessoa = pesoPessoa
        
    def resultado(self):
        self.IMC = pesoPessoa / (alturaPessoa ** 2)
        print(f"\n{self.nomePessoa} seu IMC é de {self.IMC:.2f}\n")

if __name__ == "__main__":
    
    print("\nSistema de Calculo IMC\n")

    # # Coletando dados do usuário
    nomePessoa = str(input("Digite seu nome: "))
    alturaPessoa = float(input("Digite a sua altura: "))
    pesoPessoa = float(input("Digite o seu peso: "))

    # Criando o objeto fornecido pelo usuário
    pessoa1 = Pessoa(nomePessoa,alturaPessoa,pesoPessoa)

    # # Apresentando o resultado
    pessoa1.resultado()