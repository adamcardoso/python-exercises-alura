import forca
import jogo_de_adivinhacao

print("********************************")
print("*********Escolha seu jogo!*******")
print("********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual é o jogo? "))

if (jogo == 1):
    print("Jogando Forca")
elif (jogo == 2):
    print("Jogando Adivinhação")