# Crie um função em Python, que receba 2 números e retorne a multiplicação dos 2 números.

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

def numXnum():
    resultado = num1 * num2
    return resultado

print(numXnum())

# Ou

def numXnum(num1,num2):
    resultado = num1 * num2
    print(resultado)

numXnum(num1, num2)