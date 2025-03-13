from A113_contaCorrente import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def rendimento(self, taxa):
        self.saldo += self.saldo * taxa
        print(f"Rendimento aplicado! Saldo atual: R${self.saldo:.2f}")

poupanca1 = ContaPoupanca("Thiago", 2100)
poupanca1.rendimento(0.10)
# poupanca1.ExibirSaldo()