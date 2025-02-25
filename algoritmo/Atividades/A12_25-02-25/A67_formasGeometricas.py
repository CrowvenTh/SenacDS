# Escreva um programa em Python que solicita ao usuário o nome de uma forma geométrica (triângulo, quadrado, círculo) e utiliza match-case para exibir uma mensagem correspondente à forma escolhida.

forma = input("Insira uma forma geométrica geometrica: ")
lados = 0

match forma:
    case "QUADRADO":
        lados = 4
        print(f"O {forma} tem {lados} lados.")
    case "TRIÂNGULO":
        lados = 3
        print(f"O {forma} tem {lados} lados.")
    case "CÍRCULO":
        lados = 0
        print(f"O {forma} não contem lados nem vértices, pois ele é redondo.")
    case _ :
        print(f"Insira uma opção válida")

        