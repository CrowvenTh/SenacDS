# Faça um programa que transforme um texto todo em letras maiúsculas e conte quantas letras 'A' ele possui.

# palavra = input("Insira uma palavra: ")

# print(palavra.upper().count("A"))
palavra = input("Insira uma palavra: ").upper()
contagem = palavra.count("A")
print(f"a palavra {palavra} contém {contagem} letras 'A'")