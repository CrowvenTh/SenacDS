# Escreva um programa em Python que receba uma lista de números inteiros separados por espaço e conte quantos números pares estão presentes na lista.

def contaPar():
    try:
        numero = input("Insira uma sequência de números separados por espaço: ").split(" ")
        lista = [int(i) for i in numero if (int(i) % 2 == 0)]
        print(lista)
        soma = len(lista)
        print(f"Você inseriu {soma} números pares")
    except ValueError:
        print(ValueError)

contaPar()
