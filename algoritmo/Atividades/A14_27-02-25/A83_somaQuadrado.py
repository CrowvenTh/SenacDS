# Escreva um programa em Python que receba uma lista de números inteiros separados por espaço e determine a soma dos quadrados dos números na lista.
try:
    numero = input("Insira uma sequência de números separados por espaço: ").   split(" ")

    lista = [int(i)**2 for i in numero]
    print(lista)
    soma = sum(lista)
    print(soma)
except ValueError:
    print(ValueError)