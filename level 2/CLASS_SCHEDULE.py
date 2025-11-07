import json
from datetime import datetime
import os

aulas_agendadas = []

def adicionar_aula():
    global aulas_agendadas

    add = input("Qual aula quer adicionar?: ")


    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    novo_id = len(aulas_agendadas) + 1

    horario = input("Qual o horário da aula?(00:00 - 24h): ")
    data = input("Qual o data da aula?(00/00/0000): ")

    nova_aula = {
        "id": novo_id,
        "aula": add,
        "horario": horario,
        "data": data,
        "criado_em": data_criacao
    }

    aulas_agendadas.append(nova_aula)
    salvar_dados()

    print(f"\n✅ Aula '{add} no horário de {horario}', na data de {data} adicionada com sucesso!")
    print(f"🕓 Criado em: {data_criacao}")

def apagar_item_lista():
    global aulas_agendadas

    try:
        id_digitado = int(input("Qual aula deseja excluir(coloque o ID)? "))

        for aula in aulas_agendadas:
            if aula["id"] == id_digitado:
                aulas_agendadas.remove(aula)
                atualizar_ids()
                salvar_dados()
                print(f"\n🗑️ Aula removida: {aula['aula']}\n")
                break
        else:
            print("\n⚠️ ID não encontrado.\n")

    except ValueError:
        print("\n⚠️ Digite um número válido.\n")

def salvar_dados():
    global aulas_agendadas
    try:
        with open("aulas.json", "w", encoding="utf-8") as aula:
            json.dump(aulas_agendadas, aula, indent=4, ensure_ascii=False)
        print("💾 Dados salvos com sucesso!")
    except Exception as erro:
        print(f"⚠️ Erro ao salvar os dados: {erro}")

def mostrar_lista():
    global aulas_agendadas

    if not aulas_agendadas:
        print("\n📭 Sua lista está vazia.\n")
    else:
        print("\n📋 Itens na lista:\n")
        for aula in aulas_agendadas:
            print(f"🆔 {aula['id']} - {aula['aula']} 🕒 Horário: {aula['horario']} Data : {aula['data']}")
        print()

def atualizar_ids():
    global aulas_agendadas
    for indice, aula in enumerate(aulas_agendadas, start=1):
        aula["id"] = indice

def carregar_dados():
    global aulas_agendadas
    try:
        with open("aulas.json", "r", encoding="utf-8") as aula:
            aulas_agendadas = json.load(aula)
        print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("📁 Nenhum arquivo encontrado. Criando novo banco de contas...")
        aulas_agendadas = []
    except json.JSONDecodeError:
        print("⚠️ Erro ao ler o arquivo JSON. Criando lista vazia...")
        aulas_agendadas = []

def main():
    while True:
        print("\n====AGENDA DE AULAS====")
        print("[A] Adicionar aula")
        print("[V] Ver agenda ")
        print("[R] Remover aula ")
        print("[S] Sair")

        try:
            opcao = input("Qual opção escolhe: ").upper()

            if opcao == 'A':
                adicionar_aula()
            elif opcao == 'R':
                apagar_item_lista()
            elif opcao == 'V':
                mostrar_lista()
            elif opcao == 'S':
                salvar_dados()
                os.system('cls' if os.name == 'nt' else 'clear')
                print("💾 Dados salvos com sucesso!")
                print("Volte sempre!!!")
                break

                
            else:
                print("\n⚠️ Opção inválida.\n")

        except ValueError:
            print("\n⚠️ Digite um valor válido.\n")

carregar_dados()
main()