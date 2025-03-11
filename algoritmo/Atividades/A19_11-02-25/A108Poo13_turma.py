class Turma:
    def __init__(self):
        self.alunos = []

    def AdicionaAluno(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.alunos.append({"Nome":nome, "Idade":idade})

    def ListarAlunos(self):
        print("=======| TURMA A |=======")
        for i, alunos in enumerate(self.alunos, 1):
            nomes = alunos["Nome"]    
            idades = alunos["Idade"]
            print(f"===| ID: {i}\n===| Nome: {nomes}\n===| Idade: {idades}\n=====================")
    
turma_A = Turma()    
turma_A.AdicionaAluno("Thiago","20")
turma_A.AdicionaAluno("Gabrielle","21")
turma_A.AdicionaAluno("Brunna","26")
turma_A.AdicionaAluno("Diana","19")
turma_A.AdicionaAluno("Tadeu","24")
turma_A.ListarAlunos()
    