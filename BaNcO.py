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
LIMITE_SAQUES = 5
limite = 800

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if cpf in usuarios:
        print("Usuário já cadastrado.")
    else:
        nome = input("Informe o nome: ")
        usuarios[cpf] = nome
        print(f"Usuário {nome} criado com sucesso.")

def criar_conta_corrente():
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios:
        print("Usuário não encontrado.")
    else:
        numero_conta = len(contas) + 1
        contas[numero_conta] = {"cpf": cpf, "saldo": 0, "extrato": "", "numero_saques": 0}
        print(f"Conta corrente {numero_conta} criada com sucesso para o usuário {usuarios[cpf]}.")

def depositar():
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

def sacar():
    numero_conta = int(input("Informe o número da conta: "))
    if numero_conta not in contas:
        print("Conta não encontrada.")
    else:
        valor = float(input("Informe o valor do saque: "))
        saldo = contas[numero_conta]["saldo"]
        numero_saques = contas[numero_conta]["numero_saques"]
        
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
            contas[numero_conta]["numero_saques"] += 1
            print("Saque realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

def extrato():
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

while True:
    opcao = input(menu)

    if opcao == "u":
        criar_usuario()
    elif opcao == "c":
        criar_conta_corrente()
    elif opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
