import forca
import jogo_de_adivinhacao

print("********************************")
print("*********Escolha seu jogo!*******")
print("********************************")

print("(1) Forca (2) Adivinhação (3) Sair")

jogo = int(input("Qual é o jogo? "))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação")
    jogo_de_adivinhacao.jogar()
elif (jogo == 3):
    print("Saindo...")