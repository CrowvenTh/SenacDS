# Escreva um programa que leia uma lista de números e imprima apenas aqueles que são (números que podem ser lidos da mesma forma da esquerda para a direita e vice-versa).

def numerosPalindormos():
    try: 
        numeros = input("Insira uma sequência de números: ").split()
        lista = [int(i) for i in numeros if(int(i[::-1]) == int(i))]
        print(f"Os números palíndormos são: {lista}")
    except ValueError:
        print(ValueError)

numerosPalindormos()