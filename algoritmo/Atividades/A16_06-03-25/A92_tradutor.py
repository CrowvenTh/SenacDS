# Criar um dicionário com palavras em inglês e suas traduções para português e permitir que o usuário consulte uma palavra.
dicionario = {
    "dog":"cachorro",
    "cat":"gato",
    "house":"casa",
    "car":"carro"
}
palavra = input("Insira uma palavra: ")

if palavra in dicionario:
    print(f"{palavra.capitalize()} | PTBR: {dicionario[palavra].capitalize()}")
else:
    print(f"chave não encontrada")