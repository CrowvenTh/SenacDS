def inicio():
    print("_______________________________")
    print("---|------ CALCULADORA -----|")
    print("---|------------------------|")
inicio()


def menu():
    print("---| Selecione uma operação |---")
    print("---| + : Adição             |")
    print("---| - : Subtração          |")
    print("---| * : Multiplicação      |")
    print("---| / : Divisão            |")
    print("---|------------------------|")
    print("---| 0 : Encerrar           |")
    print("---|------------------------|")
n1 = 0
n2 = 0
def numero():
    n1 = float("Insira o primeiro número: ")
    n2 = float("Insira um o segundo: ")

def soma():
    return n1 + n2

def subtracao():
    return n1 - n2

def multiplicacao():
    return n1 * n2
    
def divisao():
    if n2 > n1:
        print("Operação inválida!")
    else:
        n1 / n2

while True:
    n1 = float("Insira o primeiro número: ")
    menu()
    operacao = str(input())
    n2 = float("Insira um o segundo: ")
    match operacao:
        case "+":
            menu()
            numero()
            soma()
        case "-":
            menu()
            numero()
            subtracao()
        case "*":
            menu()
            numero()
            multiplicacao()
        case "/":
            menu()
            numero()
            divisao()
        case _:
            print("Operação inválida, tente novamente")
    break
