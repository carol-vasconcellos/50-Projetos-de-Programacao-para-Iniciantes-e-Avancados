import json
from datetime import datetime
import os

lista_add = []

def adicionar_lista():
    global lista_add

    add = input("Insira um item à sua lista: ")


    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    novo_id = len(lista_add) + 1

    nova_lista = {
        "id": novo_id,
        "item": add,
    }

    lista_add.append(nova_lista)
    salvar_dados()

    print(f"\n✅ Item '{add}' adicionado com sucesso!")
    print(f"🕓 Criado em: {data_criacao}")

def apagar_item_lista():
    global lista_add

    try:
        id_digitado = int(input("Qual ID deseja excluir? "))

        for item in lista_add:
            if item["id"] == id_digitado:
                lista_add.remove(item)
                atualizar_ids()
                salvar_dados()
                print(f"\n🗑️ Item removido: {item['item']}\n")
                break
        else:
            print("\n⚠️ ID não encontrado.\n")

    except ValueError:
        print("\n⚠️ Digite um número válido.\n")

def salvar_dados():
    global lista_add
    try:
        with open("contas.json", "w", encoding="utf-8") as lista:
            json.dump(lista_add, lista, indent=4, ensure_ascii=False)
        print("💾 Dados salvos com sucesso!")
    except Exception as erro:
        print(f"⚠️ Erro ao salvar os dados: {erro}")

def mostrar_lista():
    global lista_add

    if not lista_add:
        print("\n📭 Sua lista está vazia.\n")
    else:
        print("\n📋 Itens na lista:\n")
        for item in lista_add:
            print(f"🆔 {item['id']} - {item['item']}  \nCriado em: {item['data']}  \nPrazo para: {item['prazo']}\n")
        print()

def atualizar_ids():
    global lista_add
    for indice, item in enumerate(lista_add, start=1):
        item["id"] = indice

def carregar_dados():
    global lista_add
    try:
        with open("contas.json", "r", encoding="utf-8") as lista:
            lista_add = json.load(lista)
        print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("📁 Nenhum arquivo encontrado. Criando novo banco de contas...")
        lista_add = []
    except json.JSONDecodeError:
        print("⚠️ Erro ao ler o arquivo JSON. Criando lista vazia...")
        lista_add = []

def main():
    while True:
        print("\n====BEM-VINDO A SUA LISTA DE COMPRAS====")
        print("\n=== MENU ===")
        print("1️⃣ - Adicionar item")
        print("2️⃣ - Remover item")
        print("3️⃣ - Mostrar lista")
        print("4️⃣ - Sair")

        try:
            opcao = int(input("Qual opção escolhe: "))

            if opcao == 1:
                adicionar_lista()
            elif opcao == 2:
                apagar_item_lista()
            elif opcao == 3:
                mostrar_lista()
            elif opcao == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Volte sempre!!!")
                break
                
            else:
                print("\n⚠️ Opção inválida.\n")

        except ValueError:
            print("\n⚠️ Digite um número válido.\n")

carregar_dados()
main()
