# Escreva um programa em Python que solicite ao usuário para adivinhar um número entre 1 e 100. O programa deve continuar pedindo um palpite até que o usuário adivinhe corretamente o número. O programa deve fornecer dicas se o palpite estiver muito alto ou muito baixo
import random

randomNumber = random.randint(1, 100)
print(randomNumber)
numero = int(input("Adivinhe o número: "))

while True:
    if(randomNumber > numero):
        print("Número incorreto, tente um palpilte maior")
    elif(randomNumber < numero):
        print("Número incorreto, tente um palpilte menor")
    elif(randomNumber == numero):
        print(f"{randomNumber}, número correto!")
        break
    numero = int(input("Adivinhe o número: "))