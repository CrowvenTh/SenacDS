numeros = input("um número: ")

lista = [int(i) for i in numeros]
soma = sum(lista)
if(soma == int(numeros)):
    print(f"{soma} é um número perfeito")
print(lista)
print(soma)