menu = """

[u] Criar Usuário
[c] Criar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = {}
contas = {}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "u":
        cpf = input("Informe o CPF (somente números): ")
        if cpf in usuarios:
            print("Usuário já cadastrado.")
        else:
            nome = input("Informe o nome: ")
            usuarios[cpf] = nome
            print(f"Usuário {nome} criado com sucesso.")

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        if cpf not in usuarios:
            print("Usuário não encontrado.")
        else:
            numero_conta = len(contas) + 1
            contas[numero_conta] = {"cpf": cpf, "saldo": 0, "extrato": ""}
            print(f"Conta corrente {numero_conta} criada com sucesso para o usuário {usuarios[cpf]}.")

    elif opcao == "d":
        numero_conta = int(input("Informe o número da conta: "))
        if numero_conta not in contas:
            print("Conta não encontrada.")
        else:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                contas[numero_conta]["saldo"] += valor
                contas[numero_conta]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        numero_conta = int(input("Informe o número da conta: "))
        if numero_conta not in contas:
            print("Conta não encontrada.")
        else:
            valor = float(input("Informe o valor do saque: "))
            saldo = contas[numero_conta]["saldo"]
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                contas[numero_conta]["saldo"] -= valor
                contas[numero_conta]["extrato"] += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        numero_conta = int(input("Informe o número da conta: "))
        if numero_conta not in contas:
            print("Conta não encontrada.")
        else:
            print("\n================ EXTRATO ================")
            extrato = contas[numero_conta]["extrato"]
            print("Não foram realizadas movimentações." if not extrato else extrato)
            saldo = contas[numero_conta]["saldo"]
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
