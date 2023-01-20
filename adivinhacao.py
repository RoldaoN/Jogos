import random as random

def jogar():
    print("Bem vindo ao jogo de advinhação!")

    secreto = random.randint(1,101)
    print(secreto)
    tentativas = 0
    pontos = 1000

    print("Qual o Nivel de dificuldade?")
    print("(1) - Facíl (2) - Médio (3) Difícil")

    nivel = int(input("Escolha o nível desejado: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas + 1):
        print("Rodada {} de {}".format(rodada,tentativas))

        chute_str = input ("Digite um numero entre 1 e 100: ")
        chute = int(chute_str)

        perdidos = abs(secreto - chute)

        print("Voce digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 a 100")
            continue

        if (secreto == chute):
            print("Você acertou!Você fez {} pontos".format(pontos))
            break
        else:
            if(chute < secreto):
                print("Você errou! O numero digitado é menor que o numero secreto")
            elif(chute > secreto):
                print("Você errou! O numero digitado é maior que o numero secreto")
            pontos = pontos - perdidos

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()