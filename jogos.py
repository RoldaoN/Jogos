import forca
import adivinhacao

print("Escolha seu jogo")

print("(1)-Forca (2)-Adivinhação")

selecao = int(input ("Qual deseja jogar?"))

if(selecao == 1):
    print("Iniciando Forca.")
    forca.jogar()
elif (selecao == 2):
    print("Iniciando Adivinhação.")
    adivinhacao.jogar()