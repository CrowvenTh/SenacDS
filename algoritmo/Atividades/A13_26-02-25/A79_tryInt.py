# Crie um programa que receba um número inteiro e retorne uma mensagem de erro, caso o usuário informe número fracionado ou letra.

try:
    numero = int(input("Insira um número inteiro: "))
    print("Valor inserido corretamente")
except ValueError:
    print("Valor inválido")
    