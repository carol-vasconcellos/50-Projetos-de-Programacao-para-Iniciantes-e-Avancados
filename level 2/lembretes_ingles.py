import json
import os # Módulo para verificar se o arquivo existe

FILEPATH = 'dicionario_pt_en.json'

def load_data():
    """Carrega o dicionário do arquivo JSON. Se o arquivo não existir, retorna um dicionário vazio."""
    if os.path.exists(FILEPATH):
        try:
            with open(FILEPATH, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Aviso: O arquivo JSON está vazio ou corrompido. Iniciando com um dicionário vazio.")
            return {}
    return {}

def save_data(data):
    """Salva o dicionário no arquivo JSON."""
    with open(FILEPATH, 'w', encoding='utf-8') as file:
        # Usa ensure_ascii=False para salvar acentos e caracteres corretamente
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("\n✅ Dicionário atualizado e salvo com sucesso!")

def add_translation(data):
    """Permite ao usuário adicionar uma nova palavra/frase e sua tradução."""
    print("\n--- Adicionar Nova Tradução ---")
    
    # Recebe a palavra ou frase em INGLÊS (será a CHAVE no dicionário)
    english_word = input("Digite a palavra/frase em INGLÊS: ").strip().lower()
    
    # Verifica se a tradução já existe para evitar sobrescrever acidentalmente
    if english_word in data:
        print(f"⚠️ A palavra '{english_word}' já está no dicionário com a tradução: {data[english_word]}")
        overwrite = input("Deseja sobrescrever (S/N)? ").strip().lower()
        if overwrite != 's':
            return # Sai da função sem adicionar/salvar

    # Recebe a tradução em PORTUGUÊS (será o VALOR)
    portuguese_translation = input("Digite a tradução em PORTUGUÊS: ").strip()

    # Adiciona/atualiza o dicionário
    data[english_word] = portuguese_translation
    
    # Salva o dicionário imediatamente
    save_data(data)

def consult_translation(data):
    """Permite ao usuário consultar a tradução de uma palavra/frase."""
    print("\n--- Consultar Tradução ---")
    
    # Recebe a palavra/frase em INGLÊS para consulta
    english_word = input("Digite a palavra/frase em INGLÊS para consultar: ").strip().lower()
    
    # Busca a tradução usando .get() para uma busca segura
    translation = data.get(english_word, "Tradução não encontrada no dicionário. Tente adicioná-la!")
    
    print(f"\nResultado da Consulta:")
    print(f"INGLÊS: {english_word}")
    print(f"PORTUGUÊS: {translation}")


# --- FUNÇÃO PRINCIPAL ---
def run_translator():
    # Carrega os dados na inicialização
    dictionary = load_data()
    
    while True:
        print("\n==============================")
        print("  DICIONÁRIO INGLÊS-PORTUGUÊS")
        print("==============================")
        print("1. Consultar Tradução")
        print("2. Adicionar Nova Tradução")
        print("3. Sair")
        
        choice = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if choice == '1':
            consult_translation(dictionary)
        elif choice == '2':
            add_translation(dictionary)
        elif choice == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")

# Inicia o programa
if __name__ == "__main__":
    run_translator()