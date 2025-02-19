# Escreva um programa em Python que solicite ao usuário para adivinhar um número entre 1 e 100. O programa deve continuar pedindo um palpite até que o usuário adivinhe corretamente o número. O programa deve fornecer dicas se o palpite estiver muito alto ou muito baixo
import random

randomNumber = random.randint(1, 5)
numero = int(input("Adivinhe o número: "))
on = True

while on:
    if(randomNumber != numero):
        print("número incorreto, tente novamente!")
    else:
        print(f"{random}, número correto!")