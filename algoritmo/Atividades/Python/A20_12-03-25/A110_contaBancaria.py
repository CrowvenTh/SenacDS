class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, saldo):
        self.__saldo = saldo

conta1 = ContaBancaria("Thiago", 2100)
print(conta1.getSaldo())
print(conta1.titular)