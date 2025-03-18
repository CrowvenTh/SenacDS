# Crie um dicionário representando um filme , contendo Título, Ano e Gênero. Depois, adicione a duração  e remova o campo "ano".

filme = {}

titulo = input("Insira o titulo: ")
ano = input("Insira o ano: ")
genero = input("Insira o genero: ")

filme["titulo"] = titulo
filme["ano"] = ano
filme["genero"] = genero
print(filme)

duracao = input("Insira a duração: ")
filme["duracao"] = duracao
print(filme)

del filme["ano"]
print(filme)