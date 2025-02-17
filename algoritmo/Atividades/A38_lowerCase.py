# Escreva um programa que verifique se uma palavra está toda em letras minúsculas.

palabra = str(input("Insira uma palavra: "))

if(palabra.islower()):
    print(f"A palavra {palabra} está escrita em letras minúsculas!")
else:
    print(f"A palavra {palabra} está escrita em letras maiúsculas!")