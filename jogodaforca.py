#def jogar():
    # Jogo da forca
    print("********************************")
    print("Bem vindo ao jogo da Forca")
    print("********************************")

    # Lendo arquivo de palavras
    palavras = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper())

    numero = random.randrange(0, len(palavras))

    # Configurações do jogo
    palavrasecreta = palavras[numero].upper()
    letrasacertadas = ["_"] * len(palavrasecreta)
    total_tentativas = len(palavrasecreta)

    enforcou = False
    acertou = False
    tentativas = 0

    print("A palavra secreta tem {} letras".format(len(palavrasecreta)))
    print(letrasacertadas)
    desenhar_forca(tentativas)
   
    # Loop principal do jogo
    while(not enforcou and not acertou and tentativas < total_tentativas):
        chute = input("Digite uma letra? ")
        chute = chute.strip().upper()

        if (chute in palavrasecreta):
            index = 0
            for letra in palavrasecreta:
                if(chute == letra):
                    letrasacertadas[index] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                index = index + 1
        else:
            tentativas += 1
            desenhar_forca(tentativas)

        enforcou = tentativas == total_tentativas
        acertou = "_" not in letrasacertadas
        print("Letras acertadas:", letrasacertadas)
        print("Tentativas usadas:", tentativas)

        # Verifica se o jogador ganhou ou perdeu
        if acertou:
            mensagem_vencedor()
        elif enforcou:
            mensagem_perdedor(palavrasecreta)

    print("Fim do jogo")
if __name__ == "__main__":
    jogar()
