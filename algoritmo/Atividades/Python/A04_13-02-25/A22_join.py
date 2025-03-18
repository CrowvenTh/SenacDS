# 1 Crie um programa em Python que aceite uma TUPLA de linguagens de programação e as junte em uma única String separada por hífens, verificar o tipo da variável antes e após a operação

tupla = "Python", "Java", "C#", "PHP"
print(tupla)
print(type(tupla))
tupla_join = "-".join(tupla)
print(tupla_join)
print(type(tupla_join))

# 2 Crie um programa em Python que aceite uma Lista de linguagens de programação e as junte em uma String separada por hífens, verificar o tipo da variável antes e após a operação:

lista = ["Python", "Java", "C#", "PHP"]
print(lista)
print(type(lista))
lista_join = " - ".join(lista)
print(lista_join)
print(type(lista_join))