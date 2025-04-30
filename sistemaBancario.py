import datetime

# Classe Cliente
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = None

    def associar_conta(self, conta):
        self.conta = conta

# Classe ContaBancaria
class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self, cliente, saldo=0, limite=500):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"{datetime.datetime.now()} - Depósito: +R$ {valor:.2f}")
            print("✅ Depósito realizado com sucesso.")
        else:
            print("❌ Valor inválido para depósito.")

    def sacar(self, valor):
        if self.numero_saques >= ContaBancaria.LIMITE_SAQUES:
            print("❌ Limite diário de saques atingido.")
            return

        if valor > self.saldo:
            print("❌ Saldo insuficiente.")
        elif valor > self.limite:
            print("❌ Valor do saque excede o limite por operação.")
        elif valor > 0:
            self.saldo -= valor
            self.numero_saques += 1
            self.extrato.append(f"{datetime.datetime.now()} - Saque: -R$ {valor:.2f}")
            print("✅ Saque realizado com sucesso.")
        else:
            print("❌ Valor inválido para saque.")

    def exibir_extrato(self):
        print("\n========== EXTRATO ==========")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("==============================")


# Função para exibir o menu
def menu():
    print("""
========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================
""")

# Função principal
def main():
    # Criando um cliente e associando a conta bancária
    cliente = Cliente(nome="Ana Laura", cpf="123.456.789-00")
    conta = ContaBancaria(cliente)
    cliente.associar_conta(conta)

    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: R$ "))
            conta.depositar(valor)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: R$ "))
            conta.sacar(valor)

        elif opcao == 'e':
            conta.exibir_extrato()

        elif opcao == 'q':
            print("👋 Obrigado por usar o sistema bancário. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

# Executa a função principal
if __name__ == "__main__":
    main()
