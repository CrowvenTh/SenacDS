# Escreva um programa em Python que receba uma lista de números inteiros separados por espaço e determine quantos números são divisíveis por 3 e 5 simultaneamente.

def divisiveisPor3e5():
    numero = input("Insira uma sequência de números separados por espaço: ").split()
    lista = [int(i) for i in numero if(int(i) % 3 == 0 and int(i) % 5 == 0)]
    print(lista)
    contDivisiveis = len(lista)
    print(f"{contDivisiveis} números são divisíveis por 3 e 5 simultâneamente: {lista} ")

divisiveisPor3e5()