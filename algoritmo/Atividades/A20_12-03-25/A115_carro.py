from A115_veiculo import Veiculo

class Carro(Veiculo):

    def getPortas(self):
        return self.portas
    
    def setPortas(self, portas):
        self.portas = portas

    def ExibirDadosII(self):
        print(f"- Portas: {self.getPortas()}")

coche = Carro("Honda", "Type R", 2020)
coche.ExibirDados()
coche.setPortas(4)
coche.ExibirDadosII()
coche.Ligar()

