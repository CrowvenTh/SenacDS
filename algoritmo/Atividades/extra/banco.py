print("--------------------\n-----| Banco | -----\n--------------------")
def menu():
    print("| Selecione uma opção:\n| 0 - Encerrar programa \n| 1 - Realizar depósito \n| 2 - Realizar Saque \n| 3 - Verificar Saldo\n--------------------")

menu()
opcao = int(input(" "))
saldo = 0
while True:
        if(opcao == 1):
            deposito = float(input("| Insira o valor do depósito: "))
            saldo += deposito
            print(f"| Depósito de R${deposito:.2f} realizado com sucesso!\n| Saldo atual: R${saldo:.2f}\n")
            menu()
            opcao = int(input(" "))
        elif(opcao == 2):
            saque = float(input("| Insira o valor do saque: "))
            if(saque > saldo):
                print("| Saldo insuficiente!\n")
            else:
                print(f"| Saque de R${saque:.2f} realizado com sucesso!\n| Saldo atual: R${saldo:.2f}\n")
                saldo -= saque
                menu()
                opcao = int(input(" "))
        elif(opcao == 3):
            print(f"| Saldo atual: R${saldo:.2f}\n")
            menu()
            opcao = int(input(" "))
        else:
            print("| Programa encerrado.\n")
            break
