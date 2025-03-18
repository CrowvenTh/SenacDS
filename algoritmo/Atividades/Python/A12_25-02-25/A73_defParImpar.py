# Escreva uma função chamada par_ou_impar que aceita um número como argumento e retorna "par" se o número for par e "ímpar" se o número for ímpar.

n = int(input("Insira um número: "))

def parImpar(n):
    if(n % 2 == 0):
        resultado = f"O número {n} é par!"
    else:
        resultado = f"O número {n} é par!"
    return resultado
print(parImpar(n))

# ou

def ParOuImpar():
    if(n % 2 == 0):
        resultado = f"O número {n} é par!"
    else:
        resultado = f"O número {n} é par!"
    print(resultado)
