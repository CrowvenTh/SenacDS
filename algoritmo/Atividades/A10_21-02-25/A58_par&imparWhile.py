# Escreva um programa que solicita ao usuário uma sequência de números inteiros positivos e conta quantos números pares e quantos números ímpares foram digitados. O programa deve encerrar, quando for inserido um número negativo.

contPar = 0
contImpar = 0
while True:
    n = int(input("Insira um número: "))
    if(n <= 0):
        print(f"{contPar} números pares foram digitados!")
        print(f"{contImpar} números impares foram digitados!")
        break
    elif(n % 2 == 0):
        contPar += 1
    else:
        contImpar += 1

