# Escreva um programa que solicite ao usuário para inserir um número e determine se é positivo, negativo ou zero.

numero = int(input("Digite um número: "))

if numero > 0:
    print("é número positivo")
elif numero < 0:
    print("é número negativo")
else: 
    print("é número neutro")
