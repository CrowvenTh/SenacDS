# Escreva um programa que solicite ao usuário dois números e uma operação:

while True:
    n = int(input("Insira um número: "))
    n1 = int(input("Insira outro número: "))

    print(f"| Soma = +\n| Subtração = -\n| Multiplicação = *\n| Divisão = /\n| Encerrar programa = 0")
    operacao = str(input("Selecione uma operação: "))
    if(operacao == 0):
        print("Programa encerrado...")
        break
    elif(operacao == "+"):
        print(f"Soma: {n} + {n1} = {n + n1}\n")
    elif(operacao == "-"):
        print(f"Subtração: {n} - {n1} = {n - n1}\n")
    elif(operacao == "*"):
        print(f"Multiplicação: {n} x {n1} = {n * n1}\n")
    elif(operacao == "/"):
        print(f"Divisão: {n} ÷ {n1} = {n / n1}\n")
