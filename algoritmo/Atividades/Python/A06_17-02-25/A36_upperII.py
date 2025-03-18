# Escreva um programa que verifique se uma palavra está toda em letras maiúsculas.

word = input("Insira uma palavra: ")

if word == word.upper(): # if word.isupper():
    print("A palavra está em letras maiúsculas")
else:
    print("A palavra está em letras minúsculas")
