# Escreva um programa que solicite ao usuário um número e depois imprima todos os números pares de 1 até esse número, imprimir em ordem decresce, usando um loop while.

numero = int(input("Insira um número: "))
contador = numero

while (contador > 0):
    if(contador % 2 == 0):
        print(contador)
    contador -= 1