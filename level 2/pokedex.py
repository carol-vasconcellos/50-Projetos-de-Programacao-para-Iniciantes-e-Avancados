import json
from datetime import datetime
import os

pokedex = []

def adicionar_pokemon():
    global pokedex

    nome = input("Nome do Pokémon: ").strip().capitalize()
    tipo = input("Tipo (ex: fogo, água, grama): ").strip().capitalize()
    descricao = input("Descrição: ").strip()
    altura = input("Altura (ex: 0.7m): ").strip()
    peso = input("Peso (ex: 9kg): ").strip()

    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    novo_id = len(pokedex) + 1

    pokemon = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "altura": altura,
        "peso": peso,
        "data_criacao": data_criacao
    }
    
    pokedex.append(pokemon)
    salvar_dados()

    print(f"\n✅ Pokémon '{nome}' adicionado com sucesso!")
    print(f"🕓 Criado em: {data_criacao}")


def remover_pokemon():
    global pokedex

    try:
        remove = int(input("🗑️ ID do Pokémon que deseja remover: "))
    except ValueError:
        print("⚠️ Digite um número válido.")
        return

    for p in pokedex:
        if p["id"] == remove:
            pokedex.remove(p)
            atualizar_ids()
            salvar_dados()
            print(f"🗑️ Pokémon '{p['nome']}' removido com sucesso!")
            return

    print("❌ ID não encontrado.")


def mostrar_pokemon():
    global pokedex

    if not pokedex:
        print("\n📭 Nenhum Pokémon cadastrado.\n")
        return

    print("\n=== 📚 TODOS OS POKÉMON ===\n")

    for p in pokedex:
        print(f"🆔 {p['id']} | {p['nome']}")
        print(f"🔥 Tipo: {p['tipo']}")
        print(f"📘 Descrição: {p['descricao']}")
        print(f"📏 Altura: {p['altura']}")
        print(f"⚖️ Peso: {p['peso']}")
        print(f"📅 Criado em: {p['data_criacao']}")
        print("-" * 40)


def buscar_pokemon():
    global pokedex

    termo = input("🔍 Buscar Pokémon por nome ou tipo: ").lower().strip()

    encontrados = [
        p for p in pokedex
        if termo in p["nome"].lower() or termo in p["tipo"].lower()
    ]

    if not encontrados:
        print("❌ Nenhum Pokémon encontrado.")
        return

    print("\n=== 🔍 RESULTADOS ===\n")
    for p in encontrados:
        print(f"🆔 {p['id']} | {p['nome']} ({p['tipo']})")


def salvar_dados():
    global pokedex
    with open("pokedex.json", "w", encoding="utf-8") as arquivo:
        json.dump(pokedex, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
    global pokedex

    try:
        with open("pokedex.json", "r", encoding="utf-8") as arquivo:
            pokedex = json.load(arquivo)
            print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        pokedex = []


def atualizar_ids():
    global pokedex
    for indice, p in enumerate(pokedex, start=1):
        p["id"] = indice


def main():
    carregar_dados()

    while True:
        print("\n==== 🧩 POKÉDEX ====")
        print("[A] Adicionar Pokémon")
        print("[R] Remover Pokémon")
        print("[M] Mostrar Pokédex")
        print("[B] Buscar Pokémon")
        print("[S] Sair")

        opcao = input("Escolha uma opção: ").upper()

        if opcao == 'A':
            adicionar_pokemon()
        elif opcao == 'R':
            remover_pokemon()
        elif opcao == 'M':
            mostrar_pokemon()
        elif opcao == 'B':
            buscar_pokemon()
        elif opcao == 'S':
            salvar_dados()
            print("💾 Dados salvos! Até mais 👋")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")


main()
