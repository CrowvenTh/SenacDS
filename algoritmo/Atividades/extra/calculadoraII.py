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
    menu()
    operacao = str(input())
    n1 = float("Insira o primeiro número: ")
    n2 = float("Insira um o segundo: ")
    match operacao:
        case "+":
            menu()
            soma()
        case "-":
            menu()
            subtracao()
        case "*":
            menu()
            multiplicacao()
        case "/":
            menu()
            divisao()
        case _:
            print("Operação inválida, tente novamente")
    break
