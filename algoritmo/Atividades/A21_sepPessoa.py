# Escreva um programa em Python que use o parâmetro sep na função print() para imprimir o nome, idade e altura de uma pessoa separados por um hífen.

nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
altura= float(input("Insira sua altura: "))

print(f"nome - idade - altura\n{nome} - {idade} - {altura}" )