# Crie um programa que receba 4 notas de um aluno e calcule a média:
# Nota >= 6 Aprovado
# Nota < 6 e nota > 4 Recuperação
# Nota <= 4 Reprovado

count = 0
notaTotal = 0
while count < 4:
        nota = 0
        count += 1
        nota = float(input(f"Insira a {count}° nota: "))
        notaTotal += nota
        if(count == 4):
                media = (notaTotal / count)
                print(f"A média das nota é: {media:.1f}")
                if(media >= 6):
                        print("O aluno está aprovado!")
                elif(media < 6 and media > 4):
                        print("O aluno está de recuperação!")
                else:
                        print("O aluno está reprovado!")
                        
                