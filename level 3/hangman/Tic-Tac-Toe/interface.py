import tkinter as tk
from tkinter import messagebox
import random

# --------------------------------------
# VARIÁVEIS DO JOGO
# --------------------------------------
jogador_humano = "X"
jogador_pc = "O"
tabuleiro = [""] * 9

combinacoes = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

# --------------------------------------
# MINIMAX – IA IMPARÁVEL
# --------------------------------------
def minimax(tab, jogador):

    vencedor = verificar_vencedor_simples(tab)
    if vencedor == jogador_pc:
        return 1
    elif vencedor == jogador_humano:
        return -1
    elif all(c != "" for c in tab):
        return 0  # empate

    if jogador == jogador_pc:
        melhor_valor = -999
        for i in range(9):
            if tab[i] == "":
                tab[i] = jogador_pc
                valor = minimax(tab, jogador_humano)
                tab[i] = ""
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor

    else:
        melhor_valor = 999
        for i in range(9):
            if tab[i] == "":
                tab[i] = jogador_humano
                valor = minimax(tab, jogador_pc)
                tab[i] = ""
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor


def melhor_jogada():
    melhor_valor = -999
    melhor_movimento = None

    for i in range(9):
        if tabuleiro[i] == "":
            tabuleiro[i] = jogador_pc
            valor = minimax(tabuleiro, jogador_humano)
            tabuleiro[i] = ""

            if valor > melhor_valor:
                melhor_valor = valor
                melhor_movimento = i

    return melhor_movimento


# --------------------------------------
# FUNÇÕES DO JOGO
# --------------------------------------
def clicar_botao(indice):
    if tabuleiro[indice] != "":
        return

    tabuleiro[indice] = jogador_humano
    botoes[indice].config(text=jogador_humano)

    if verificar_fim():
        return

    root.after(200, jogada_pc)  # pequena espera para naturalidade


def jogada_pc():
    movimento = melhor_jogada()

    tabuleiro[movimento] = jogador_pc
    botoes[movimento].config(text=jogador_pc)

    verificar_fim()


def verificar_vencedor_simples(tab):
    for a, b, c in combinacoes:
        if tab[a] == tab[b] == tab[c] and tab[a] != "":
            return tab[a]
    return None


def verificar_fim():
    vencedor = verificar_vencedor_simples(tabuleiro)
    if vencedor:
        messagebox.showinfo("Fim de jogo", f"Jogador {vencedor} venceu!")
        reiniciar()
        return True

    if all(c != "" for c in tabuleiro):
        messagebox.showinfo("Fim de jogo", "Deu velha! Empate.")
        reiniciar()
        return True

    return False


def reiniciar():
    global tabuleiro
    tabuleiro = [""] * 9
    for botao in botoes:
        botao.config(text="")


# --------------------------------------
# INTERFACE TKINTER
# --------------------------------------
root = tk.Tk()
root.title("Tic-Tac-Toe (IA Imbatível)")
root.geometry("300x500")

titulo = tk.Label(root, text="Tic-Tac-Toe (IA Imbatível)", font=("Arial", 18))
titulo.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

botoes = []

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        width=6,
        height=3,
        font=("Arial", 20),
        command=lambda i=i: clicar_botao(i)
    )
    btn.grid(row=i // 3, column=i % 3)
    botoes.append(btn)

btn_reset = tk.Button(root, text="Reiniciar Jogo", font=("Arial", 14), command=reiniciar)
btn_reset.pack(pady=15)

root.mainloop()
