class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.compras = []
    
    def adicionar_compra(self):
        self.valor = input("Insira o valor da compra: ")
        self.compras.append(self.valor)

    def historico(self):
        print(f"===| Histórico de Cliente |===\n===| {self.nome}")
        for i in self.compras:
            print(f"===| Histórico: {i}")

cliente1 = Cliente("Thiago")
cliente1.adicionar_compra()
cliente1.adicionar_compra()
cliente1.adicionar_compra()
cliente1.historico()