import json
from datetime import datetime
import os

receitas = []

def add_receita():
    global receitas

    nome = input("🍽️ Nome da receita: ").strip()
    ingredientes = input("🧂 Ingredientes (separe por vírgula): ").strip()
    modo_preparo = input("📘 Como preparar?: ").strip()
    categoria = input("📂 Categoria: ").strip()
    tempo = input("⏱️ Tempo de preparo: ").strip()
    dificuldade = input("🎯 Dificuldade: ").strip()

    if not nome:
        print("⚠️ O nome não pode ser vazio.")
        return

    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    novo_id = len(receitas) + 1

    nova_receita = {
        "id": novo_id,
        "nome": nome,
        "ingredientes": ingredientes.split(","),   # vira lista
        "modo_preparo": modo_preparo,
        "categoria": categoria,
        "tempo": tempo,
        "dificuldade": dificuldade,
        "data_criacao": data_criacao
    }

    receitas.append(nova_receita)
    salvar_dados()
    print(f"\n✅ Receita '{nome}' adicionada com sucesso!\n")

def ver_receita():
    global receitas

    if not receitas:
        print("\n📭 Nenhuma receita cadastrada.\n")
        return

    print("\n=== 📚 TODAS AS RECEITAS ===\n")

    for receita in receitas:
        print(f"🆔 {receita['id']} | {receita['nome']}")
        print(f"🧂 Ingredientes: {', '.join(receita['ingredientes'])}")
        print(f"📘 Modo de preparo: {receita['modo_preparo']}")
        print(f"📂 Categoria: {receita['categoria']}")
        print(f"⏱️ Tempo: {receita['tempo']}")
        print(f"🎯 Dificuldade: {receita['dificuldade']}")
        print(f"📅 Criado em: {receita['data_criacao']}")
        print("-" * 40)

def buscar_receita():
    global receitas
    termo = input("🔍 Buscar receita por nome ou categoria: ").lower().strip()

    encontrados = [
        r for r in receitas 
        if termo in r["nome"].lower() or termo in r["categoria"].lower()
    ]

    if not encontrados:
        print("❌ Nenhuma receita encontrada.")
        return

    print("\n=== 🔍 RESULTADOS ===\n")
    for receita in encontrados:
        print(f"🆔 {receita['id']} | {receita['nome']}")
        print(f"📂 Categoria: {receita['categoria']}")
        print("-" * 40)

def remover_receitas():
    global receitas

    try:
        remove = int(input("🗑️ ID da receita que deseja remover: "))
    except ValueError:
        print("⚠️ Digite um número válido.")
        return

    for r in receitas:
        if r["id"] == remove:
            receitas.remove(r)
            atualizar_ids()
            salvar_dados()
            print(f"🗑️ Receita '{r['nome']}' removida com sucesso!")
            return

    print("❌ ID não encontrado.")

def salvar_dados():
    global receitas
    with open("receitas.json", "w", encoding="utf-8") as arquivo:
        json.dump(receitas, arquivo, indent=4, ensure_ascii=False)

def atualizar_ids():
    global receitas
    for indice, receita in enumerate(receitas, start=1):
        receita["id"] = indice

def carregar_dados():
    global receitas
    try:
        with open("receitas.json", "r", encoding="utf-8") as arquivo:
            receitas = json.load(arquivo)
            print("📂 Dados carregados!")
    except:
        receitas = []

def main():
    carregar_dados()
    
    while True:
        print("\n=== 🍲 RECIPE BOOK ===")
        print("[A] Adicionar receita")
        print("[V] Ver todas as receitas")
        print("[B] Buscar receita")
        print("[R] Remover receita")
        print("[S] Sair")

        opcao = input("\nEscolha uma opção: ").upper()

        if opcao == "A":
            add_receita()
        elif opcao == "V":
            ver_receita()
        elif opcao == "B":
            buscar_receita()
        elif opcao == "R":
            remover_receitas()
        elif opcao == "S":
            salvar_dados()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("👋 Até mais!")
            break
        else:
            print("⚠️ Opção inválida!")

main()
