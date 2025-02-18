# Escreva um programa que solicite ao usuário um número e depois imprima todos os números pares de 1 até esse número, usando um loop while

numero = int(input("Insira um número: "))
contador = 0
while contador < numero:
    contador += 2
    print(contador)