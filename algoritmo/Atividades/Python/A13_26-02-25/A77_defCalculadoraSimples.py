# Criar um programa que simula uma calculadora básica com operações de adição, subtração, multiplicação e divisão. O programa solicitará ao usuário que escolha a operação desejada, inserindo um número correspondente, e então pedirá os dois números nos quais a operação será realizada. Por fim, mostrará o resultado da operação escolhida.

def Soma():
    soma = (n1 + n2)
    print(f"{n1} + {n2} = {soma}")


def Sub():
    sub = (n1 - n2)
    print(f"{n1} - {n2} = {sub}")


def Mult():
    mult = (n1 * n2)
    print(f"{n1} x {n2} = {mult}")


def Div():
    div = (n1 / n2)
    print(f"{n1} ÷ {n2} = {div}")


n1 = float(input("Insira o primeiro número: "))


def operacao():
    print(f"| 1 - Adição\n| 2 - subtração\n| 3 - Multiplicação\n| 4 - Divisão")


operacao()

operacao = int(input("Selecione uma operação: "))

n2 = float(input("Insira o segundo número: "))

match operacao:
    case 1:
        Soma()
    case 2:
        Sub()
    case 3:
        Mult()
    case 4:
        Div()
