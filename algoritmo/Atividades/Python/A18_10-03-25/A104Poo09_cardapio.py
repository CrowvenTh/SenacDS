# Crie uma classe chamada Restaurante que armazena um cardápio de pratos. A classe deve ter os seguintes métodos:
    # adicionar_prato(prato): adiciona um prato ao cardápio.
    # listar_cardapio(): exibe todos os pratos disponíveis.

class Restaurante:
    def __init__(self):
        self.cardapio = []

    def adicionar_prato(self, prato):
        self.cardapio.append(prato)
    
    def listar_cardapio(self):
        print("\n=====| Pai d'Égua |=====")
        for i, prato in enumerate(self.cardapio, 1):
            print(f"===| {i} - {prato}")
        print("=====|============|=====")

kardapio = Restaurante()
kardapio.adicionar_prato("Tacacá")
kardapio.adicionar_prato("Vatapá")
kardapio.adicionar_prato("Pato no Tucupi")
kardapio.adicionar_prato("Açaí com farinha")
kardapio.adicionar_prato("Maniçoba")
kardapio.listar_cardapio()