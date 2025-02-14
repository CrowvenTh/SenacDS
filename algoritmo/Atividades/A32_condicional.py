# Escreva um programa que solicite ao usuário para inserir dois números inteiros. O programa deve então verificar qual número é maior e imprimir uma mensagem correspondente.
num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif(num1 == num2):
    print(f"{num1} é igual a {num2}")
else: print(f"{num1} é menor que {num2}")