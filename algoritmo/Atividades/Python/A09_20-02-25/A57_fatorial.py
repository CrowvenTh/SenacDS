# Implemente um programa que imprima o fatorial do número informado pelo usuário.

n = int(input("Insira um número: "))
fatorial = 0
cont = 1
while cont <= n:
    fatorial += cont
    cont += 1
print(fatorial)
    