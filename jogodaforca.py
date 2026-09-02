import importlib.machinery
from pathlib import Path
import random


desenhos = importlib.machinery.SourceFileLoader(
    "desenhos", str(Path(__file__).with_name("desenhos.txt"))
).load_module()


def jogar():
    # Jogo da forca
    print("********************************")
    print("Bem vindo ao jogo da Forca")
    print("********************************")

    # Lendo arquivo de palavras
    palavras = []

    caminho_palavras = Path(__file__).with_name("palavras.txt")
    with caminho_palavras.open("r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavra = linha.strip().upper()
            if palavra:
                palavras.append(palavra)

    if not palavras:
        print("Nenhuma palavra foi cadastrada.")
        return

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
    desenhos.desenhar_forca(tentativas)
   
    # Loop principal do jogo
    while(not enforcou and not acertou and tentativas < total_tentativas):
        try:
            chute = input("Digite uma letra? ")
        except EOFError:
            print("\nJogo interrompido.")
            return
        chute = chute.strip().upper()

        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra.")
            continue

        if (chute in palavrasecreta):
            index = 0
            for letra in palavrasecreta:
                if(chute == letra):
                    letrasacertadas[index] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                index = index + 1
        else:
            tentativas += 1
            desenhos.desenhar_forca(tentativas)

        enforcou = tentativas == total_tentativas
        acertou = "_" not in letrasacertadas
        print("Letras acertadas:", letrasacertadas)
        print("Tentativas usadas:", tentativas)

        # Verifica se o jogador ganhou ou perdeu
        if acertou:
            desenhos.mensagem_vencedor()
        elif enforcou:
            desenhos.mensagem_perdedor(palavrasecreta)

    print("Fim do jogo")
if __name__ == "__main__":
    jogar()
