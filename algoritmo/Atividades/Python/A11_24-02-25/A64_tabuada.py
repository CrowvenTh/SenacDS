# Imprima a tabuada de multiplicação de um número fornecido pelo usuário.
numero = int(input("Insira o número desejado: "))

for t in range(11):
    print(f"{numero} x {t} = {numero * t}")
