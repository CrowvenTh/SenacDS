# Escreva uma função chamada soma que aceita dois argumentos e retorna a soma deles.

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))

def soma(n1, n2):
    return n1 + n2
resultado = soma(n1,n2)

print(resultado)

# OU

def somaII():
    soma = n1 + n2
    print(f"A soma de {n1} + {n2} é igual a {soma}")

somaII()