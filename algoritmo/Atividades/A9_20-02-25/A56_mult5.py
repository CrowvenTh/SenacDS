# Escreva um programa que imprima os múltiplos de 5 de 1 até o número informado pelo usuário.

while True:
    n = int(input("insira um número: "))
    if(n % 5 == 0):
        print(f"O número {n} é múltiplo de 5")
    else: 
        print(f"O número {n} não é múltiplo de 5")
        break
