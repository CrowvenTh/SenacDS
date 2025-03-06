# Objetivo: Criar um dicionário para armazenar informações de um produto e exibi-las depois.

#criação do dicionário vazio 
meuCarro = {}

# implementação de input nos atributos do dicionario
marca = input("Insira a marca: ")
modelo = input("Insira o modelo: ")
ano = input("Insira o ano do veiculo: ")
cor = input("Insira a cor do veiculo: ")

# atribuição dos inputs aos atributos do dicionario
meuCarro["marca"] = marca
meuCarro["modelo"] = modelo
meuCarro["ano"] = ano
meuCarro["cor"] = cor

# mostrando o dicionario
print("Informações sobre o carro: ")
print(meuCarro)