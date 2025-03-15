from A114_contaBancariaII import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def rendimento(self, taxa):
        rend = self.getSaldo() * taxa # ajustar calculo
        self.setSaldo(rend)
        print(f"Rendimento aplicado! Saldo atual: R${rend:.2f}")


poupanca = ContaPoupanca("Thiago", 0)
poupanca.Deposito(500)
poupanca.Saque(100)
poupanca.rendimento(0.10)