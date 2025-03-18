class Estoque:
    def __init__(self, nome, estoque):
        self.nome = nome
        self.estoque = estoque

    def repor_estoque(self, quantidade):
        quantidade = input("insira a qtd a reabastecer: ")
        self.estoque += int(quantidade)
        print(f"Estoque reabastecido\nNova Quantidade: {self.estoque}")

est = Estoque("Relógio",100)
est.repor_estoque(50)