# Defina uma função, que receba 3 números e retorne o maior deles

n = int(input("Insira um número: "))
n1 = int(input("Insira um número: "))
n2 = int(input("Insira um número: "))

def maiorNumero():
    if(n > n1 and n > n2):
        print(f"{n} é maior que {n1} e {n2}")
    elif(n1 > n2 and n1 > n):
        print(f"{n1} é maior que {n2} e {n}")
    elif(n2 > n and n2 > n1):
        print(f"{n2} é maior que {n} e {n1}")

maiorNumero()