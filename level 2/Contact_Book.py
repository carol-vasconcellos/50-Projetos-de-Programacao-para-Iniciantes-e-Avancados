import json
import os

contatos = []


def salvar_dados():
    global contatos
    try:
        with open("contatos.json", "w", encoding="utf-8") as arquivo:
            json.dump(contatos, arquivo, indent=4, ensure_ascii=False)
        print("💾 Dados salvos com sucesso!")
    except Exception as erro:
        print(f"⚠️ Erro ao salvar os dados: {erro}")


def carregar_dados():
    global contatos
    try:
        with open("contatos.json", "r", encoding="utf-8") as arquivo:
            contatos = json.load(arquivo)
        print("📂 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("📁 Nenhum arquivo encontrado. Criando novo banco de contatos...")
        contatos = []
    except json.JSONDecodeError:
        print("⚠️ Erro ao ler o arquivo JSON. Criando lista vazia...")
        contatos = []


def adicionar_contato():
    global contatos
    nome = input("👤 Nome completo: ").strip().capitalize()
    telefone = input("📞 Telefone: ").strip()
    email = input("✉️ E-mail: ").strip().lower()
    empresa = input("🏢 Empresa: ").strip().capitalize()

    novo_id = len(contatos) + 1
    novo_contato = {
        "id": novo_id,
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "empresa": empresa
    }

    contatos.append(novo_contato)
    salvar_dados()
    print(f"\n✅ Contato '{nome}' adicionado com sucesso!\n")


def ver_contatos():
    global contatos
    if not contatos:
        print("\n📭 Nenhum contato salvo ainda.\n")
        return

    print("\n=== LISTA DE CONTATOS ===\n")
    for contato in contatos:
        print(f"🆔 {contato['id']}")
        print(f"👤 Nome: {contato['nome']}")
        print(f"📞 Telefone: {contato['telefone']}")
        print(f"✉️ E-mail: {contato['email']}")
        print(f"🏢 Empresa: {contato['empresa']}")
        print("-" * 40)


def buscar_contato():
    global contatos
    termo = input("🔍 Buscar por nome ou empresa: ").strip().lower()

    encontrados = [c for c in contatos if termo in c["nome"].lower() or termo in c["empresa"].lower()]

    if not encontrados:
        print("❌ Nenhum contato encontrado.")
        return

    print("\n📋 RESULTADOS DA BUSCA:\n")
    for contato in encontrados:
        print(f"👤 {contato['nome']} | 📞 {contato['telefone']} | 🏢 {contato['empresa']}")
    print("-" * 40)


def editar_contato():
    global contatos
    try:
        id_digitado = int(input("✏️ Digite o ID do contato que deseja editar: "))
        contato = next((c for c in contatos if c["id"] == id_digitado), None)

        if not contato:
            print("❌ Contato não encontrado.")
            return

        print(f"\nEditando contato: {contato['nome']}")
        novo_nome = input(f"Novo nome ({contato['nome']}): ") or contato["nome"]
        novo_telefone = input(f"Novo telefone ({contato['telefone']}): ") or contato["telefone"]
        novo_email = input(f"Novo e-mail ({contato['email']}): ") or contato["email"]
        nova_empresa = input(f"Nova empresa ({contato['empresa']}): ") or contato["empresa"]

        contato.update({
            "nome": novo_nome,
            "telefone": novo_telefone,
            "email": novo_email,
            "empresa": nova_empresa
        })

        salvar_dados()
        print("✅ Contato atualizado com sucesso!")

    except ValueError:
        print("⚠️ Digite um ID válido.")


def remover_contato():
    global contatos
    try:
        id_digitado = int(input("🗑️ Digite o ID do contato que deseja remover: "))

        for contato in contatos:
            if contato["id"] == id_digitado:
                contatos.remove(contato)
                atualizar_ids()
                salvar_dados()
                print(f"\n🗑️ Contato '{contato['nome']}' removido com sucesso!\n")
                break
        else:
            print("⚠️ ID não encontrado.")

    except ValueError:
        print("⚠️ Digite um número válido.")


def atualizar_ids():
    global contatos
    for indice, contato in enumerate(contatos, start=1):
        contato["id"] = indice


def menu_principal():
    carregar_dados()
    while True:
        print("\n=== 📇 AGENDA DE CONTATOS ===")
        print("[A] Adicionar contato")
        print("[V] Ver todos os contatos")
        print("[B] Buscar contato")
        print("[E] Editar contato")
        print("[R] Remover contato")
        print("[S] Sair")

        opcao = input("\nEscolha uma opção: ").upper()

        if opcao == "A":
            adicionar_contato()
        elif opcao == "V":
            ver_contatos()
        elif opcao == "B":
            buscar_contato()
        elif opcao == "E":
            editar_contato()
        elif opcao == "R":
            remover_contato()
        elif opcao == "S":
            salvar_dados()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("💾 Dados salvos! Até mais 👋")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

menu_principal()
