# # Crie um programa que verifique se uma pessoa é maior de idade.
# Situação: Este programa precisa lidar com a entrada de valores não inteiros ou negativos.

idade = float(input("Insira sua idade: "))

def MaiorIdade():
    try: 
        if (idade >= 18):
            print("Você é maior de idade")
        else:
            print("Você é menor de idade")
    except ValueError:
        print("Valor inválido")

MaiorIdade()
