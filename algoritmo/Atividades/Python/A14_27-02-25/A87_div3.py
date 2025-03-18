# Escreva um programa que leia uma lista de números e imprima apenas aqueles que são divisíveis por 3.

def divisiveisPor3():
    try:
        numeros = input("Insira uma sequência de números: ").split()
        lista = [int(i) for i in numeros if(int(i) % 3 == 0 and int(i) > 0)]
        print(f"Números divisíveis por 3: {lista}")
    except ValueError:
        print(ValueError)
divisiveisPor3()