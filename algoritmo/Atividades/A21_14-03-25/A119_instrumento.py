class Instrumento:
    def __init__(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo

    def emitirSom(self):
        print(f"Som do instrumento")

