# Programa para calcular a média de uma lista de números.
# Situação: Este programa precisa permitir de valores com casas decimais ou negativos. 
# Observação: Toda a lista vai ser inserida em um único input

def CalcularMedia():
    try: 
        n = input("Insira uma sequencia de numeros separados por espaço: ").    split   (" ")
        lista = [float(i) for i in n]
        media = sum(lista)/len(lista)
        print(media)
    except ValueError:
        print("Valor inválido") 

CalcularMedia()