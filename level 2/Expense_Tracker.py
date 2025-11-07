import json
from datetime import datetime
import os

gastos = []

def adicionar_despesa():
    global gastos

    despesa = input("O que vai gastar?: ")
    descricao = input("O que você fara?: ")
    
    try:
        valor = float(input("Qual é o valor?: "))
        if valor <= 0:
            print("⚠️ O valor deve ser maior que zero!")
            return
    except ValueError:
        print("⚠️ Valor inválido! Digite um número.")
        return

    categoria = input("Qual é a categoria?: ")
    data = input("Para a data: ")

    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    novo_id = len(gastos) + 1

    novo_gasto = {
        "id": novo_id,
        "despesa": despesa,
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "data_criacao": data_criacao
    }

    gastos.append(novo_gasto)
    salvar_dados()

    print(f"\n✅ Gasto '{despesa}' adicionado com sucesso!")
    print(f"💰 Valor: R$ {valor:.2f} | Categoria: {categoria} | Data: {data}")
    print(f"🕓 Criado em: {data_criacao}")


def mostrar_despesas():
    global gastos

    if not gastos:
        print("\n📭 Sua lista está vazia.\n")

    else:
        print("\n📋 Itens na lista:\n")
        total = 0

        for gasto in gastos:
            print(f"🆔 {gasto['id']} | {gasto['despesa']} - R$ {gasto['valor']:.2f}")
            print(f"📝 Descrição: {gasto['descricao']}")
            print(f"📂 Categoria: {gasto['categoria']}")
            print(f"📅 Data: {gasto['data']} | Criado em: {gasto['data_criacao']}")
            print("-" * 40)

            total += gasto["valor"]

    print(f"\n💰 Total geral: R$ {total:.2f}\n")

def total_por_categoria():
    global gastos

    if not gastos:
        print("\n📭 Nenhuma despesa cadastrada.\n")
        return

    # Dicionário para armazenar os totais de cada categoria
    categorias = {}

    # Percorre cada gasto e soma por categoria
    for gasto in gastos:
        categoria = gasto["categoria"]
        valor = gasto["valor"]

        # Se a categoria ainda não existe, cria com valor inicial 0
        if categoria not in categorias:
            categorias[categoria] = 0

        # Soma o valor do gasto na categoria correspondente
        categorias[categoria] += valor

    # Exibe o total de cada categoria formatado
    print("\n📊 TOTAL POR CATEGORIA:\n")
    for categoria, total in categorias.items():
        print(f"📂 {categoria}: R$ {total:.2f}")

    print("-" * 40)

def remover_despesa():
    global gastos

    try:
        id_digitado = int(input("Qual item de gasto da lista você quer excluir?(Digite o ID): "))

        for gasto in gastos:
            if gasto["id"] == id_digitado:
                gastos.remove(gasto)
                atualizar_ids()
                salvar_dados()
                print(f"\n🗑️ Despesa removida: {gasto['despesa']}\n")
                break
        else:
            print("\n⚠️ ID não encontrado.\n")

    except ValueError:
        print("\n⚠️ Digite um número válido.\n")

def salvar_dados():
    global gastos
    try:
        with open("despesas.json", "w", encoding="utf-8") as gasto:
            json.dump(gastos, gasto, indent=4, ensure_ascii=False)
       
    except Exception as erro:
        print(f"⚠️ Erro ao salvar os dados: {erro}")

def atualizar_ids():
    global gastos
    for indice, gasto in enumerate(gastos, start=1):
        gasto["id"] = indice

def carregar_dados():
    global gastos

    try:
        with open("despesas.json", "r", encoding="utf-8") as despesa:
            gastos = json.load(despesa)
            print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("📁 Nenhum arquivo encontrado. Criando novo banco de contas...")
        gastos = []
    except json.JSONDecodeError:
        print("⚠️ Erro ao ler o arquivo JSON. Criando lista vazia...")
        gastos = []

def menu_principal():

    carregar_dados()
    while True:
        print("==== RASTREADOR DE GASTOS ====")
        print("[A] Adicionar despesa")
        print("[V] Ver despesas")
        print("[T] Total por categoria")
        print("[R] Remover despesa")
        print("[S] Sair")

        try:

            opcao = input("\nEscolha uma opção: ").upper()

            if opcao == "A":
                adicionar_despesa()
            elif opcao == "V":
                mostrar_despesas()
            elif opcao == "T":
                total_por_categoria()
            elif opcao == "R":
                remover_despesa()
            elif opcao == "S":
                salvar_dados()
                os.system('cls' if os.name == 'nt' else 'clear')
                print("💾 Dados salvos com sucesso! Até mais 👋")
                break

            else:
                print("⚠️ Opção inválida! Tente novamente.")

        except ValueError:
            print("\n⚠️ Digite um valor válido.\n")

menu_principal()