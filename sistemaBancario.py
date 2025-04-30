import datetime

# Variáveis globais
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

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

# Função para realizar o depósito
def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"{datetime.datetime.now()} - Depósito: +R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Valor inválido para depósito.")

# Função para realizar o saque
def sacar(valor):
    global saldo, limite, numero_saques, extrato
    if numero_saques >= LIMITE_SAQUES:
        print("❌ Limite diário de saques atingido.")
        return

    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print("❌ Valor do saque excede o limite por operação.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"{datetime.datetime.now()} - Saque: -R$ {valor:.2f}")
        print("✅ Saque realizado com sucesso.")
    else:
        print("❌ Valor inválido para saque.")

# Função para exibir o extrato
def exibir_extrato():
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================")

# Função principal
def main():
    global saldo, numero_saques

    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: R$ "))
            depositar(valor)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: R$ "))
            sacar(valor)

        elif opcao == 'e':
            exibir_extrato()

        elif opcao == 'q':
            print("👋 Obrigado por usar o sistema bancário. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

# Executa a função principal
if __name__ == "__main__":
    main()
