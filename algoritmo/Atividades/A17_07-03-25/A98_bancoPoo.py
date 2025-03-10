class Banco:
    saldo = 0
    def __init__(self,titular):
        self.titular = titular
    
    def Titular(self):
        self.titular = input("Insira o nome do titular: ")

    def MostrarSaldo(self):
        print(f"===| Titular: {self.titular}\n===| Saldo atual: R${self.saldo}\n")

    def DepositarValor(self):
        self.deposito = float(input("===| Insira o valor do deposito: "))
        self.saldo += self.deposito
        print(f"===| Titular: {self.titular}\n===| Depósito de R${self.deposito} realizado com sucesso!\n")
    
    def SacarValor(self):
        self.saque = float(input("===| Insira o valor do saque: "))
        self.saldo -= self.saque
        print(f"===| Titular: {self.titular}\n===| Saque de R${self.saque} realizado com sucesso!\n")
def Menu():
    print("""
          ===| Titular: {self.titular}\n
          ===| 1 - Deposito \n
          ===| 2 - Saque \n
          ===| 3 - Saldo \n
          ===| 4 - Encerrar
          """)
    option = int(input(""))

while True:
    conta = Banco()
    conta.Titular()
    Menu()
    option = int(input(""))
    match option:
        case 1:
            conta.DepositarValor()
            Menu()
        case 2:
            conta.SacarValor()
            Menu()
        case 3:
            conta.MostrarSaldo()
            Menu()
        case 4:
            print("Programa encerrado...")
            break
        case _:
            print("Opção inválida!")
            Menu()