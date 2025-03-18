class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def VerificaAprovacao(self):
        if(self.nota >= 7):
            print(f"{self.nome} - aprovado!")
        else:
            print(f"{self.nome} - reprovado!")

#==== Instância de Objeto ====#

aluno1 = Aluno("Thiago", 8.9)
aluno1.VerificaAprovacao()

aluno2 = Aluno("Thalles", 6.3)
aluno2.VerificaAprovacao()

