# faça um programa que receba o valor de emprestimo e a quantidade de parcelas, se as parcelas forem maior que 10 então acresça juros de 15%,caso conrário 10%. mostre os resultados finais e uma lista com a quantidade de parcelas.

valor = float(input("Insira o valor do empréstimo: "))
parcela = int(input("Insira a quantidade de parcelas: "))

if parcela <= 10:
    juros = valor + valor * 0.10
else: 
    juros = valor + valor * 0.15

print(f"Valor total: R${juros}")

for i in range (1, parcela):
    print(f"Parcela: {i} - {(juros / parcela):.2f} ")

