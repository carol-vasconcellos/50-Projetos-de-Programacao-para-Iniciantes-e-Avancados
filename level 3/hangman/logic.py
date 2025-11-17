import random

palavras = ["banana", "python", "seguranca", "rede", "roteador", "switch", "firewall"]

palavra_secreta = ""
estado_palavra = []
erros = 0
tentativas_max = 6
letras_usadas = []


def iniciar_jogo():
    global palavra_secreta, estado_palavra, erros, letras_usadas
    palavra_secreta = random.choice(palavras)
    estado_palavra = ["_"] * len(palavra_secreta)
    erros = 0
    letras_usadas = []


def tentar(letra):
    """Retorna True se acerto, False se erro"""
    global erros
    
    letra = letra.lower()

    # validações
    if len(letra) != 1 or not letra.isalpha() or letra in letras_usadas:
        return None  

    letras_usadas.append(letra)

    if letra in palavra_secreta:
        for i, c in enumerate(palavra_secreta):
            if c == letra:
                estado_palavra[i] = letra
        return True
    else:
        erros += 1
        return False


def get_palavra():
    return " ".join(estado_palavra)

def get_erros():
    return erros, tentativas_max

def get_letras_usadas():
    return ", ".join(letras_usadas)

def ganhou():
    return "_" not in estado_palavra

def perdeu():
    return erros >= tentativas_max
