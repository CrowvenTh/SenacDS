class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getAno(self,):
        return self.ano
    
    def setAno(self, ano):
        self.ano = ano


    def ExibirDados(self):
        print(f"Infomrções do Veículo: \n- Marca: {self.getMarca()}\n- Modelo: {self.getModelo()}\n- Ano: {self.getAno()}")

    def Ligar(self):
        print(f"{self.getModelo()} foi ligado!")

# coche = Veiculo("Honda", "Type R", 2020)
# coche.ExibirDados()
# coche.Ligar()
        