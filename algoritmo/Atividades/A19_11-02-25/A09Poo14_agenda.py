class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome}: {self.telefone}"
contato1 = Contato("Thiago","61 99878-9099")

##########################################################################
    
class Agenda:
    def __init__(self):
        self.agenda = []

    def AdicionatContato(self,):
        nome = input("Insira seu nome: ").capitalize()
        telefone = input("Insira seu telefone: ")
        self.agenda.append({"Nome":nome, "Telefone":telefone})

    def ListarContatos(self):
        if(self.agenda == []):
            print("===| Não há contatos salvos na agenda")

        for i, agenda in enumerate(self.agenda, 1):
            nomes = agenda["Nome"]
            telefones = agenda["Telefone"]
            print(f"=======| Contato {i} |=========\n===|Nome: {nomes}\n===|Número: {telefones}\n=============================")

def Main():
    def Menu():
        print(""" 
    ==========================
    | 1 - Adicionar Contato  |
    | 2 - Listar Contatos    |
    | 3 - Buscar Contato     |
    | 4 - Remover Contato    |
    | 0 - Encerrar Programa  |
    ==========================
    """)
    agenda = Agenda()
    while True:
        Menu()
        op = int(input("Insira uma opção: "))
        match op:
            case 1:
                agenda.AdicionatContato()
            case 2:
                agenda.ListarContatos()
            case 3:
                print("opcão 3")
            case 4:
                print("opcão 4")
            case 0:
                print("Programa encerrado")
                break
            case _:
                print("Opção inválida")

Main()