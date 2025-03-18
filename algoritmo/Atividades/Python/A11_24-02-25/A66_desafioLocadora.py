# Faça uma programa que dados a quantidade de fitas que uma vídeo locadora possui e o valor que ela cobra por cada aluguel, informe:
# Sabendo que um terço das fitas são alugadas por mês, qual o seu faturamento anual.

# Sabendo que quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel

# Um décimo das fitas alugadas no mês são devolvidas com atraso é o valor ganho com multas por mês.

estoque = int(input("Informe quantas fitas a locadora possui: "))
valorAluguel = float(input("Informe o valor do aluguel: "))

totalAluguel = (estoque / 3) * valorAluguel
totalMulta = (totalAluguel * 0.1) * 12
faturamento = (totalAluguel * 12) + totalMulta

print(f"---------------------------")
print(f"Faturamento mensal: R${totalAluguel:.2f}")
print(f"Faturamento com multas: R${totalAluguel * 12:.2f}")
print(f"Faturamento anual: R${faturamento:.2f}")
print(f"---------------------------\n")