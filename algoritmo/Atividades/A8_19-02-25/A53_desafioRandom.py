# Escreva um programa em Python que solicite ao usuário para adivinhar um número entre 1 e 100. O programa deve continuar pedindo um palpite até que o usuário adivinhe corretamente o número. O programa deve fornecer dicas se o palpite estiver muito alto ou muito baixo
import random

randomNumber = random.randint(1, 100)
# print(randomNumber)
numero = int(input("Adivinhe o número: "))

while randomNumber != numero:
    print("número incorreto, tente novamente!")
    numero = int(input("Adivinhe o número: "))
    if(randomNumber == numero):
        print(f"{randomNumber}, número correto!")