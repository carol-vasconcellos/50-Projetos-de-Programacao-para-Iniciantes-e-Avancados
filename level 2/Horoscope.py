def previsao(signo):
    mensagens = {
        "Aquário": "💧 Inovadora e sonhadora. O futuro está nas suas mãos!",
        "Peixes": "🐟 Sensível e empática. Hoje é dia de cuidar do coração.",
        "Áries": "🔥 Corajosa e determinada. A ação te levará longe!",
        "Touro": "🌿 Persistente e confiável. Um bom momento para planejar.",
        "Gêmeos": "💨 Curiosa e comunicativa. As ideias estão a mil!",
        "Câncer": "🌙 Afetuosa e protetora. Cuide de quem ama.",
        "Leão": "☀️ Carismática e intensa. Seu brilho inspira os outros!",
        "Virgem": "🌾 Organizada e prática. Hoje o foco trará resultados.",
        "Libra": "⚖️ Equilibrada e gentil. Harmonia é sua força.",
        "Escorpião": "🦂 Profunda e leal. Use sua intuição com sabedoria.",
        "Sagitário": "🏹 Aventureira e otimista. O mundo é seu campo de descoberta!",
        "Capricórnio": "⛰️ Disciplinada e ambiciosa. O sucesso vem passo a passo."
    }

    return mensagens.get(signo, "✨ Signo desconhecido, mas energia boa por aí!")

def descobrir_signo(dia, mes):
    
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Peixes"
    
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    
    else:
        return "Capricórnio"
    
def main():
    while True:
        iniciar = input("\n🔮 Deseja descobrir seu signo do [z]odíaco ou [s]air? ").lower()

        if iniciar == 's':
            print("Até mais!! 🌙")
            break

        elif iniciar == 'z':
            try:
                dia = int(input("Digite o dia do seu nascimento: "))
                mes = int(input("Digite o mês do seu nascimento (número): "))
            except ValueError:
                print("⚠️ Por favor, digite números válidos!")
                continue  # volta pro começo do loop

            if dia < 1 or dia > 31 or mes < 1 or mes > 12:
                print("⚠️ Data inválida! Tente novamente.")
                continue

            signo = descobrir_signo(dia, mes)
            mensagem = previsao(signo)

            print("\n✨ Seu signo é:", signo)
            print(mensagem)
            print("--------------------------------")
        else:
            print("⚠️ Opção inválida! Digite [z] ou [s].")

main()    