# Faça um programa que receba um número de 1 a 5 e retorne um prato específico usando match-case. As opções podem ser:

print("\n--------------\n| 1 - Pizza\n| 2 - Hambúguer\n| 3 - Sushi\n| 4 - Salada\n| 5 - Lasanha\n|--------------")
id = int(input("Selecione um prato: "))

match id:
    case 1:
        print("Pizza foi selecionada")
    case 2:
        print("Hambúrguer foi selecionado")
    case 3:
        print("Sushi foi selecionado")
    case 4:
        print("Salada foi selecionada")
    case 5:
        print("Lasanha foi selecionada")
    case _:
        print("Opção inválida")
