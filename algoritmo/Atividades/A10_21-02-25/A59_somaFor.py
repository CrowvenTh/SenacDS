# Escreva um programa que solicite ao usuário dois números e uma operação:

for i in range(1, 2): # no rango, pode-se ler os parentes como primeira posição menos a segunda: range(1, 2) significa que vai começar em 1 e vai até o 2, executando o loop apenas uma vez
    n = int(input("Insira um número: "))
    n1 = int(input("Insira outro número: "))
    print(f"a soma de {n} + {n1} = {n + n1}")
