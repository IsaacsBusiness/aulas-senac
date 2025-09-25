class ContaBancaria:
    def __init__(self, titular):
        self.titular, self.saldo = titular, 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("\nSaldo insuficiente !!")

    def mostrar_saldo(self):
        print(f"\n{self.titular} seu saldo é de R$ {self.saldo:.2f}\n")


# Uso
conta = ContaBancaria("Zack")
conta.depositar(100)
conta.sacar(15)
conta.mostrar_saldo()
conta.sacar(90)  # Saldo insuficiente

# Novo usuário (conta2)
nome_titular = input("\nInforme o nome do titular da conta: ")
conta2 = ContaBancaria(nome_titular)  # Instanciando a conta com o nome do titular

saldo_inicial = float(input("Informe o saldo inicial: "))  # Recebe saldo como float
conta2.depositar(saldo_inicial)  # Deposita o saldo inicial

conta2.mostrar_saldo()  # Mostra o saldo após o depósito
valor_saque = float(input("Informe o valor do saque: "))  # Recebe valor de saque

conta2.sacar(valor_saque)  # Realiza o saque
conta2.mostrar_saldo()  # Mostra o saldo após o saque
