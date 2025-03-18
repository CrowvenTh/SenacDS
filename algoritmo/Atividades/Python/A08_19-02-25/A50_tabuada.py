# Escreva um programa que imprima a tabuada de multiplicação de um número específico até 10, usando um loop while.

numero = int(input("Insira um número:"))
cont = 0

while cont <= 10:
    print(f"{numero} x {cont} = {numero * cont}")
    cont +=1
