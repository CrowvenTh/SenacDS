from A119_instrumento import Instrumento

class Guitarra(Instrumento):
    def __init__(self, tipo, cordas):
        super().__init__(tipo)
        self.__cordas = cordas

    def getCordas(self):
        return self.__cordas
    
    def setCordas(self, cordas):
        self.__cordas = cordas

    def emitirSom(self):
        super().emitirSom()
        print(f"Som de guitarra")

guitarra = Guitarra("guitarra", 16)
guitarra.emitirSom()
