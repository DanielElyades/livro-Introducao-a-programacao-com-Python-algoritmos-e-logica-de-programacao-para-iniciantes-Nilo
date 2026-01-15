# Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de
# juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

# Ler o depósito inicial
deposito = float(input("Qual o valor inicial: "))
saldo = deposito
# Ler a taxa de juros da poupança
taxa = float(input("Qual a taxa de juros da poupança: "))

# Converter para taxa de juros mensal
taxa_mensal = taxa / 12
taxa_mensal = taxa_mensal / 100

# Contador
mes = 0
resultado = 0

# Calculo usando while
while mes <= 24:
    saldo = saldo + (saldo * taxa_mensal)
    mes = mes + 1
    print(f"Resultado do mês {mes}: {saldo:.2f}")

print(f"Saldo inicial: {saldo - deposito:.2f}")
print(f"Saldo final: {saldo:.2f}")