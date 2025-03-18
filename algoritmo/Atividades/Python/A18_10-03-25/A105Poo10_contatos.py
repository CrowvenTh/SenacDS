# # Crie uma classe chamada Agenda que armazena uma lista de contatos. Cada contato deve ter um nome e um número de telefone. A classe deve ter os seguintes métodos:
#     # adicionar_contato(nome, telefone): adiciona um contato à agenda.
#     # listar_contatos(): exibe todos os contatos armazenados.

class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionar(self, nome, telefone):
        self.contatos.append({"Nome": nome, "Telefone": telefone})

    def listar_contatos(self):
        for i, listar_contatos in enumerate(self.contatos, 1):
            print(f"{i} - {listar_contatos}")

agenda1 = Agenda()
agenda1.adicionar("Thiago", "61 98787-9009")
agenda1.adicionar("Hiago", "61 98787-9009")
agenda1.adicionar("Thais", "61 98787-9009")
agenda1.listar_contatos()