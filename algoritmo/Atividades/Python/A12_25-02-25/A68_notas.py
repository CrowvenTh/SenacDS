# Crie um programa que pede ao usuário uma nota de 0 a 10 e usa match-case para exibir a seguinte classificação:
# 9 ou 10: "Excelente"
# 7 ou 8: "Bom"
# 5 ou 6: "Regular"
# 3 ou 4: "Ruim"
# 0, 1 ou 2: "Muito ruim"

nota = int(input("Insira uma nota: "))

match nota:
    case 9 | 10:
        print("Excelente")
    case 7 | 8:
        print("Bom")
    case 5 | 6:
        print("Regular")
    case 3 | 4:
        print("Ruim")
    case 0 | 1 | 2:
        print("Muito ruim")