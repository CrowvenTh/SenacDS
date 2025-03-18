# Criar um dicionário para armazenar o nome e o telefone de uma pessoa e exibi-los.

contato = {}

nome = input("Insira o nome do contato: ")
numero = input("Insira o número de telefone: ")

contato["nome"] = nome
contato["numero"] = numero

print(contato)