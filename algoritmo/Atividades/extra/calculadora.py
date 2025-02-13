print("-----| Calculadora |-----")
num1 = int(input("Insira o primeiro número: "))
print(num1,"\n")

print("Escolha a operação:\n| + = Multiplicação\n| - = Subtração\n| * = Multiplicação\n| / = Divisão\n--------------------\n")
operacao = input()
print("A operação selecionada foi:",operacao,"\n")

num2 = int(input("Insira o segundo número: "))
print(num2,"\n")

def calculo():
    if (operacao == "+"):
        resultado = (num1 + num2)
        print(f"{num1} + {num2} = {resultado}")
    elif (operacao == "-"):
        resultado = (num1 - num2)
        print(f"{num1} - {num2} = {resultado}")
    elif (operacao == "*"):
        resultado = (num1 * num2)
        print(f"{num1} x {num2} = {resultado}")
    else:
        resultado = (num1 / num2)
        print(f"{num1} / {num2} = {resultado}")

print(calculo())
    

    