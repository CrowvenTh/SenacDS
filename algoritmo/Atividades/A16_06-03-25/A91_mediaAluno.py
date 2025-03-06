# Criar um dicionário para armazenar as notas de um aluno e calcular a média.

aluno = {}

nota1 = float(input("Insira a 1° nota: "))
nota2 = float(input("Insira a 2° nota: "))
nota3 = float(input("Insira a 3° nota: "))
media = (nota1 + nota2 + nota3) / 3

aluno["nota1"] = nota1
aluno["nota2"] = nota2
aluno["nota3"] = nota3
aluno["media"] = media

print(aluno)

