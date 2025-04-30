import datetime

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def menu():
    print("""
========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================
""")

while True:
    menu()
    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"{datetime.datetime.now()} - Depósito: +R$ {valor:.2f}")
            print("✅ Depósito realizado com sucesso.")
        else:
            print("❌ Valor inválido para depósito.")

    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print("❌ Limite diário de saques atingido.")
            continue

        valor = float(input("Informe o valor do saque: R$ "))
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

    elif opcao == 'e':
        print("\n========== EXTRATO ==========")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for operacao in extrato:
                print(operacao)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == 'q':
        print("👋 Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
