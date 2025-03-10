# # Crie uma classe chamada Agenda que armazena uma lista de contatos. Cada contato deve ter um nome e um número de telefone. A classe deve ter os seguintes métodos:
#     # adicionar_contato(nome, telefone): adiciona um contato à agenda.
#     # listar_contatos(): exibe todos os contatos armazenados.

class Agenda:
    def __init__(self):
        self.nomes = []
        self.telefones = []
        
    def adicionar_contato(self, nome, telefone):
        self.nomes.append(nome)
        self.telefones.append(telefone)
    
    def listar_contatos():
        for nome, telefone in self.nomes:
            print(f"{i} - Nome: {nome}\nTelefone: {telefone}")

listaTelefonica = Agenda()
listaTelefonica.adicionar_contato("Thiago","61 99788-8787")
listaTelefonica.listar_contatos()


notas={'João'   :  9,
       'Maria'  : 10,
       'José'   : 4  }

nome = input("Digite o nome do aluno: ")
nota = float(input("Nota dele: "))

if notas.get(nome):
    print("Ja existe o aluno ",nome)
else:
    notas[nome] = nota
print(notas)