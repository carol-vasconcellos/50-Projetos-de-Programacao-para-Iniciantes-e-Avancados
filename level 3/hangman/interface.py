import tkinter as tk
import logic


def atualizar_interface():
    palavra_label.config(text=logic.get_palavra())

    e, t = logic.get_erros()
    erro_label.config(text=f"Erros: {e}/{t}")

    letras_label.config(text=f"Letras usadas: {logic.get_letras_usadas()}")

    if logic.ganhou():
        status_label.config(text="🎉 Você venceu!")
        desabilitar_botoes()

    elif logic.perdeu():
        status_label.config(text=f"💀 Você perdeu! Palavra: {logic.palavra_secreta}")
        desabilitar_botoes()


def clicar_letra(letra, botao):
    resultado = logic.tentar(letra)

    if resultado is None:
        return
    
    botao.config(state="disabled")
    atualizar_interface()


def desabilitar_botoes():
    for b in botoes:
        b.config(state="disabled")


def reiniciar():
    logic.iniciar_jogo()
    status_label.config(text="")
    
    for b in botoes:
        b.config(state="normal")
        
    atualizar_interface()


root = tk.Tk()
root.title("Forca Tkinter")
root.geometry("500x600")

logic.iniciar_jogo()

# UI
titulo = tk.Label(root, text="Jogo da Forca", font=("Arial", 24))
titulo.pack(pady=10)

palavra_label = tk.Label(root, text=logic.get_palavra(), font=("Arial", 28))
palavra_label.pack(pady=10)

erro_label = tk.Label(root, text="Erros: 0/6", font=("Arial", 16))
erro_label.pack(pady=10)

letras_label = tk.Label(root, text="Letras usadas:", font=("Arial", 12))
letras_label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 20))
status_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
botoes = []

linha = 0
coluna = 0

for letra in alfabeto:
    btn = tk.Button(frame, text=letra, width=4, height=2, 
                    command=lambda l=letra: clicar_letra(l, btn))
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

    botoes.append(btn)

    coluna += 1
    if coluna == 6:
        coluna = 0
        linha += 1

btn_reset = tk.Button(root, text="Reiniciar", command=reiniciar)
btn_reset.pack(pady=20)

root.mainloop()
