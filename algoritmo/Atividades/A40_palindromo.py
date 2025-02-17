# Crie um programa que verifique se um palavra é um palíndromo(Igual, quando lida de trás para frente).

palavra = input("escreva uma palavra: ")

if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é um palíndromo")
else:
    print(f"A palavra {palavra} não é um palíndromo")


