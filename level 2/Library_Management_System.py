import json

lista_livros = []

def inserir_livro():
    global lista_livros

    titulo = input("Insira o titulo: ")
    autor = input("Insira o autor: ")
    ano = input("Insira o ano: ")
    status = "disponível"

    novo_id = len(lista_livros) + 1

    novo_livro = {
        "id": novo_id,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": status
    }

    lista_livros.append(novo_livro)
    salvar_dados()

    print("\n--- ✅ Livro Adicionado com Sucesso! ---")
    print(f"Título: {novo_livro['titulo']}")
    print(f"Autor: {novo_livro['autor']}")
    print(f"Ano: {novo_livro['ano']}")
    print(f"Status: {novo_livro['status']}")
    print("-------------------------------------")


def atualizar_ids():
    global lista_livros
    for indice, livro in enumerate(lista_livros, start=1):
        livro["id"] = indice

def mostrar_livro():
    global lista_livros

    livro_digitado = input("Digite 'todos' para ver os livros disponiveis:  ").lower()
    if livro_digitado == "todos":
        print("\n📚 Lista de todos os livros:\n")
        for livro in lista_livros:
            print(f"📘 {livro['id']} - {livro['titulo']} — {livro['status']}")
            print("--------------------------------")
        return


    livro_encontrado = None
    for livro in lista_livros:
        if livro["titulo"] == livro_digitado:
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        print("❌ Livro não encontrado. Verifique o título e tente novamente.")
        return

    print("\n--- 📊 Informações do Livro ---")
    print(f"Título: {livro_encontrado['titulo']}")
    print(f"Autor: {livro_encontrado['autor']}")
    print(f"Ano: {livro_encontrado['ano']}")
    print(f"Status: {livro_encontrado['status']}")
    print("--------------------------------")


def remover_livro():
    global lista_livros

    try:
        id_digitado = int(input("Qual item de gasto da lista você quer excluir?(Digite o ID): "))

        for livro in lista_livros:
            if livro["id"] == id_digitado:
                lista_livros.remove(livro)
                atualizar_ids()
                salvar_dados()
                print(f"\n🗑️ Livro removido: {livro['titulo']}\n")
                break
        else:
            print("\n⚠️ ID não encontrado.\n")

    except ValueError:
        print("\n⚠️ Digite um número válido.\n")

def emprestar_livro():
    global lista_livros

    try:
        pergunta = input("📚 Qual livro você quer emprestar?: ").strip()

        if not pergunta:
            print("⚠️ Você precisa digitar o título do livro.")
            return

        livro_encontrado = False

        for livro in lista_livros:
            if pergunta.lower() == livro["titulo"].lower():
                livro_encontrado = True
                if livro["status"] == "disponível":
                    livro["status"] = "não disponível"
                    salvar_dados()
                    print(f"\n📕 Livro '{livro['titulo']}' emprestado com sucesso!")
                    print("Agora ele está marcado como não disponível.")
                else:
                    print(f"\n⚠️ O livro '{livro['titulo']}' já foi emprestado.")
                break

        if not livro_encontrado:
            print("❌ Livro não encontrado. Verifique o título e tente novamente.")

    except Exception as erro:
        print(f"⚠️ Ocorreu um erro inesperado ao emprestar o livro: {erro}")

def devolver_livro():
    global lista_livros

    try:
        pergunta = input("📗 Qual livro você quer devolver?: ").strip()

        if not pergunta:
            print("⚠️ Você precisa digitar o título do livro.")
            return

        livro_encontrado = False

        for livro in lista_livros:
            if pergunta.lower() == livro["titulo"].lower():
                livro_encontrado = True
                if livro["status"] == "não disponível":
                    livro["status"] = "disponível"
                    salvar_dados()
                    print(f"\n📗 Livro '{livro['titulo']}' devolvido com sucesso!")
                    print("Agora ele está novamente disponível para empréstimo.")
                else:
                    print(f"\n⚠️ O livro '{livro['titulo']}' já está disponível.")
                break

        if not livro_encontrado:
            print("❌ Livro não encontrado. Verifique o título e tente novamente.")

    except Exception as erro:
        print(f"⚠️ Ocorreu um erro inesperado ao devolver o livro: {erro}")


def salvar_dados():
    global lista_livros
    try:
        with open("biblioteca.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_livros, arquivo, indent=4, ensure_ascii=False)
        print("💾 Dados salvos com sucesso!")
    except Exception as erro:
        print(f"⚠️ Erro ao salvar os dados: {erro}")

def carregar_dados():
    global lista_livros
    try:
        with open("biblioteca.json", "r", encoding="utf-8") as arquivo:
            lista_livros = json.load(arquivo)
        print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("📁 Nenhum arquivo de dados encontrado. Criando novo banco de livros...")
        lista_livros = []
    except json.JSONDecodeError:
        print("⚠️ Erro ao ler o arquivo JSON. Criando lista vazia...")
        lista_livros = []

def menu_principal():
    while True:
        escolha_usuario = input(
            "\n=== SISTEMA DE BIBLIOTECA ===\n"
            "[A] Adicionar livro\n"
            "[V] Ver livros\n"
            "[E] Emprestar livro\n"
            "[D] Devolver livro\n"
            "[R] Remover livro\n"
            "[S] Sair\n"
            "Opção: "
        ).upper()

        if escolha_usuario == "A":
            inserir_livro()
        elif escolha_usuario == "V":
            mostrar_livro()
        elif escolha_usuario == "E":
            emprestar_livro()
        elif escolha_usuario == "D":
            devolver_livro()
        elif escolha_usuario == "R":
            remover_livro()
        elif escolha_usuario == "S":
            print("Obrigado por nos escolher. Até breve!! 👋")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

carregar_dados()
menu_principal()