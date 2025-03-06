# Crie um programa que cadastre um produto em um dicionário, incluindo nome, preço e quantidade. Em seguida, adicione a marca do produto, remova o item "quantidade" e exiba o dicionário atualizado.

produto = {}

nome = input("Insira o nome: ")
preco = input("Insira o preço: ")
quantidade = input("Insira a quantidade: ")

produto["nome"] = nome
produto["preco"] = preco
produto["quantidade"] = quantidade

print(produto)

marca = input("Insira a marca: ")
produto["marca"] = marca

print(produto)

del produto["quantidade"]

print(produto)