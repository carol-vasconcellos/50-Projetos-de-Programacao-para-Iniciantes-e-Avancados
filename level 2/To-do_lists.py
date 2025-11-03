import os 
import json

favoritos = {
    "filmes": [],
    "músicas": [],
    "livros": [],
    "comidas": [],
    "jogos": []
}

def salvar_dados():
    global favoritos
    try:
        with open("favoritos.json", "w", encoding="utf-8") as arquivo:
            json.dump(favoritos, arquivo, indent=4, ensure_ascii=False)
        print("💾 Dados salvos com sucesso!")
    except Exception as erro:
        print(f"⚠️ Erro ao salvar os dados: {erro}")

def mostrar_lista():
    global favoritos

    print("\n📋 LISTA DE FAVORITOS\n")

    for categoria, itens in favoritos.items():
        print(f"💖 {categoria.capitalize()}:")
        if itens:
            for i, item in enumerate(itens, start=1):
                print(f"  {i}. {item}")
        else:
            print("  🌸 Nenhum item ainda.\n")


def carregar_dados():
    global favoritos
    try:
        with open("favoritos.json", "r", encoding="utf-8") as arquivo:
            favoritos = json.load(arquivo)
        print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("📁 Nenhum arquivo encontrado. Criando novo banco de favoritos...")
        favoritos = {
            "filmes": [],
            "músicas": [],
            "livros": [],
            "comidas": [],
            "jogos": []
        }
    except json.JSONDecodeError:
        print("⚠️ Erro ao ler o arquivo JSON. Criando lista vazia...")
        favoritos = {
            "filmes": [],
            "músicas": [],
            "livros": [],
            "comidas": [],
            "jogos": []
        }

def main():  
    global favoritos

    carregar_dados()

    while True:
        print("\n==== BEM-VINDO À SUA LISTA DE FAVORITOS ====")
        print("\n=== MENU ===")
        print("[A] - Adicionar item")
        print("[R] - Remover item")
        print("[M] - Mostrar lista")
        print("[S] - Sair")

        opcao = input("Qual opção escolhe: ").upper()

        if opcao == 'A':
            categoria = input("Digite a categoria (filmes, músicas, livros, comidas, jogos): ").lower()
            if categoria not in favoritos:
                print("⚠️ Categoria inválida!")
                continue

            item = input(f"Digite o nome do seu favorito em {categoria}: ").strip().capitalize()
            if item in favoritos[categoria]:
                print("⚠️ Esse item já está na sua lista!")
            else:
                favoritos[categoria].append(item)
                print(f"💖 '{item}' adicionado em {categoria}!")
                salvar_dados()
        
        elif opcao == 'R':
            categoria = input("De qual categoria deseja remover? ").lower()
            if categoria not in favoritos:
                print("⚠️ Categoria inválida!")
                continue

            item = input(f"Digite o nome do item que deseja remover de {categoria}: ").strip().capitalize()
            if item in favoritos[categoria]:
                favoritos[categoria].remove(item)
                print(f"🗑️ '{item}' removido com sucesso de {categoria}.")
                salvar_dados()
            else:
                print("❌ Esse item não está nessa categoria.")

        elif opcao == 'M':
            mostrar_lista()
        elif opcao == 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("💾 Dados salvos com sucesso!")
            salvar_dados()
            print("💖 Volte sempre!")
            break
                
        else:
            print("\n⚠️ Opção inválida.\n")

main()
