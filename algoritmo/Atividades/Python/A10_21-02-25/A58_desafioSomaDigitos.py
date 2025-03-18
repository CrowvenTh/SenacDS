# Escreva um programa que solicita ao usuário um número inteiro positivo e calcula a soma dos seus dígitos.

numero = input("Digite um número: ")
soma = 0
cont= 0

while cont < len(numero):
    soma += int(numero[cont]) 
    cont += 1  
print("A soma dos caracteres é:", soma)