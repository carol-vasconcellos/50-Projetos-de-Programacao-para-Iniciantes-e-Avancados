import json

lista_contas = []

def criar_conta():
    global lista_contas

    usuario = input("Insira seu nome completo: ")

    numero_base = len(lista_contas) + 1
    numero_formatado = str(numero_base).zfill(5)
    numero_conta_final = f"{numero_formatado}-0"

    nova_conta = {
        "nome": usuario,
        "conta": numero_conta_final,
        "saldo": 0
    }

    lista_contas.append(nova_conta)
    salvar_dados()

    print("\n--- ✅ Conta Criada com Sucesso! ---")
    print(f"Usuário: {nova_conta['nome']}")
    print(f"Número da Conta: {nova_conta['conta']}")
    print(f"Saldo: R$ {nova_conta['saldo']:.2f}")
    print("-------------------------------------")


def depositar():
    global lista_contas

    numero_conta = input("Digite o número da conta (com o dígito): ")

    conta_encontrada = None
    for conta in lista_contas:
        if conta["conta"] == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada is None:
        print("❌ Conta não encontrada. Verifique o número e tente novamente.")
        return

    try:
        valor = float(input(f"Digite o valor que deseja depositar para {conta_encontrada['nome']}: R$ "))
    except ValueError:
        print("⚠️ Valor inválido! Digite um número.")
        return

    if valor <= 0:
        print("⚠️ O valor deve ser maior que zero!")
        return

    conta_encontrada["saldo"] += valor
    salvar_dados()

    print("\n--- 💰 Depósito Realizado com Sucesso ---")
    print(f"Titular: {conta_encontrada['nome']}")
    print(f"Conta: {conta_encontrada['conta']}")
    print(f"Valor depositado: R$ {valor:.2f}")
    print(f"Novo saldo: R$ {conta_encontrada['saldo']:.2f}")
    print("-----------------------------------------")


def sacar():
    global lista_contas

    numero_conta = input("Digite o número da conta (com o dígito): ")

    conta_encontrada = None
    for conta in lista_contas:
        if conta["conta"] == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada is None:
        print("❌ Conta não encontrada. Verifique o número e tente novamente.")
        return

    try:
        valor = float(input(f"Digite o valor que deseja sacar para {conta_encontrada['nome']}: R$ "))
    except ValueError:
        print("⚠️ Valor inválido! Digite um número.")
        return

    if valor <= 0:
        print("⚠️ O valor deve ser maior que zero!")
        return

    if valor > conta_encontrada["saldo"]:
        print("❌ Saldo insuficiente para o saque!")
        return

    conta_encontrada["saldo"] -= valor
    salvar_dados()

    print("\n--- 💸 Saque Realizado com Sucesso ---")
    print(f"Titular: {conta_encontrada['nome']}")
    print(f"Conta: {conta_encontrada['conta']}")
    print(f"Valor sacado: R$ {valor:.2f}")
    print(f"Novo saldo: R$ {conta_encontrada['saldo']:.2f}")
    print("---------------------------------------")


def mostrar_saldo():
    global lista_contas

    numero_conta = input("Digite o número da conta (com o dígito): ")

    conta_encontrada = None
    for conta in lista_contas:
        if conta["conta"] == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada is None:
        print("❌ Conta não encontrada. Verifique o número e tente novamente.")
        return

    print("\n--- 📊 Informações da Conta ---")
    print(f"Titular: {conta_encontrada['nome']}")
    print(f"Número da Conta: {conta_encontrada['conta']}")
    print(f"Saldo Atual: R$ {conta_encontrada['saldo']:.2f}")
    print("--------------------------------")

def salvar_dados():
    global lista_contas
    try:
        with open("contas.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_contas, arquivo, indent=4, ensure_ascii=False)
        print("💾 Dados salvos com sucesso!")
    except Exception as erro:
        print(f"⚠️ Erro ao salvar os dados: {erro}")

def carregar_dados():
    global lista_contas
    try:
        with open("contas.json", "r", encoding="utf-8") as arquivo:
            lista_contas = json.load(arquivo)
        print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("📁 Nenhum arquivo de dados encontrado. Criando novo banco de contas...")
        lista_contas = []
    except json.JSONDecodeError:
        print("⚠️ Erro ao ler o arquivo JSON. Criando lista vazia...")
        lista_contas = []

def menu_principal():
    while True:
        escolha_usuario = input(
            "\nEscolha uma opção:\n"
            "[C] Criar conta\n"
            "[D] Depositar\n"
            "[S] Sacar\n"
            "[M] Mostrar saldo\n"
            "[SA] Sair\n"
            "Opção: "
        ).upper()

        if escolha_usuario == "C":
            criar_conta()
        elif escolha_usuario == "D":
            depositar()
        elif escolha_usuario == "S":
            sacar()
        elif escolha_usuario == "M":
            mostrar_saldo()
        elif escolha_usuario == "SA":
            print("Obrigado por nos escolher. Até breve!! 👋")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

carregar_dados()
menu_principal()
