import tkinter as tk
from tkinter import messagebox
import random

# CONFIGURAÇÃO
tamanho = 8
tamanhos_navios = [2, 3, 3]

modo_ia = True  # definido pelo menu
vez = 1         # 1 = jogador 1, 2 = jogador 2 ou IA


def criar_tabuleiro():
    return [["~"] * tamanho for _ in range(tamanho)]


tab_navios_1  = criar_tabuleiro()
tab_visivel_1 = criar_tabuleiro()

tab_navios_2  = criar_tabuleiro()
tab_visivel_2 = criar_tabuleiro()


def posicionar_navios(tab):
    for tamanho_navio in tamanhos_navios:
        colocado = False
        while not colocado:
            orient = random.choice(["H", "V"])
            l = random.randint(0, tamanho - 1)
            c = random.randint(0, tamanho - 1)

            if orient == "H":
                if c + tamanho_navio > tamanho:
                    continue
                pos = [(l, c + i) for i in range(tamanho_navio)]
            else:
                if l + tamanho_navio > tamanho:
                    continue
                pos = [(l + i, c) for i in range(tamanho_navio)]

            if any(tab[x][y] == "N" for x, y in pos):
                continue

            for x, y in pos:
                tab[x][y] = "N"
            colocado = True


def acabou(tab):
    for linha in tab:
        if "N" in linha:
            return False
    return True


def atirar(l, c, board_nav, board_vis, botoes):
    if board_vis[l][c] != "~":
        return False

    if board_nav[l][c] == "N":
        board_nav[l][c] = "X"
        board_vis[l][c] = "X"
        botoes[l][c].config(text="💥", bg="red", fg="white")
    else:
        board_vis[l][c] = "o"
        botoes[l][c].config(text="🌊", bg="blue", fg="white")

    return True


def jogada_ia():
    livres = [(l, c) for l in range(tamanho) for c in range(tamanho)
              if tab_visivel_1[l][c] == "~"]

    l, c = random.choice(livres)
    atirar(l, c, tab_navios_1, tab_visivel_1, botoes_1)

    if acabou(tab_navios_1):
        messagebox.showinfo("Derrota!", "A IA afundou todos seus navios!")
        reiniciar()


def clicar_adversario(l, c):
    global vez

    if vez != 1:
        return

    if not atirar(l, c, tab_navios_2, tab_visivel_2, botoes_2):
        return

    if acabou(tab_navios_2):
        messagebox.showinfo("Vitória!", "Você afundou todos os navios inimigos!")
        reiniciar()
        return

    vez = 2

    if modo_ia:
        root.after(500, turno_ia)


def clicar_jogador_duplo(l, c):
    global vez

    if modo_ia:
        return

    if vez != 2:
        return

    if not atirar(l, c, tab_navios_1, tab_visivel_1, botoes_1):
        return

    if acabou(tab_navios_1):
        messagebox.showinfo("Vitória Jogador 2!", "Jogador 2 venceu!")
        reiniciar()
        return

    vez = 1


def turno_ia():
    global vez
    jogada_ia()
    vez = 1


def reiniciar():
    global tab_navios_1, tab_navios_2, tab_visivel_1, tab_visivel_2, vez

    tab_navios_1 = criar_tabuleiro()
    tab_visivel_1 = criar_tabuleiro()
    tab_navios_2 = criar_tabuleiro()
    tab_visivel_2 = criar_tabuleiro()

    posicionar_navios(tab_navios_1)
    posicionar_navios(tab_navios_2)

    vez = 1

    for linha in botoes_1:
        for btn in linha:
            btn.config(text=" ", bg="SystemButtonFace")

    for linha in botoes_2:
        for btn in linha:
            btn.config(text=" ", bg="SystemButtonFace")


def abrir_menu_modo():
    menu = tk.Toplevel()
    menu.title("Escolha o modo de jogo")
    menu.geometry("350x180")

    tk.Label(menu, text="Selecione o modo:", font=("Arial", 16)).pack(pady=10)

    frame_opcoes = tk.Frame(menu)
    frame_opcoes.pack(pady=10)

    tk.Button(frame_opcoes, text="Contra IA", font=("Arial", 14),
              width=12, command=lambda: iniciar_jogo(menu, True)).grid(row=0, column=0, padx=10)

    tk.Button(frame_opcoes, text="Multiplayer", font=("Arial", 14),
              width=12, command=lambda: iniciar_jogo(menu, False)).grid(row=0, column=1, padx=10)


def iniciar_jogo(menu, usar_ia):
    global modo_ia
    modo_ia = usar_ia
    menu.destroy()
    reiniciar()


root = tk.Tk()
root.title("Battleship Avançado — IA ou Multiplayer")
root.geometry("800x650")

tk.Label(root, text="⚓ Battleship Avançado", font=("Arial", 22)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

left = tk.LabelFrame(frame, text="Tabuleiro do Jogador 1")
left.grid(row=0, column=0, padx=30)

right = tk.LabelFrame(frame, text="Tabuleiro do Inimigo")
right.grid(row=0, column=1, padx=30)

botoes_1 = []
botoes_2 = []

# Criar tabuleiro do jogador
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        btn = tk.Button(left, width=3, height=1, font=("Arial", 14),
                        command=lambda i=i, j=j: clicar_jogador_duplo(i, j))
        btn.grid(row=i, column=j, padx=2, pady=2)
        linha.append(btn)
    botoes_1.append(linha)

# Criar tabuleiro do inimigo
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        btn = tk.Button(right, width=3, height=1, font=("Arial", 14),
                        command=lambda i=i, j=j: clicar_adversario(i, j))
        btn.grid(row=i, column=j, padx=2, pady=2)
        linha.append(btn)
    botoes_2.append(linha)

tk.Button(root, text="Escolher Modo de Jogo", font=("Arial", 16),
          command=abrir_menu_modo).pack(pady=10)

tk.Button(root, text="Reiniciar Jogo", font=("Arial", 16),
          command=reiniciar).pack(pady=10)

reiniciar()

root.mainloop()
