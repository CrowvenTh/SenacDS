# Crie um programa que receba dois números e faça a divisão dos dois, e crie uma mensagem de erro da divisão por zero ou se o usuário informar algo diferente de números.

def Divisao():
    media = n1 / n2
    print(f"O resultado da divisão é: {media}")
    
n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))

try:
    Divisao()
except ZeroDivisionError:
    print("Divisão inválida")