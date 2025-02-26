# Escreva um programa que calcula a média ponderada de três números fornecidos pelo usuário, onde os pesos são fornecidos pelo usuário também.

def MediaPonderada():
    medPonderada = (nota1 * p1) + (nota2 * p2) + (nota3 * p3) / (p1 + p2 + p3)
    print(f"A média ponderada das notas é: {medPonderada}")

nota1 = float(input("Insira 1° a nota: "))
p1 = int(input("Insira o peso 1: "))

nota2 = float(input("Insira 2° a nota: "))
p2 = int(input("Insira o peso 2: "))

nota3 = float(input("Insira 3° a nota: "))
p3 = int(input("Insira o peso 3: "))

MediaPonderada()