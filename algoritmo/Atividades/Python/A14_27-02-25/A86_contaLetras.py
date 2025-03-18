# Escreva um programa em Python que receba uma lista de palavras separadas por espaço e determine quantas palavras têm mais de 5 letras.

palavra = input("Insira uma sequência de palavras separadas por espaço: ").split()

lista = [i for i in palavra if(len(i) >= 5)]
print(lista)
validador = len(lista)
print(f"Qtd de palavras com mais de 5 letras: {validador}")