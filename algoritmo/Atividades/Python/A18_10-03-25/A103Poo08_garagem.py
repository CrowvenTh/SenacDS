class Garagem:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self,modelo):
        self.modelo = modelo
        self.carros.append(modelo)

    def listar_carros(self):
        print("\n=========| GARAGEM |=========")
        for i, self.modelo in enumerate(self.carros, 1):
            print(f"{i} - {self.modelo}")
        print("=============================")

carros1 = Garagem()
carros1.adicionar_carro("Civic Type R")
carros1.adicionar_carro("GTR R34")
carros1.adicionar_carro("NSX")
carros1.adicionar_carro("240SX")
carros1.adicionar_carro("RAM TRX")
carros1.adicionar_carro("Challenger")
carros1.listar_carros()
